#!/usr/bin/env python3
"""
Mapper Script: User Profile Preprocessing for Join Operation

This script processes user profile records and prepares them for
a join operation by tagging and salting skewed keys.

Input:   UserID,Name,Location \t AdditionalProfileInfo
Output:  UserID(_i if skewed) \t P:FullProfileData
"""

import sys
import os

# Load skewed keys from environment, if defined
skewed_keys_str = os.environ.get('skewed.keys', '')
skewed_keys = set(skewed_keys_str.split(',')) if skewed_keys_str else set()

NUM_SALTS = 10  # Number of variants to emit for skewed keys

for line in sys.stdin:
    try:
        fields = line.strip().split('\t', 1)
        if len(fields) >= 1:
            user_id_parts = fields[0].split(',')
            user_id = user_id_parts[0]  # Assume user_id is the first value

            # Reconstruct the full profile data
            profile_data = fields[0]
            if len(fields) > 1:
                profile_data += "\t" + fields[1]

            # Emit salted keys if the user_id is skewed
            if user_id in skewed_keys:
                for i in range(NUM_SALTS):
                    salted_key = f"{user_id}_{i}"
                    print(f"{salted_key}\tP:{profile_data}")
            else:
                print(f"{user_id}\tP:{profile_data}")
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to parse line: {line.strip()} | Reason: {str(e)}\n")
