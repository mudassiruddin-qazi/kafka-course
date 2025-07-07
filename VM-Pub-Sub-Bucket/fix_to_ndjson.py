import json
import os

folder = "/data/semi-structure"

for filename in os.listdir(folder):
    if filename.endswith(".json"):
        full_path = os.path.join(folder, filename)
        with open(full_path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"❌ Skipping {filename}: Invalid JSON")
                continue

        # Only convert arrays
        if isinstance(data, list):
            with open(full_path, "w") as f:
                for item in data:
                    json.dump(item, f)
                    f.write("\n")
            print(f"✅ Converted {filename} to NDJSON")
        else:
            print(f"ℹ️ Skipping {filename}: Already NDJSON or single object")
