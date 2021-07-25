fruit = {"orange":"a sweet orange citrus fruit",
         "apple":"good for making cider",
         "lemon":"a sour yellow citrus fruit",
         "grape":"a small sweet fruit growing in brunches",
         "lime":"a sour green citrus fruit",}
print(fruit)

veg = {"cabbage":"every childs favourite",
       "sprouts":"mmmmmm,lovely",
       "spinach":"can i have some more fruits, please"}
print(veg)

# veg.update(fruit)
# print(veg)
#
# print(fruit.update(veg))
# print(fruit)

nice = fruit.copy()
nice.update(veg)
print(nice)