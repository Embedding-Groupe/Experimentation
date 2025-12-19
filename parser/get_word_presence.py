import json
import sys
import os
from collections import Counter

def main(target_file=None):
    if target_file is None:
        if len(sys.argv) > 1:
            target_file = sys.argv[1]
        else:
            target_file = "test.json"

    if not os.path.exists(target_file):
        print(f"File {target_file} not found.")
        return

    try:
        with open(target_file, "r", encoding="utf8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {target_file}")
        return

    if not isinstance(data, list):
        print("Expected JSON content to be a list.")
        return

    # Count frequencies
    counter = Counter(data)

    # Convert to dictionary for JSON output
    # We can just use the dict(counter) or keep the sorted order if we want to be fancy, 
    # but standard JSON dicts are unordered (though Python 3.7+ preserves insertion order).
    # Let's sort it by frequency for readability in the file.
    sorted_counts = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    result_dict = {word: count for word, count in sorted_counts}

    # Overwrite the file with the dictionary
    with open(target_file, "w", encoding="utf8") as f:
        json.dump(result_dict, f, indent=4, ensure_ascii=False)

    print(f"Successfully wrote word frequencies to {target_file}")

if __name__ == "__main__":
    main()
