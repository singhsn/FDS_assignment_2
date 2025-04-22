# reducer


import sys


current_content = None
total = 0
THRESHOLD = 100  

for line in sys.stdin:
    line = line.strip()
    content_id, count = line.split("\t")
    count = int(count)

    if current_content and content_id != current_content:
        if total >= THRESHOLD:
            print(f"{current_content}\t{total}\tTRENDING")
        else:
            print(f"{current_content}\t{total}")
        total = 0

    current_content = content_id
    total += count

if current_content:
    if total >= THRESHOLD:
        print(f"{current_content}\t{total}\tTRENDING")
    else:
        print(f"{current_content}\t{total}")

with open("reducer_task3.py", "w") as f:
    f.write("""#!/usr/bin/env python3
import sys

# Reducer: Aggregates counts per content_id and marks TRENDING if >= threshold
current_content = None
total = 0
THRESHOLD = 100  # You can adjust this threshold based on stats

for line in sys.stdin:
    line = line.strip()
    content_id, count = line.split("\\t")
    count = int(count)

    if current_content and content_id != current_content:
        if total >= THRESHOLD:
            print(f"{current_content}\\t{total}\\tTRENDING")
        else:
            print(f"{current_content}\\t{total}")
        total = 0

    current_content = content_id
    total += count

if current_content:
    if total >= THRESHOLD:
        print(f"{current_content}\\t{total}\\tTRENDING")
    else:
        print(f"{current_content}\\t{total}")
""")

!cat social_media_logs.txt | python3 mapper_task3.py | sort | python3 reducer_task3.py > trending_output.txt
