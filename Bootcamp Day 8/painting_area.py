#The program will calculate how many ink cans you need
import math

def area_calc(height,width,walls,coverage):
    area = (height * width) * walls
    print(area)
    return area/coverage
#start
print("--- Welcome to Painting Calculator ---\n")
area = input("Do you aready know the total area of walls?(yes/no).. ").upper()
coverage = 5
if area == "YES":
    area = float(input("What the total area that you will paint? "))
    cans = math.ceil(area / coverage)
else:
    h = float(input("What the height of the wall? "))
    w = float(input("What the width of the wall? "))
    n = int(input("How many walls you will paint? "))
    cans = math.ceil(area_calc(h,w,n,coverage))

print(f"\nYou need to buy {cans} ink cans.")