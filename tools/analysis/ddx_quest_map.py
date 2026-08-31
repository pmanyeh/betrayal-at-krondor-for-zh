#!/usr/bin/env python3
"""Betrayal at Krondor -- DDX quest / story-flag map.

Betrayal at Krondor has no "quest" data structure. Story progress lives in a
flat pool of event flags (``gstate_event_read`` / ``gstate_event_write``) that
DDX dialogue records read as branch conditions and write as side effects. This
tool decodes every ``DIAL_Zxx.DDX`` record's choices and opcodes into readable
prose so a human can group the flag/conversation clusters into named quests.

Opcode / condition semantics are transcribed from the engine:
  * bak/SRC/DIALOG/DIALOG.C   -- dialog_play_record()'s opcode switch + the
                                choice matcher (DdxChoice.wCond / dwTarget_key)
  * bak/SRC/DIALOG/EVTCOND.C  -- evtcond_dialog_action_dispatch() (wOp 7)

Anything still uncertain is prefixed ``?`` in the output; verify against the
source before relying on it.

Output (under docs/research/quest-map/):
  DIAL_Zxx.md      one section per keyed node: speaker, gate conditions,
                   effects, branches, translated text excerpt
  _flags.md        every event-flag id -> written-by / read-by cross reference
  _effects.md      index of "reward-ish" nodes (grant spell / raise stat /
                   give item / consume encounter / change party)
  _README.md       the legend and how to read the reports

Usage:
    python tools/analysis/ddx_quest_map.py
    python tools/analysis/ddx_quest_map.py --ddx-dir scratchpad/pristine \\
        --translated-dir localization/translated --out docs/research/quest-map
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools" / "text"))
from ddx_extract import extract_ddx_data  # noqa: E402

TEXT_EXCERPT = 240


def _u32(nA1: int, nA2: int) -> int:
    return (nA2 << 16) | nA1


def _s16(v: int) -> int:
    """DDX amounts are read into signed shorts; 0xFD00 means -768, not 64768."""
    return v - 0x10000 if v >= 0x8000 else v


# g_abStatNames order (DIALOG.C:25); 16 is the Health+Stamina pseudo-stat.
STAT_NAMES = [
    "Health", "Stamina", "Speed", "Strength", "Defense", "Crossbow Acc",
    "Melee Acc", "Casting Acc", "Assessment", "Armorcraft", "Weaponcraft",
    "Barding", "Haggling", "Lockpick", "Scouting", "Stealth",
]


def _stat(idx: int) -> str:
    return STAT_NAMES[idx] if 0 <= idx < len(STAT_NAMES) else (
        "Health+Stamina" if idx == 16 else f"stat#{idx}")


def decode_record_flags(f: int) -> list[str]:
    bits = {
        0x0040: "reload-scr-between-pages",
        0x0100: "?flag0x100",
        0x0200: "paged-text",
        0x0400: "ASK-ABOUT keyword menu",
        0x0800: "random branch (RND over choices)",
    }
    return [name for bit, name in bits.items() if f & bit]


def decode_condition(wCond: int, nA3: int, nA4: int, chapter_names: dict[int, str]) -> str:
    """DdxChoice.wCond matcher, from DIALOG.C ~line 1548."""
    if wCond == 0:
        return "always"
    if wCond >= 56000 and wCond % 10 == 0:
        bmi = (wCond - 56000) // 10
        xor = nA3 & 0xFF
        mask = (nA3 >> 8) & 0xFF
        mode = nA4 & 0xFF
        chapbits = (nA4 >> 8) & 0xFF
        chs = ",".join(str(i + 1) for i in range(8) if chapbits & (1 << i)) or "-"
        return (f"event_bitmap_hi[{bmi}] (xor={xor:#04x} mask={mask:#04x} "
                f"mode={mode} chapters={chs})")
    return f"flag {wCond:#06x} in [{nA3}..{nA4}]"


def decode_opcode(op: dict[str, int]) -> str:
    """DdxOp.wOp, from DIALOG.C's opcode switches + EVTCOND.C for wOp 7."""
    w = op["wOp"]
    a1, a2, a3, a4 = op["nA1"], op["nA2"], op["nA3"], op["nA4"]
    if w == 0:
        return None  # padding / no-op
    if w == 1:
        return f"bind speaker-name slot (kind={a1} sub={a2})"
    if w == 6:
        return f"frame/rect style override x={a1} y={a2} w={a3} h={a4}"
    lo = a1 & 0xFF          # (unsigned char)op->nA1
    who = (a1 >> 8) & 0x7F  # high byte = party-member selector on give/take
    if w == 2:
        if lo == ord("5"):
            return f"GIVE gold +{a2 * 10}"
        if lo == ord("6"):
            return f"GIVE gold +{a2}"
        tgt = f"member#{who}" if who > 1 else "party"
        return f"GIVE item {chr(lo)!r} cond={a2} to {tgt} (cost {a3})"
    if w == 3:
        if lo == 0x35:
            return f"TAKE gold -{a2 * 10}"
        if lo == 0x36:
            return f"TAKE gold -{a2}"
        return f"REMOVE item {chr(lo)!r} cond={a2}"
    if w == 4:
        if a1 == 0x7534:
            return f"set party-speaker = {a4}"
        if a1 == 0x7538:
            return f"set npc-speaker = {a4}"
        if a1 >= 56000 and a1 % 10 == 0:
            return f"event_bitmap_hi[{(a1 - 56000)//10}] bitop"
        parts = [f"SET flag {x:#06x}={a4}" for x in (a1, a2, a3) if x]
        return "; ".join(parts) if parts else "SET flag (none)"
    if w == 5:
        return f"preload portraits {a1:#x},{a2:#x},{a3:#x},{a4:#x}"
    if w == 7:
        return "ACTION: " + decode_action(op)
    if w == 8:
        tgt = f"member#{a1 - 2}" if a1 > 1 else "party"
        rng = f"{_s16(a3)}" if a3 == a4 else f"{_s16(a3)}..{_s16(a4)}"
        return f"apply status/condition to {tgt} idx={a2} amt={rng}"
    if w == 9:
        tgt = f"member#{a1 - 2}" if a1 > 1 else "party"
        rng = f"{_s16(a3)}" if a3 == a4 else f"{_s16(a3)}..{_s16(a4)}"
        verb = "DAMAGE" if _s16(a3) < 0 else "RAISE"
        return f"{verb} {_stat(a2)} of {tgt} by {rng}"
    if w == 10:
        return f"read {_stat(a2)} -> dlg-result (sel={a1})"
    if w == 11:
        return f"play sfx {a1}"
    if w == 12:
        if a2 == 1:
            return f"play {'sfx' if a1 < 1000 else 'music'} {a1}"
        if a2 == 2:
            return f"(on-exit) play {'sfx' if a1 < 1000 else 'music'} {a1}"
        return f"?wOp12 a1={a1} a2={a2}"
    if w == 13:
        return f"advance in-game time by {_u32(a1, a2)}"
    if w == 14:
        return f"SET flag {a1:#06x}=1 + timer ({_u32(a3, a4)})"
    if w == 15:
        return "free paged image table"
    if w == 0x10:
        return f"push return-address key {_u32(a1, a2)} (GoodBye target)"
    if w == 17:
        return f"SET PARTY size={a1} members=[{a2},{a3},{a4}]"
    if w == 18:
        who = "speaker" if a1 > 1 else "party"
        return f"HEAL {who} amt={a2}"
    if w == 19:
        return f"set combatant bitmap bit (sel={a1} bit={a2})"
    if w == 20:
        return f"load teleport table {a1}"
    if w == 22:
        return f"timer upsert kind={a1 & 0xff} sub={a2} ({_u32(a3, a4)})"
    if w == 23:
        return f"consume party items kind={a1:#x} x{a2}"
    if w == 0x15:
        return f"END conversation, result={a1}"
    if w == 0xC:
        return f"?wOp0xC a1={a1} a2={a2}"
    return f"?wOp {w} a1={a1} a2={a2} a3={a3} a4={a4}"


ACTION_NAMES = {
    0: lambda o: "deduct gold (EvtArgGoldCost)",
    1: lambda o: "add gold (EvtArgValue)",
    2: lambda o: "repair party armour",
    3: lambda o: f"CONSUME region encounter #{o['nA2']}",
    4: lambda o: f"mark region encounter #{o['nA2']} defended (roster killed)",
    5: lambda o: "spawn+clone inventory (obj 0x14)",
    6: lambda o: "spawn+clone inventory (obj 0x14)",
    7: lambda o: f"EvtArgValue += {o['nA2']}",
    8: lambda o: f"gambling resolve (max {o['nA2']}/{o['nA3']} payout {o['nA4']}%)",
    9: lambda o: "restore worn category-1 items",
    10: lambda o: "spawn fixed objs 0x14/0x1e, clone inv",
    11: lambda o: f"popup-retry-state = max(state, {o['nA2']})",
    12: lambda o: "request hotspot activation at player",
    13: lambda o: "reset kind-1/sub-0 timers, tick",
    14: lambda o: "clear fixed-obj (3) inventory",
    15: lambda o: "RAISE stat (EvtArgActor0, stat=EvtArgValue, +0x200)",
    16: lambda o: "SHARE Owyn<->Pug spellbooks",
}


def decode_action(op: dict[str, int]) -> str:
    fn = ACTION_NAMES.get(op["nA1"])
    return fn(op) if fn else f"?action nA1={op['nA1']} nA2={op['nA2']}"


def load_translations(translated_dir: Path) -> dict[str, dict[int, str]]:
    """file-stem -> {rec_index -> translated (or source) text}."""
    out: dict[str, dict[int, str]] = {}
    for p in sorted(translated_dir.glob("DIAL_*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        by_idx: dict[int, str] = {}
        for e in data.get("entries", []):
            eid = e.get("id", "")
            if "#" not in eid:
                continue
            try:
                idx = int(eid.rsplit("#", 1)[1])
            except ValueError:
                continue
            txt = e.get("translation") or e.get("source") or ""
            by_idx[idx] = txt.replace("\x00", "").replace("\n", " ").replace("\t", " ").strip()
        out[p.stem] = by_idx
    return out


REWARD_KEYS = ("RAISE ", "DAMAGE ", "SHARE Owyn", "GIVE item", "SET PARTY",
               "CONSUME region", "HEAL ", "GIVE gold", "advance in-game time")


def is_reward_node(effects: list[str]) -> bool:
    return any(any(k in e for k in REWARD_KEYS) for e in effects)


def analyse(ddx_dir: Path, translated_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    translations = load_translations(translated_dir)

    flag_writes: dict[int, list[str]] = defaultdict(list)
    flag_reads: dict[int, list[str]] = defaultdict(list)
    reward_rows: list[str] = []
    summary_rows: list[str] = []

    for ddx in sorted(ddx_dir.glob("DIAL_Z*.DDX")):
        stem = ddx.stem
        data = extract_ddx_data(ddx.read_bytes())
        tx = translations.get(stem, {})
        # reverse map: which node_ids does each record fall under (keyed records only)
        idx_to_node = {r["rec_index"]: r["node_id"] for r in data["records"]}

        lines = [f"# {stem}", "",
                 f"{data['total_records']} records, {len(data['dir_entries'])} keyed nodes", ""]
        n_reward = n_flagwrite = 0

        for r in data["records"]:
            ridx = r["rec_index"]
            node = r["node_id"]
            tag = f"{stem}#{ridx}"

            effects = []
            for op in r["opcodes"]:
                d = decode_opcode(op)
                if d:
                    effects.append(d)
                if op["wOp"] == 4:
                    for x in (op["nA1"], op["nA2"], op["nA3"]):
                        if x and not (x in (0x7534, 0x7538) or x >= 56000):
                            flag_writes[x].append(f"{tag} = {op['nA4']}")
                            n_flagwrite += 1
                if op["wOp"] == 14 and op["nA1"]:
                    flag_writes[op["nA1"]].append(f"{tag} = 1 (timer)")

            branches = []
            for c in r["choices"]:
                cond = decode_condition(c["wCond"], c["nA3"], c["nA4"], {})
                tgt = _u32(c["nA1"], c["nA2"])
                branches.append(f"[{cond}] -> node {tgt}" + ("" if tgt else " (no jump)"))
                if c["wCond"] and not (c["wCond"] >= 56000):
                    flag_reads[c["wCond"]].append(f"{tag} (branch)")

            # only emit a section for keyed nodes or records with real content
            if node is None and not effects and not branches:
                continue

            text = tx.get(ridx, "")
            excerpt = (text[:TEXT_EXCERPT] + "...") if len(text) > TEXT_EXCERPT else text

            head = f"## node {node}  ({tag})" if node is not None else f"### (sub) {tag}"
            lines.append(head)
            meta = [f"speaker={r['speaker_id']}", f"style={r['style']}"]
            rf = decode_record_flags(r["flags"])
            if rf:
                meta.append("flags=" + "|".join(rf))
            lines.append("- " + "  ".join(meta))
            if effects:
                lines.append("- effects:")
                lines += [f"    - {e}" for e in effects]
            if branches:
                lines.append("- branches:")
                lines += [f"    - {b}" for b in branches]
            if excerpt:
                lines.append(f"- text: {excerpt}")
            lines.append("")

            if is_reward_node(effects):
                n_reward += 1
                payoff = "; ".join(e for e in effects
                                   if any(k in e for k in REWARD_KEYS) or "ACTION" in e)
                cell = excerpt[:120].replace("|", "/").replace("\n", " ")
                reward_rows.append(f"| {stem} | {tag} | node {node} | {payoff} | {cell} |")

        (out_dir / f"{stem}.md").write_text("\n".join(lines), encoding="utf-8")
        summary_rows.append(f"| {stem} | {data['total_records']} | {len(data['dir_entries'])} | {n_flagwrite} | {n_reward} |")

    # _flags.md
    fl = ["# Event-flag cross reference", "",
          "Every event-flag id touched by a DDX choice condition or a SET opcode.",
          "`written by` = a wOp 4 / wOp 14 SET; `read by` = a DdxChoice branch condition.", ""]
    for fid in sorted(set(flag_writes) | set(flag_reads)):
        fl.append(f"## flag {fid:#06x}  ({fid})")
        if flag_writes.get(fid):
            fl.append("- written by: " + ", ".join(sorted(set(flag_writes[fid]))))
        if flag_reads.get(fid):
            fl.append("- read by: " + ", ".join(sorted(set(flag_reads[fid]))))
        fl.append("")
    (out_dir / "_flags.md").write_text("\n".join(fl), encoding="utf-8")

    # _effects.md
    ef = ["# Reward / progression nodes", "",
          "Nodes whose opcodes grant a spell, raise a stat, give an item, change",
          "the party, heal, or consume a region encounter -- the quest-payoff-ish",
          "records. Read the linked DIAL_Zxx.md for full branch context.", "",
          "| file | record | node | effect | text |", "|---|---|---|---|---|"]
    ef += reward_rows
    (out_dir / "_effects.md").write_text("\n".join(ef), encoding="utf-8")

    # _README.md
    rd = ["# DDX quest map -- how to read this", "",
          "Generated by `tools/analysis/ddx_quest_map.py`. Semantics transcribed",
          "from `DIALOG.C` and `EVTCOND.C`; `?` marks anything unverified.", "",
          "## Files", "",
          "- `DIAL_Zxx.md` -- one section per keyed node (a conversation entry",
          "  point the engine can jump to). Shows speaker, record flags, decoded",
          "  effects (opcodes), decoded branches (choices -> target node), and a",
          "  translated-text excerpt.",
          "- `_flags.md` -- event-flag id -> which records SET it / branch on it.",
          "  This is the story state machine: follow a flag from its writer to its",
          "  readers to trace a quest's progress gates.",
          "- `_effects.md` -- the subset of nodes that hand out spells / stats /",
          "  items / party changes / encounter completions.", "",
          "## Turning this into a quest list", "",
          "1. Pick a chapter. Skim `_effects.md` for that chapter's payoffs.",
          "2. For each payoff node, open its `DIAL_Zxx.md` section, read the text,",
          "   note the flags it SETs.",
          "3. In `_flags.md`, find who else reads those flags -- that's the rest of",
          "   the quest chain (the NPC who reacts once it's done, the hotspot that",
          "   unlocks, etc).",
          "4. Name the cluster, write its objective from the dialogue text, mark",
          "   main vs side and whether a chapter boundary makes it missable.", "",
          "## Opcode legend (DdxOp.wOp)", "",
          "```",
          "2   give gold / give item",
          "3   take gold / remove item",
          "4   SET event flag(s) (nA1..nA3 = ids, nA4 = value)",
          "7   ACTION dispatch (see EVTCOND.C): nA1 selects --",
          "      0 deduct gold   1 add gold   3 consume encounter   4 kill encounter",
          "      15 raise stat   16 share Owyn/Pug spells   ...",
          "8   apply status/condition   9 modify stat   10 read stat -> result",
          "13  advance time   14 set flag + timer   17 SET PARTY composition",
          "18  heal   20 load teleport table   23 consume party items",
          "0x10 push GoodBye return address   0x15 end conversation (result)",
          "```", "",
          "## Condition legend (DdxChoice.wCond)", "",
          "```",
          "0                       always (unconditional branch)",
          "flag id in [nA3..nA4]   branch taken iff nA3 <= gstate_event_read(id) <= nA4",
          ">=56000, %10==0         event_bitmap_hi[(wCond-56000)/10] bit + chapter test",
          "```", ""]
    (out_dir / "_README.md").write_text("\n".join(rd), encoding="utf-8")

    sm = ["# DDX quest-map summary", "",
          "| file | records | keyed nodes | flag writes | reward nodes |",
          "|---|---|---|---|---|"]
    sm += summary_rows
    (out_dir / "_summary.md").write_text("\n".join(sm), encoding="utf-8")

    print(f"wrote {len(summary_rows)} file reports + _flags/_effects/_summary/_README to {out_dir}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ddx-dir", type=Path, default=REPO / "scratchpad" / "pristine")
    ap.add_argument("--translated-dir", type=Path, default=REPO / "localization" / "translated")
    ap.add_argument("--out", type=Path, default=REPO / "docs" / "research" / "quest-map")
    args = ap.parse_args()
    analyse(args.ddx_dir, args.translated_dir, args.out)


if __name__ == "__main__":
    main()
