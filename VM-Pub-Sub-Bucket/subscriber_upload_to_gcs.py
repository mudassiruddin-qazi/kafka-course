import json
from google.cloud import pubsub_v1, storage

project_id = "lustrous-drake-412814"
subscription_id = "semi-sub"
bucket_name = "semi-structure-bucket-1751779155"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)

def callback(message):
    try:
        data = json.loads(message.data.decode("utf-8"))
        file_name = data["file_name"]
        file_path = data["file_path"]

        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_path)

        print(f"📤 Uploaded '{file_name}' from '{file_path}' to bucket '{bucket_name}'")
        message.ack()
    except Exception as e:
        print(f"❌ Error: {e}")
        message.nack()

print(f"👂 Listening for messages on {subscription_path}...")
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
streaming_pull_future.result()
