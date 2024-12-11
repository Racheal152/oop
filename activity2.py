class Guitar:
    def play(self):
        return "Strumming the guitar "

class Piano:
    def play(self):
        return "Playing the piano "

class Drums:
    def play(self):
        return "Beating the drums "

instruments = [Guitar(), Piano(), Drums()]
for instrument in instruments:
    print(instrument.play())