locations = {0:"your sitting in front of a coumputer learning python",
             1:"you standing at the end of a road before a small brice building",
             2:"your at the top of a hill",
             3:"yopur inside a building , well house for small stream ",
             4:"your in a vally beside a stream",
             5:"you are in the forest"}

exits = [{"Q":0},
         {"W":2,"E":3,"N":5,"S":4,"Q":0},
         {"N":5,"Q":0},
         {"W":1,"Q":0},
         {"N":1,"W":2,"Q":0},
         {"W":2,"S":1,"Q":0}]

loc = 1
while True:
    avaliableExits = " , ".join(exits[loc].keys())

    print(locations[loc])

    if loc  ==0:
        break

    direction = input("avilable exits are " + avaliableExits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("you can not go i that direction")