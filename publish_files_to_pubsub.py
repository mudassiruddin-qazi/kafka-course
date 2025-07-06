import os
import json
from google.cloud import pubsub_v1

project_id = "lustrous-drake-412814"
topic_id = "semi-structured-topic"
folder_path = "/data/semi-structure"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        message = {
            "file_name": file_name,
            "file_path": file_path
        }
        future = publisher.publish(topic_path, json.dumps(message).encode("utf-8"))
        print(f"✅ Published {file_name} | Message ID: {future.result()}")
