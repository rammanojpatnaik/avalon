# Avalon

An online multiplayer implementation of **The Resistance: Avalon**, the social deduction game of hidden roles, secret quests, and deception. Built with a **FastAPI** backend and a **React** frontend.

## About the Game

Players are secretly split into two factions — the **Loyal Servants of Arthur** (Good) and the **Minions of Mordred** (Evil). Across five quests, teams are proposed, voted on, and sent on missions:

- **Good** wins by succeeding **three** quests.
- **Evil** wins by sabotaging **three** quests — or by **assassinating Merlin** at the end, even after losing.

Special roles (Merlin, Percival, Morgana, Mordred, Oberon, Assassin) give some players hidden knowledge, turning every game into a battle of bluffs and deduction. Supports **5–10 players**.

## Tech Stack

| Layer    | Technology        |
| -------- | ----------------- |
| Backend  | FastAPI (Python)  |
| Frontend | React             |
| Realtime | WebSockets        |

## Project Structure

```
avalon/
├── server/         # FastAPI app — game logic, rooms, WebSocket endpoints
└── client/         # React app — game UI
```

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+

### Backend

```bash
cd server
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The API runs at `http://localhost:8000`.

### Frontend

```bash
cd client
npm install
npm run dev
```

The app runs at `http://localhost:5173`.

## How to Play

1. Start the backend and frontend.
2. Open the app in your browser and create a game room.
3. Share the room code with 5–10 friends.
4. Get your secret role, propose teams, vote, and run quests.
5. Good completes three quests to win — but watch out for the Assassin.

## License

MIT
