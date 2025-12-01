"""
Simulated AWS Lambda function.

In AWS, this would be triggered by an S3 event.
Here, we just read a local JSON file and write a cleaned version.
"""

from typing import Dict, Any, List
from utils import load_events, save_json


REQUIRED_FIELDS = ["event_id", "timestamp", "user_id", "value"]


def is_valid(record: Dict[str, Any]) -> bool:
    """Check that all required fields are present and non-null."""
    for field in REQUIRED_FIELDS:
        if field not in record or record[field] in (None, ""):
            return False
    return True


def handler(event=None, context=None):
    # In AWS, 'event' would contain S3 info.
    # Locally, we just read sample_events.json.
    raw_events = load_events("sample_events.json")
    cleaned = [r for r in raw_events if is_valid(r)]

    print(f"Loaded {len(raw_events)} events, {len(cleaned)} passed validation.")

    # Simulate writing to a "clean" S3 location by saving another file
    save_json(cleaned, "clean_events.json")


if __name__ == "__main__":
    handler()
