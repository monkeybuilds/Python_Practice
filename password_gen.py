import random

sym = int(input("Enter the no of symbol: "))
num = int(input("Enter the Number"))
lett = int(input("Enter the Number"))

password = ""
for i in range(1, lett + 1):
    ran = random.choice(lett)

