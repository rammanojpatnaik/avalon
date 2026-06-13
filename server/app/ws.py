"""WebSocket endpoint for real-time room updates."""
from __future__ import annotations

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app import store

router = APIRouter()


class ConnectionManager:
    """Tracks active WebSocket connections per room code."""

    def __init__(self) -> None:
        self._connections: dict[str, set[WebSocket]] = {}

    async def connect(self, code: str, ws: WebSocket) -> None:
        await ws.accept()
        self._connections.setdefault(code, set()).add(ws)

    def disconnect(self, code: str, ws: WebSocket) -> None:
        conns = self._connections.get(code)
        if conns:
            conns.discard(ws)
            if not conns:
                self._connections.pop(code, None)

    async def broadcast(self, code: str, message: dict) -> None:
        for ws in list(self._connections.get(code, set())):
            await ws.send_json(message)


manager = ConnectionManager()


@router.websocket("/ws/{code}")
async def room_socket(websocket: WebSocket, code: str) -> None:
    room = store.get_room(code)
    if room is None:
        await websocket.close(code=4004)
        return

    await manager.connect(room.code, websocket)
    await manager.broadcast(room.code, {"type": "state", "data": room.public_state()})

    try:
        while True:
            # Echo client messages back to the room for now; replace with
            # real game-action handling (propose team, vote, quest, etc.).
            payload = await websocket.receive_json()
            await manager.broadcast(room.code, {"type": "message", "data": payload})
    except WebSocketDisconnect:
        manager.disconnect(room.code, websocket)
        await manager.broadcast(room.code, {"type": "state", "data": room.public_state()})
