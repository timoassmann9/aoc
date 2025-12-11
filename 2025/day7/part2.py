class Start:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return "Start"
    
    def __repr__(self) -> str:
        return "Start"

class Space:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "Space"
    
    def __repr__(self) -> str:
        return "Space"

class Splitter:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.went_left = False
        self.went_right = False

    def __str__(self) -> str:
        return "Splitter"
    
    def __repr__(self) -> str:
        return "Splitter"

class TachyonParticle:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.path: list[Splitter] = list()

    def __str__(self) -> str:
        return "TachyonParticle"
    
    def __repr__(self) -> str:
        return "TachyonParticle"

    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def jump(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":

    with open("input.txt") as f:
        data = f.read()

    # vorher alle splitter locations speichern
    # Starte bei S
    #   gehe 1 nach unten, bis du auf einen splitter triffst oder das ende erreichst
    #   wenn du auf einen splitter triffst, nimm ihn in deinen Pfad auf
    #       gehe links
    #   wenn ende, timeline + 1
    #   gehe zum vorherigen splitter
    #   wenn rechts noch frei ist, gehe rechts
    #   wenn keiner mehr frei ist, gehe zum vorherigen splitter und lösche den letzten aus dem Pfad
    #   repeat
    data = data.split()

    timelines = 0
    map = list()

    for i in reversed(range(len(data))):
        line = list()
        for j in range(len(data[i])):
            char = data[i][j]
            if char == "S":
                line.append(Start(j, len(data) - i - 1))
            elif char == ".":
                line.append(Space(j, len(data) - i - 1))
            elif char == "^":
                line.append(Splitter(j, len(data) - i - 1))
        map.append(line)

    for obj in map[-1]:
        if isinstance(obj, Start):
            particle = TachyonParticle(obj.x, obj.y)
            print(f"particle erstellt bei {particle.x}, {particle.y}")
            break

    while particle.y > 0:
        print("hier rein")
        print(particle.x, particle.y)
        current_obj = map[particle.y][particle.x]
        while not isinstance(current_obj, Splitter) and particle.y > 0:
            particle.move_down()
            current_obj = map[particle.y][particle.x]
        if isinstance(current_obj, Splitter):
            print(f"Splitter bei {particle.x}, {particle.y}")
            particle.path.append(current_obj)
            particle.move_left()
            current_obj.went_left = True

    latest_splitter = particle.path[-1]
    while not latest_splitter.went_right:
        particle.jump(latest_splitter.x, latest_splitter.y)
        particle.move_right()
        latest_splitter.went_right = True
        

    for obj in particle.path:
        print(obj.x, obj.y, obj.went_left, obj.went_right)
    timelines += 1

    # for i in reversed(range(len(map))):
    #     print(map[i])

    print(timelines)