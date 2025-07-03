#!/bin/bash

# Define directory and size limit
TARGET_DIR="/data/semi-structure"
TARGET_SIZE_MB=1024  # 1 GB = 1024 MB
FILE_PREFIX="student_data"
FILE_INDEX=1

# Create directory
mkdir -p "$TARGET_DIR"

# Python inline script to generate ~10MB JSON file
generate_json() {
  python3 - <<EOF
import json, random, uuid

records = []
for _ in range(50000):  # ~10MB of data per file
    record = {
        "id": str(uuid.uuid4()),
        "name": random.choice(["Ayaan", "Mirha", "Zoya", "Armaan", "Kabir"]),
        "age": random.randint(5, 15),
        "class": random.choice(["1st", "2nd", "3rd", "4th", "5th"]),
        "score": {
            "math": random.randint(30, 100),
            "science": random.randint(30, 100),
            "english": random.randint(30, 100)
        },
        "address": {
            "city": random.choice(["Delhi", "Mumbai", "Pune", "Hyderabad"]),
            "pincode": random.randint(100000, 999999)
        }
    }
    records.append(record)

with open("$TARGET_DIR/${FILE_PREFIX}_${FILE_INDEX}.json", "w") as f:
    json.dump(records, f)
EOF
}

# Keep generating files until ~1GB reached
echo "Generating 1GB of semi-structured data in $TARGET_DIR..."
while true; do
    generate_json
    FILE_INDEX=$((FILE_INDEX+1))

    CURRENT_SIZE_MB=$(du -sm "$TARGET_DIR" | cut -f1)
    echo "Current size: ${CURRENT_SIZE_MB} MB"
    if [ "$CURRENT_SIZE_MB" -ge "$TARGET_SIZE_MB" ]; then
        echo "✅ 1GB data generation complete."
        break
    fi
done
