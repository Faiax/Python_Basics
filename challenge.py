locations = {0:"your sitting in front of a coumputer learning python",
             1:"you standing at the end of a road before a small brice building",
             2:"your at the top of a hill",
             3:"your inside a building , well house for small stream ",
             4:"your in a vally beside a stream",
             5:"you are in the forest"}

exits = {0: {"Q":0},
         1: {"W":2, "2":2, "E":3, "3":3,"N":5, "5":5 , "S":4, "4": 4, "Q":0},
         2: {"N":5, "5":5, "Q":0},
         3: {"W":1, "1":1, "Q":0},
         4: {"N":1, "1":1 ,"W":2,"2":2,"Q":0},
         5: {"W":2, "2":2 ,"S":1,"1":1,"Q":0}}

vocabulary = {"QUIT":"Q",
              "NORTH": "N",
              "SOUTH":"S",
              "EAST":"E",
              "WEST":"W",
              "ROAD":"1",
              "HILL":"2",
              "BUILDING":"3",
              "VALLY":"4",
              "FOREST":"5"}

loc = 1
while True:
    avaliableExits = " , ".join(exits[loc].keys())

    print(locations[loc])

    if loc  ==0:
        break

    direction = input("avilable exits are " + avaliableExits + " ").upper()
    print()
    if len(direction) > 1:
        words = direction.spliit()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[words]
                break