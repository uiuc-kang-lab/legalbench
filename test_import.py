#!/usr/bin/env python3

try:
    from legalbench import TASKS, ISSUE_TASKS
    print("Import successful!")
    print(f"Found {len(TASKS)} tasks and {len(ISSUE_TASKS)} issue tasks")
except Exception as e:
    print(f"Import failed: {e}") 