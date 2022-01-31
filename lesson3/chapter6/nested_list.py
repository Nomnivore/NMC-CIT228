player = {
    "name": "kyle",
    "fav_color": "blue",
    "platforms": ["pc", "switch", "android"],
    "games": ["overwatch", "valorant", "hades", "ffxiv"]
}

for key, value in player.items():
    if type(value) == list:
        print(f"Your {key} are:")
        for item in value:
            print(f"\t{item}")
    else:
        print(f"Your {key} is {value}.")
