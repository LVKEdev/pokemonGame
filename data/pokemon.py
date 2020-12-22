import csv

class Pokemon:
  def __init__(self, row):
    self.name = row[0]
    self.type = row[1]
    self.hp = row[2]
    self.attack = row[3]
    self.defence = row[4]
    self.spAttack = row[5]
    self.spDefence = row[6]
    self.speed = row[7]
    self.move1 = row[8]
    self.move2 = row[9]
    self.move3 = row[10]
    self.move4 = row[11]
    self.display1 = row[12]
    self.display2 = row[13]
    self.display3 = row[14]
    self.reverse1 = row[15]
    self.reverse2 = row[16]
    self.reverse3 = row[17]

with open("pokemon.csv") as fp:
  reader = csv.reader(fp, delimiter=",", quotechar='`')
  # next(reader, None)  # if we want to skip the header row
  pokemon_data = [row for row in reader]
  print(pokemon_data)
  pokeList = [Pokemon(pokemon_data[i]) for i in range(1, len(pokemon_data))]
  print(pokeList[0].name, pokeList[0].type)

