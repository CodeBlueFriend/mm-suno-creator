#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from mm_creator_core import analyze_lyrics

parser = argparse.ArgumentParser(description="Estimate lyric structure and sung duration")
parser.add_argument("lyrics_file", type=Path)
args = parser.parse_args()
print(json.dumps(analyze_lyrics(args.lyrics_file.read_text(encoding="utf-8")), ensure_ascii=False, indent=2))
