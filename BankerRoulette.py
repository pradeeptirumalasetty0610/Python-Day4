import random as rand
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(f'{names[rand.randint(0,len(names)-1)]} is going to buy the meal today!')