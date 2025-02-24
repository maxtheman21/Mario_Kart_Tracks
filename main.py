import sqlite3


# db = sqlite3.connect('Mariokart.db')
# cursor = db.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS Tracks (ID INTEGER PRIMARY KEY AUTOINCREMENT, Username CHAR, Track_Title TEXT, time TEXT)''')
# db.close()
    
def playerStats(username):
    db = sqlite3.connect('Mariokart.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * 
                   FROM Tracks
                   WHERE Username = ?
                   ORDER BY time DESC
                   LIMIT 5
                   ''', (username.name,))
    
    results = cursor.fetchall()
    db.close()
    return results

def addTime(username, track, time): # Grab player's last time (if any) and compare to new time, replace if faster.
    db = sqlite3.connect('Mariokart.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO Tracks (Username, Track_Title, time) VALUES (?, ?, ?)", (username.name, track, time))
    db.commit()
    db.close()
    return True
    
    
    
def leaderboard(track):
    db = sqlite3.connect('Mariokart.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * 
                   FROM Tracks
                   WHERE Track_Title = ?
                   ORDER BY time DESC
                   LIMIT 5
                   ''', (track,))
    
    results = cursor.fetchall()
    db.close()
    return results
    
def translateTrack(track):
    temp0 = []
    temp1 = track.strip().split(" ")
    for i in temp1:
        temp2 = i.strip().split(" ")
        for j in temp2:
            temp3 = list(j)
            for k in range(len(temp3)):
                temp3[k] = temp3[k].lower()
            temp3[0] = temp3[0].upper()
            j = "".join(temp3)
            temp0.append(j)

    track = " ".join(temp0)
    return track

def checkTracks(track):
    tracks = [
        "Amsterdam Drift",
        "Animal Crossing",
        "Athens Dash",
        "Baby Park",
        "Bangkok Rush",
        "Berlin Byways",
        "Big Blue",
        "Bone-Dry Dunes",
        "Boo Lake",
        "Bowser Castle 3 (SNES)",
        "Bowser's Castle (Wii U)",
        "Cheep Cheep Beach"
        "Cheese Land"
        "Choco Mountain"
        "City Tracks",
        "Cloudtop Cruise",
        "Coconut Mall",
        "Daisy Circuit",
        "Daisy Cruiser",
        "DK Jungle",
        "DK Mountain",
        "DK Summit",
        "Dolphin Shoals",
        "Donut Plains 3",
        "Dragon Driftway",
        "Dry Dry Desert",
        "Electrodrome",
        "Excitebike Arena",
        "Grumble Volcano",
        "Hyrule Circuit",
        "Ice Ice Outpost",
        "Kalimari Desert",
        "Koopa Cape",
        "London Loop",
        "Los Angeles Laps",
        "Madrid Drive",
        "Maple Treeway",
        "Mario Circuit",
        "Mario Circuit (DS)",
        "Mario Circuit (GBA)",
        "Mario Circuit (Wii U)",
        "Mario Circuit 3",
        "Mario Kart Stadium",
        "Merry Mountain",
        "Moo Moo Meadows",
        "Moonview Highway",
        "Mount Wario",
        "Mushroom Gorge",
        "Music Park",
        "Mute City",
        "Neo Bowser City",
        "New York Minute",
        "Ninja Hideaway",
        "Paris Promenade",
        "Peach Gardens",
        "Piranha Plant Cove",
        "Piranha Plant Slide",
        "Rainbow Road (3DS)",
        "Rainbow Road (N64)",
        "Rainbow Road (SNES)",
        "Rainbow Road (Wii U)",
        "Rainbow Road (Wii)",
        "Ribbon Road",
        "Riverside Park",
        "Rock Rock Mountain",
        "Rome Avanti",
        "Rosalina's Ice World",
        "Royal Raceway",
        "Sherbet Land (GCN)",
        "Shroom Ridge",
        "Shy Guy Falls",
        "Singapore Speedway",
        "Sky Garden",
        "Sky-High Sundae",
        "Snow Land",
        "Squeaky Clean Sprint",
        "Sunset Wilds",
        "Sunshine Airport",
        "Super Bell Subway",
        "Sweet Sweet Canyon",
        "Sydney Sprint",
        "Thwomp Ruins",
        "Tick-Tock Clock",
        "Toad Circuit",
        "Toad Harbor",
        "Toad's Turnpike",
        "Tokyo Blur",
        "Twisted Mansion",
        "Vancouver Velocity",
        "Waluigi Pinball",
        "Waluigi Stadium (GCN)",
        "Wario Stadium (DS)",
        "Wario's Gold Mine",
        "Water Park",
        "Wild Woods",
        "Yoshi Circuit",
        "Yoshi Valley",
        "Yoshi's Island"]
    if track in tracks:
        return True
    return False    

