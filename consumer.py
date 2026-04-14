from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'airports_raw',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer iniciado!")

for message in consumer:
    print(message.value)