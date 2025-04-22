#!/usr/bin/env python3
import sys

# This mapper processes user actions and identifies interactions that contribute to content popularity.
# It emits (content_id, 1) for each 'like' or 'share' event detected in the input stream.

for line in sys.stdin:
    fields = line.strip().split("\t")
    
    # Ensure the record has the expected number of fields
    if len(fields) != 5:
        continue

    _, _, action_type, content_id, _ = fields
    action_type = action_type.lower()

    # Only track 'like' and 'share' interactions
    if action_type in ["like", "share"]:
        print(f"{content_id}\t1")
