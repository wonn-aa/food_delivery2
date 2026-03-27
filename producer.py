from kafka import KafkaProducer
import json
import time
from generator import FoodDeliveryGenerator

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8')
)

TOPIC = 'food_delivery_topic'
print(f"Producer запущен. Отправка в топик: {TOPIC}")

try:
    while True:
        data = FoodDeliveryGenerator.generate_order()
        print(f"ОТПРАВЛЕНО: {data}")
        producer.send(TOPIC, value=data)
        time.sleep(2)
except KeyboardInterrupt:
    print("Producer остановлен.")
finally:
    producer.close()

