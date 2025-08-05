import os
import csv
import random
import uuid
from faker import Faker
from datetime import datetime
from pathlib import Path

# Constants
TARGET_DIR = "/data/sale-data"
FILE_SIZE_MB = 10
TOTAL_SIZE_MB = 1024  # 1 GB
BYTES_IN_MB = 1024 * 1024
RECORDS_BATCH_SIZE = 1000

# Product catalog
PRODUCTS = [
    ("P001", "Smartphone"), ("P002", "Laptop"), ("P003", "Headphones"), ("P004", "Smartwatch"),
    ("P005", "Bluetooth Speaker"), ("P006", "Tablet"), ("P007", "Wireless Charger"), ("P008", "DSLR Camera"),
    ("P009", "Gaming Console"), ("P010", "Monitor"), ("P011", "Keyboard"), ("P012", "Mouse"),
    ("P013", "Power Bank"), ("P014", "Smart TV"), ("P015", "Router"), ("P016", "Drone"),
    ("P017", "Fitness Tracker"), ("P018", "Portable SSD"), ("P019", "VR Headset"), ("P020", "Graphics Card"),
    ("P021", "External HDD"), ("P022", "Webcam"), ("P023", "Projector"), ("P024", "Microphone"),
    ("P025", "Smart Bulb"), ("P026", "Thermostat"), ("P027", "E-Reader"), ("P028", "Smart Plug"),
    ("P029", "Car Dashcam"), ("P030", "Wi-Fi Extender"), ("P031", "Coffee Machine"), ("P032", "Air Purifier"),
    ("P033", "Hair Dryer"), ("P034", "Electric Toothbrush"), ("P035", "Robot Vacuum"), ("P036", "Blender"),
    ("P037", "Microwave Oven"), ("P038", "Refrigerator"), ("P039", "Washing Machine"), ("P040", "Air Conditioner"),
    ("P041", "Heater"), ("P042", "Water Purifier"), ("P043", "Juicer"), ("P044", "Grinder"),
    ("P045", "Electric Kettle"), ("P046", "Induction Cooktop"), ("P047", "Oven Toaster"), ("P048", "Mixer"),
    ("P049", "Rice Cooker"), ("P050", "Sandwich Maker")
]

fake = Faker()
Faker.seed(0)
random.seed(0)

# Ensure output directory exists
Path(TARGET_DIR).mkdir(parents=True, exist_ok=True)

def generate_record():
    product = random.choice(PRODUCTS)
    location = fake.city()
    timestamp = datetime.now().isoformat()
    name = fake.name()
    email = fake.email()
    mobile = fake.phone_number()
    mac = fake.mac_address()
    return [product[0], product[1], location, timestamp, name, email, mobile, mac]

def get_file_path(index):
    return os.path.join(TARGET_DIR, f"sales_data_{index}.csv")

def main():
    file_index = 1
    total_written_bytes = 0

    while total_written_bytes < TOTAL_SIZE_MB * BYTES_IN_MB:
        file_path = get_file_path(file_index)
        with open(file_path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ProductID", "ProductName", "Location", "Timestamp", "CustomerName", "Email", "Mobile", "MAC"])

            while csvfile.tell() < FILE_SIZE_MB * BYTES_IN_MB:
                for _ in range(RECORDS_BATCH_SIZE):
                    writer.writerow(generate_record())
                csvfile.flush()

        file_size = os.path.getsize(file_path)
        total_written_bytes += file_size
        print(f"[+] Created {file_path} - {file_size / BYTES_IN_MB:.2f} MB")
        file_index += 1

    print(f"[✓] Done generating {file_index-1} files totaling ~{total_written_bytes / BYTES_IN_MB:.2f} MB")

if __name__ == "__main__":
    main()
