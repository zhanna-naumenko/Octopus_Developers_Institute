name = "zhanna"
print(name.upper())
num1 = 4
num2 = 6
print(num1 + num2)

list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200
print(list1)

color = input('Please input one of the color "red", "green" or "yellow":  ')
if color == "red":
    print("Stop driving!")
elif color == "green":
    print("You can drive!")
elif color == "yellow":
    print("Slow down!")
else:
    print("The value is not defined!")