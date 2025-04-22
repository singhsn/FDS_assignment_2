#mapper


import sys

for line in sys.stdin:
    fields = line.strip().split("\t")

    if len(fields) != 5:
        continue  

    user_id = fields[1]      
    action_type = fields[2].lower()

    if action_type in ["post", "like", "comment", "share"]:
        print(f"{user_id}\t{action_type}")


mapper_code = """#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split("\\t")

    if len(fields) != 5:
        continue  # Skip malformed lines

    user_id = fields[1]  # timestamp, user_id, action_type, content_id, metadata
    action_type = fields[2].lower()

    if action_type in ["post", "like", "comment", "share"]:
        print(f"{user_id}\\t{action_type}")
"""

with open("mapper_task2.py", "w") as f:
    f.write(mapper_code)

!chmod +x mapper_task2.py
