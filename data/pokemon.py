import os
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

class Reader:
  def __init__(self):
    self.sources = []
  
  def addSource(self, name, file):
    source = Data(name).load(file)
    self.sources.append(source)

  def selectPokemon(self):
    self.sources.index
    print('Select a pokemon')
    # drop off point -- continue here

class Data:
  def __init__(self, name):
    self.name = name

  def load(self, file):
    with open(file) as f:
      content = csv.reader(f, delimiter=",", quotechar="`")
      self.data = [row for row in content]
      self.columns = self.data[0]
      self.rows = self.data[1:]
      return self
      
  def vals(self):
    self.byKey = [{"name":row[0], "data":row[1:]} for row in self.rows]
    return self

def main():
  reader = Reader()
  reader.addSource('pokemon', 'pokemon.csv')
  pokemon = reader.sources[0].vals().byKey
  print([pokemon[i]['name'] for i in range(0, len(pokemon))])
  # also continue here
  
main()