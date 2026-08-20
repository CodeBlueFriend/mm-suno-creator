#!/usr/bin/env python3
import argparse
import json
from mm_creator_core import query_tags

parser = argparse.ArgumentParser(description="Search the MM Suno tag dictionary")
parser.add_argument("query")
parser.add_argument("--limit", type=int, default=8)
args = parser.parse_args()
print(json.dumps(query_tags(args.query, args.limit), ensure_ascii=False, indent=2))
