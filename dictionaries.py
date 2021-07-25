fruit = {"orange":"a sweet orange citrus fruit",
         "apple":"good for making cider",
         "lemon":"a sour yellow citrus fruit",
         "grape":"a small sweet fruit growing in brunches",
         "lime":"a sour green citrus fruit",
        "banana":"long yellow tasty things"}
print(fruit)

#ordered_keys = list(fruit.keys())
#ordered_keys.sort()
#ordered_keys = sorted(list(fruit.keys()))
#for f in ordered_keys:
#    print(f + "_" + fruit[f])
#for f in sorted(fruit.key(())):
#for f in fruit:
#    print(f + "_" + fruit[f])
#
#for val in fruit.values():
#    print(val)
#
#print("__"*50)
#
#for key in fruit:
#    print(fruit[key])

#fruit_keys =fruit.keys()
#print(fruit_keys)
#
#fruit["tomato"] = "not good with ice cream "
#print(fruit_keys)

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snacks in f_tuple:
    item, description = snacks
    print(item + " is " + description)

print(dict(f_tuple))