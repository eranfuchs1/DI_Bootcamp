class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        print(*self.lyrics, sep="\n")

stairway= Song(["There\u2019s a lady who's sure","all that glitters is gold", "and she\u2019s buying a stairway to heaven"])
stairway.sing_me_a_song()
