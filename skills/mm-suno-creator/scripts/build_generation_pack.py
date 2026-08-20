#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from mm_creator_core import render_pack

parser = argparse.ArgumentParser(description="Render a standard Suno generation pack")
parser.add_argument("input", type=Path)
parser.add_argument("--output", type=Path)
args = parser.parse_args()
result = render_pack(json.loads(args.input.read_text(encoding="utf-8")))
if args.output:
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding="utf-8")
else:
    print(result)
