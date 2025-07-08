import csv
import os
import random
import string
from datetime import datetime, timedelta

# Output directory and file
output_dir = "/data/structure"
output_file = os.path.join(output_dir, "structured_data_1GB.csv")
total_rows = 10_000_000  # ~1GB if each row is ~100 bytes

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Random data generators
def random_name(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_email(name):
    domains = ["example.com", "test.org", "demo.net"]
    return f"{name.lower()}@{random.choice(domains)}"

def random_date(start_year=2000, end_year=2025):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

# Write CSV
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "email", "age", "created_at"])  # Header

    for i in range(1, total_rows + 1):
        name = random_name()
        email = random_email(name)
        age = random.randint(18, 70)
        created_at = random_date()
        writer.writerow([i, name, email, age, created_at])

        if i % 100000 == 0:
            print(f"Generated {i} rows...")

print(f"\n✅ Done! Generated file at: {output_file}")
