import math

width = 1
height = 2

Capacity = (math.pi) * ((width/2) * (width/2)) * height

print("Tilps tiek litru:",Capacity)

AmountOfLiquid = 50

AmountOfContainers = math.ceil(AmountOfLiquid / Capacity)

print("Reikes tiek indu:",AmountOfContainers)