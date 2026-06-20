"""Avalon game server — FastAPI entrypoint."""
from typing import Annotated

from fastapi import Cookie, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from app.store import create_player, get_player_from_cookie
from app.types import Cookies, Player
from app.utils import generate_random_string

app = FastAPI(title="Avalon", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/sign_up")
def sign_up(response: Response):
    session_cookie = generate_random_string()
    player = create_player(session_cookie)
    response.set_cookie(key="session_cookie", value=session_cookie)
    return None

@app.get("/player")
def get_player(cookies: Annotated[Cookies, Cookie()]) -> Player:
    player = get_player_from_cookie(cookies.session_cookie)
    return player
