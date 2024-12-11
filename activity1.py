class Music:
    def __init__(self, genre, artist, song):
        self.genre = genre          
        self.artist = artist        
        self.__song = song          

    def play(self):
        return f"Now playing: '{self.__song}' by {self.artist}, Genre: {self.genre}."

    def reveal_song(self):
        return f"The song currently playing is '{self.__song}'."

    def set_song(self, new_song):
        self.__song = new_song

class Playlist(Music):
    def __init__(self, genre, artist, song, playlist_name):
        super().__init__(genre, artist, song)  
        self.playlist_name = playlist_name

    def play(self):
        return f"Playing from playlist '{self.playlist_name}': '{self.__song}' by {self.artist}."


track = Music("Rock", "Queen", "Bohemian Rhapsody")
playlist = Playlist("Pop", "Taylor Swift", "Shake It Off", "Party Mix")


print(track.play())
print(track.reveal_song())
track.set_song("Don't Stop Me Now")
print(track.play())

print(playlist.play())
