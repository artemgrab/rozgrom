from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ws_logic.manager import manager

ws_router = APIRouter()


@ws_router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(user_id, websocket)
    try:
        while True:
            # Receive as JSON
            data = await websocket.receive_json()

            # Extract text safely
            message_text = data.get("text", "")

            response = {
                "sender_id": user_id,
                "text": message_text,
                "timestamp": "19:55",  # Placeholder
            }

            await manager.broadcast_json(response)
    except WebSocketDisconnect:
        manager.disconnect(user_id)
