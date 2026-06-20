from app.types import Player

player_store: dict[int, Player] = {}
session_to_player: dict[str, int] = {}

def create_player(session_cookie: str) -> Player:
    player_id = len(player_store) + 1
    new_player = Player(id = player_id, name = f"Anon{player_id}")
    player_store[player_id] = new_player
    session_to_player[session_cookie] = player_id
    return new_player

def get_player_from_cookie(session_cookie: str) -> Player:
    player_id = session_to_player[session_cookie]
    return player_store[player_id]
