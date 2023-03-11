def start_playing(asd):
    return asd.play()


class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))