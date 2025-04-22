#FDS_Assignment_2

Question 1: MapReduce Workflow for Social Media Analytics — Detailed Breakdown --

Task 1: Parsing and Cleaning Raw Data
Objective: Process entries from social_media_logs.txt, remove corrupted or invalid lines, and produce well-structured output.

Steps:
Mapper (mapper_task1.py)

Split each line using tab delimiters.

Check if the timestamp follows the expected format.

Extract metadata fields from the JSON block.

Keep track of malformed entries using print statements or logging.

Run Environment: Local machine or Google Colab.

Task 2: Aggregating User Actions and Sorting by Posts
Objective: Compute the number of different actions (posts, likes, comments, shares) each user performs, and sort the result by number of posts.

Steps:
Mapper (mapper_task2.py)

Output key-value pairs in the form: (user_id, action_type).

Reducer (reducer_task2.py)

Tally up the occurrences of each action type per user.

Format output like: user_id\tposts:N,likes:N,...

Run Environment: Can be tested via Colab notebooks or local Bash execution.

Task 3: Detecting Trending Content
Objective: Highlight content that’s currently trending, determined by the combined number of likes and shares exceeding a defined threshold.

Steps:
Mapper (mapper_task3.py)

For every like or share, emit a pair with content_id and 1.

Reducer (reducer_task3.py)

Sum up the interactions for each content item.

Output content that exceeds the set threshold (e.g., 50+ total interactions).

Execution: Can be tested in your preferred environment.

Task 4: Merging Activity Logs with User Profiles
Objective: Perform a join operation between user activities (user_actions.txt) and profile data (user_profiles.txt).

Steps:

Remove headers before processing if necessary.

Scripts Involved:

join_profile_mapper.py

join_activity_mapper.py

join_reducer.py

Execution: Run the mappers and reducer in sequence to complete the join.

Task 5: Improving Performance and Ensuring Reliability
Objective: Optimize the MapReduce jobs for efficiency and robustness.

Performance Enhancements:

Utilize combiners to cut down on shuffle data.

Apply optimized structures like defaultdict or Counter for aggregation.

Adjust cluster settings (e.g., heap size, reducer count) for better performance.

Monitoring Tools:

Use Hadoop counters for tracking record validity and throughput.

Monitor memory usage and execution time via logs.

In cloud environments (e.g., GCP), leverage Cloud Monitoring and Logging services.