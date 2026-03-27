import random
from datetime import datetime

class FoodDeliveryGenerator:
    @staticmethod
    def generate_order():
        restaurants = ["Вкусный Уголок", "Пицца Мастер", "Суши Хаус"]
        menu_items = ["Борщ", "Пицца Маргарита", "Сет Роллов", "Кофе"]
        clients = ["Иван Иванов", "Мария Петрова", "Алексей Смирнов"]
        couriers = ["Олег", "Анна", "Игорь"]

        return {
            "order_id": random.randint(1000, 9999),
            "restaurant": random.choice(restaurants),
            "client": random.choice(clients),
            "courier": random.choice(couriers),
            "items": random.sample(menu_items, k=random.randint(1, 2)),
            "total_price": round(random.uniform(-100.0, 3000.0), 2), # Есть отрицательные для валидации
            "timestamp": datetime.now().isoformat()
        }
