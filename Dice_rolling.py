import random

def roll():
    return random.randint(1, 6)
result = roll()
if result == 6:
    print("6 !you rolled the highest")
elif result == 1 : 
    print("1 !you rolled the lowest")   
elif result == 2: 
    print(" 2! two for the crew")   
elif result == 3 : 
    print(" three you are free")   
elif result == 4: 
    print(" four ! score more")   
elif result == 5 : 
    print("five alive")
   