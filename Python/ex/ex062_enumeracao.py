import enum

#Directions = enum.Enum('Directions', ['RIGHT', 'LEFT']) voce pode criar desta maneira
#porem prejudica a typagem do programa

class Directions(enum.Enum):
    RIGHT = 0 #voce pode enumerar manualmente ouuuuu
    LEFT = enum.auto() #usar o enum.auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Direction not found')

    print(f'Moving for {direction.name} ')

move(Directions.LEFT)

print(Directions(1), Directions['RIGHT'], Directions.RIGHT) #por membro...
print(Directions(1).name) #por chave
print(Directions(0).value) #por valor