from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}

    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: int):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def send_personal_message(self, message: str, user_id: int):
        # Sending personal message to user identifying them by their ID
        if user_id in self.active_connections:
            await self.active_connections[user_id].send_text(message)

    async def broadcast_json(self, message: dict):
        for connection in self.active_connections.values():
            await connection.send_json(message)


# Creating a single instance of manager, which we will use everywhere
manager = ConnectionManager()
