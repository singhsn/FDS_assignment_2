#!/usr/bin/env python3
"""
Mapper Script: User Activity Preprocessing for Join Operation

This script prepares user activity records for a join task.
If a user ID is identified as skewed, it emits multiple salted keys
to distribute load evenly across reducers.

Input:   UserID \t ActionDetails
Output:  UserID(_i if skewed) \t A:ActionDetails
"""

import sys
import os

# Load skewed user IDs from environment variable (if provided)
skewed_keys_str = os.environ.get('skewed.keys', '')
skewed_keys = set(skewed_keys_str.split(',')) if skewed_keys_str else set()

NUM_SALTS = 10  # Number of salted variations to emit for skewed keys

for line in sys.stdin:
    try:
        fields = line.strip().split('\t', 1)
        if len(fields) >= 2:
            user_id = fields[0]
            activity_data = fields[1]

            # Emit multiple salted versions if the key is skewed
            if user_id in skewed_keys:
                for i in range(NUM_SALTS):
                    salted_key = f"{user_id}_{i}"
                    print(f"{salted_key}\tA:{activity_data}")
            else:
                # Emit normally tagged record for non-skewed keys
                print(f"{user_id}\tA:{activity_data}")
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to process line: {line.strip()} | Reason: {str(e)}\n")
