games = {
    "hades": {
        "platform": "pc",
        "genre": "roguelite",
        "multiplayer": False
    },
    "overwatch": {
        "platform": "pc",
        "genre": "first person shooter",
        "multiplayer": True
    },
    "diablo": {
        "platform": "switch",
        "genre": "action rpg",
        "multiplayer": True
    }
}

for game, data in games.items():
    print(f"Game: {game}")
    for key, value in data.items():
        print(f"    {key}: {value}")
    print("\n")
