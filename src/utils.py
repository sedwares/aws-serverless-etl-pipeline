import json
from pathlib import Path
from typing import List, Dict


DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_events(filename: str = "sample_events.json") -> List[Dict]:
    """Load JSON events from the data folder."""
    path = DATA_DIR / filename
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data, filename: str):
    """Save JSON to the data folder (used to simulate S3 output)."""
    path = DATA_DIR / filename
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


