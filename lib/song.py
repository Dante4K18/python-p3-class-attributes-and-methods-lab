class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the song count
        Song.add_song_to_count()
        
        # Add genre and artist to their respective lists
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # Increment the genre and artist count
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)        # "99 Problems"
print(ninety_nine_problems.artist)      # "Jay-Z"
print(ninety_nine_problems.genre)       # "Rap"
print(Song.count)                        # 1
print(Song.genres)                       # ["Rap"]
print(Song.artists)                      # ["Jay-Z"]
print(Song.genre_count)                  # {"Rap": 1}
print(Song.artist_count)                 # {"Jay-Z": 1}

# Adding more songs
song2 = Song("Lose Yourself", "Eminem", "Rap")
song3 = Song("Bohemian Rhapsody", "Queen", "Rock")
song4 = Song("Take Me Home, Country Roads", "John Denver", "Country")

print(Song.count)                        # 4
print(Song.genres)                       # ["Rap", "Rock", "Country"]
print(Song.artists)                      # ["Jay-Z", "Eminem", "Queen", "John Denver"]
print(Song.genre_count)                  # {"Rap": 2, "Rock": 1, "Country": 1}
print(Song.artist_count)                 # {"Jay-Z": 1, "Eminem": 1, "Queen": 1, "John Denver": 1}
