import random

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

fruits = ["Orange", "Apple", "Banana"] 
fruits[2] = "bannana"
fruits.insert(0, "Watermelon")
fruits.append("Pineapple")
fruits.extend(["Strawberry", "Blueberry"])
print(fruits)

Mustapha = ["Akinola" , "Titilope" , "Babajide", "Olasubomi"]
Mustapha.insert(4, "Abimbola")
Mustapha.extend(["Omobolanle"])
print(Mustapha)
