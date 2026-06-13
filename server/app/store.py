"""Simple in-memory room store.

Swap this out for Redis or a database when you need rooms to survive a
restart or run across multiple server processes.
"""
from __future__ import annotations

import random
import string

from app.models import Room

_rooms: dict[str, Room] = {}


def _generate_code() -> str:
    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=4))
        if code not in _rooms:
            return code


def create_room(host_id: str) -> Room:
    room = Room(code=_generate_code(), host_id=host_id)
    _rooms[room.code] = room
    return room


def get_room(code: str) -> Room | None:
    return _rooms.get(code.upper())


def delete_room(code: str) -> None:
    _rooms.pop(code.upper(), None)
