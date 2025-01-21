from kafka import KafkaProducer
import json
import time


# Kafka configuration
TOPIC = 'olympics_data'
BROKER = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Sending datasets to Kafka topic
for dataset in datasets:
    producer.send(TOPIC, dataset)
    print(f"Sent dataset: {dataset['dataset']}")
    time.sleep(2)

producer.close()