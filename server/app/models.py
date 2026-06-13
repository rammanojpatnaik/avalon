"""In-memory game models for Avalon."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Phase(str, Enum):
    LOBBY = "lobby"
    TEAM_BUILDING = "team_building"
    VOTING = "voting"
    QUEST = "quest"
    ASSASSINATION = "assassination"
    FINISHED = "finished"


@dataclass
class Player:
    id: str
    name: str
    role: str | None = None  # assigned when the game starts


@dataclass
class Room:
    code: str
    host_id: str
    players: dict[str, Player] = field(default_factory=dict)
    phase: Phase = Phase.LOBBY

    def public_state(self) -> dict:
        """State safe to broadcast to everyone (no secret roles)."""
        return {
            "code": self.code,
            "host_id": self.host_id,
            "phase": self.phase,
            "players": [{"id": p.id, "name": p.name} for p in self.players.values()],
        }
