from homeworks.distance import Distance

d1 = Distance(230, "cm")
d2 = Distance(3.3, "m")
d3 = Distance(1.1, "km")

print("пример:")
print(d1)
print(d2)
print(d3)

print("\nСложение:")
print(d1 + d2)
print(d2 + d3)

print("\nВычитание:")
print(d3 - d2)
print(d2 - d1)