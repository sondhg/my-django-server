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
            current_time = datetime.now().isoformat()
            
            # Create data for each AGV
            agvs_array_data = []
            for car_id in [1, 2]:  # Only two AGVs
                data = {
                    "car_id": car_id,
                    "agv_state": random.choice([0, 1, 2]),
                    "agv_speed": round(random.uniform(0, 15), 2),
                    "agv_battery": round(random.uniform(20, 100), 2),
                    "previous_waypoint": random.randint(1, 20),
                    "next_waypoint": random.randint(21, 40),
                    "time_stamp": current_time,
                    "distance_sum": round(random.uniform(0, 500), 2),
                    "distance": round(random.uniform(0, 50), 2),
                }
                agvs_array_data.append(data)

            # Send data for both AGVs in one message
            await self.send(json.dumps({
                "agvs_array_data": agvs_array_data
            }))
            await asyncio.sleep(1)  # Adjust the sleep time as needed for updates
