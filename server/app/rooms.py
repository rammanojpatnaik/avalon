"""REST endpoints for creating and joining rooms."""
from __future__ import annotations

import uuid

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.models import Player
from app import store

router = APIRouter(prefix="/rooms", tags=["rooms"])


class CreateRoomRequest(BaseModel):
    name: str = Field(min_length=1, max_length=20)


class JoinRoomRequest(BaseModel):
    name: str = Field(min_length=1, max_length=20)


class PlayerResponse(BaseModel):
    player_id: str
    room_code: str


@router.post("", response_model=PlayerResponse)
def create_room(req: CreateRoomRequest) -> PlayerResponse:
    player_id = str(uuid.uuid4())
    room = store.create_room(host_id=player_id)
    room.players[player_id] = Player(id=player_id, name=req.name)
    return PlayerResponse(player_id=player_id, room_code=room.code)


@router.post("/{code}/join", response_model=PlayerResponse)
def join_room(code: str, req: JoinRoomRequest) -> PlayerResponse:
    room = store.get_room(code)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    if len(room.players) >= 10:
        raise HTTPException(status_code=400, detail="Room is full")

    player_id = str(uuid.uuid4())
    room.players[player_id] = Player(id=player_id, name=req.name)
    return PlayerResponse(player_id=player_id, room_code=room.code)


@router.get("/{code}")
def get_room(code: str) -> dict:
    room = store.get_room(code)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room.public_state()
