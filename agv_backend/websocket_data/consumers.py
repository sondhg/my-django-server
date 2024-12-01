import asyncio
import json
import random
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer


class WebSocketDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_sending = True
        asyncio.create_task(self.send_dummy_data())

    async def disconnect(self, close_code):
        self.keep_sending = False

    async def send_dummy_data(self):
        while self.keep_sending:
            data = {
                "data_id": random.randint(1, 100000),
                "car_id": random.randint(1, 10),
                "agv_state": random.choice([0, 1, 2]),
                "agv_speed": round(random.uniform(0, 15), 2),
                "agv_battery": round(random.uniform(20, 100), 2),
                "previous_waypoint": random.randint(1, 20),
                "next_waypoint": random.randint(21, 40),
                "time_stamp": datetime.now().isoformat(),
                "distance_sum": round(random.uniform(0, 500), 2),
                "distance": round(random.uniform(0, 50), 2),
            }
            await self.send(json.dumps(data))
            await asyncio.sleep(1)
