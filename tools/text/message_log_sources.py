#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY = ROOT / "docs/research/message-log-source-policy.json"
OUTPUT = ROOT / "upstream/betrayal-at-krondor/bak/SRC/DIALOG/CAPCLASS.INC"


def load_policy(path: Path = POLICY) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    ranges = data["excluded_ranges"]
    keys = data["excluded_keys"]
    if any(item["first"] > item["last"] for item in ranges):
        raise ValueError("excluded range is reversed")
    ordered = sorted(ranges, key=lambda item: (item["first"], item["last"]))
    for left, right in zip(ordered, ordered[1:]):
        if left["last"] >= right["first"]:
            raise ValueError("excluded ranges overlap")
    if len({item["key"] for item in keys}) != len(keys):
        raise ValueError("excluded key is duplicated")
    return data


def is_excluded(key: int, policy: dict | None = None) -> bool:
    data = load_policy() if policy is None else policy
    key &= 0x7FFFFFFF
    return any(item["first"] <= key <= item["last"] for item in data["excluded_ranges"]) or any(
        item["key"] == key for item in data["excluded_keys"]
    )


def render(policy: dict | None = None) -> str:
    data = load_policy() if policy is None else policy
    lines: list[str] = []
    for item in data["excluded_ranges"]:
        lines.extend(
            [
                f"if (key >= {item['first']}UL && key <= {item['last']}UL)",
                "    return 1;",
            ]
        )
    keys = sorted(item["key"] for item in data["excluded_keys"])
    if keys:
        conditions = [f"key == {key}UL" for key in keys]
        current = "if (" + conditions[0]
        for condition in conditions[1:]:
            if len(current) + len(condition) + 4 > 92:
                lines.append(current + " ||")
                current = "    " + condition
            else:
                current += " || " + condition
        lines.extend([current + ")", "    return 1;"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        return 0 if OUTPUT.exists() and OUTPUT.read_text(encoding="ascii") == expected else 1
    OUTPUT.write_text(expected, encoding="ascii", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
