"""
Reducer Script: Merging User Activities with Profile Information

"""

import sys

current_user = None
profile_data = None
activity_data = None

# Read and process each input line from stdin
for line in sys.stdin:
    try:
        # Separate user ID and tagged content
        user_id, tagged_info = line.strip().split('\t', 1)

        # Remove skew-handling suffix from user ID, if any
        if '_' in user_id:
            user_id = user_id.split('_')[0]

        # If a new user is encountered, process the accumulated data
        if user_id != current_user:
            if current_user is not None and profile_data and activity_data:
                print(f"{current_user}\t{profile_data}\t{activity_data}")

            # Reset values for the new user
            current_user = user_id
            profile_data = None
            activity_data = None

        # Identify tag and strip data
        tag = tagged_info[0]
        content = tagged_info[2:]

        if tag == 'P':
            profile_data = content
        elif tag == 'A':
            activity_data = content

    except Exception as e:
        # Log issues but continue processing
        sys.stderr.write(f"[ERROR] Line skipped: {line.strip()} | Reason: {str(e)}\n")

# Output for the last user (if valid)
if current_user and profile_data and activity_data:
    print(f"{current_user}\t{profile_data}\t{activity_data}")
