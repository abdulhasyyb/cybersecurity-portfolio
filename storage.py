# storage.py

# storage.py

import json

def save_data(data, filename="output.json"):
    """Append extracted data to a JSON file."""
    if not data:
        return

    try:
        with open(filename, "a", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
            f.write("\n")  # newline-delimited JSON
        print(f"Saved: {data.get('url', 'unknown')}")
    except Exception as e:
        print(f"Failed to save data: {e}")

