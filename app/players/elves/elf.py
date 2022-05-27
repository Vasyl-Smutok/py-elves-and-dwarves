from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str):
        super(Elf, self).__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrument}")