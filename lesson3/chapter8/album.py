def make_album(artist, title, songs=0):
    album = {
        "artist": artist,
        "title": title,
        "songs": songs
    }
    return album

print("---------- Albums ----------")

album1 = make_album("John Smith", "Mixtape 3")
album2 = make_album("PopSinger", "Pop Hits 17", 12)
album3 = make_album("Nickelback", "The Same Songs Again")
album4 = make_album("Play Studios", "Game OST", 15)

print(album1)
print(album2)
print(album3)
print(album4)


print("---- User Album Creator ----")

def prompt(item):
    print(f"Please enter the album's {item}:")
    print("(You may enter 'q' at any time to quit")
    return input("> ").strip()

albums = []

while True:
    user_artist = prompt("artist")
    if user_artist == "q":
        break
    user_title = prompt("title")
    if user_title == "q":
        break
    user_tracks = prompt("total tracks")
    if user_tracks == "q":
        break
    
    user_album = make_album(user_artist, user_title, user_tracks)
    print(user_album)
    albums.append(user_album)
    print("\n")

print(f"You created {len(albums)} albums.")
for album in albums:
    print(album)
