#!/usr/bin/env python3
import argparse
import json
from mm_creator_core import lint_style

parser = argparse.ArgumentParser(description="Lint a Suno Style prompt")
parser.add_argument("style")
parser.add_argument("--max-chars", type=int, default=1000, help="Verified runtime budget; default is a project policy, not an official platform limit")
args = parser.parse_args()
print(json.dumps(lint_style(args.style, args.max_chars), ensure_ascii=False, indent=2))
