from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'food_delivery_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def is_valid(order):
    # Валидация: цена должна быть положительной
    return order.get('total_price', 0) > 0

print("Consumer ожидает сообщения...")

for message in consumer:
    order = message.value
    if is_valid(order):
        print(f"ПОЛУЧЕНО (VALID): {order}")
    else:
        print(f"NOT VALID: {order}")
