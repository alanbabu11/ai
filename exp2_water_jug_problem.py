print("Water Jug Problem (4L & 3L Jugs)")
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

while True:
    rno = int(input("Enter the Rule No: "))

    if rno == 1 and x < 4:
        x = 4  # Rule 1: Fill 4L jug
    elif rno == 2 and y < 3:
        y = 3  # Rule 2: Fill 3L jug
    elif rno == 5 and x > 0:
        x = 0  # Rule 5: Empty 4L jug
    elif rno == 6 and y > 0:
        y = 0  # Rule 6: Empty 3L jug
    elif rno == 7 and y > 0:  # Rule 7/9: Pour 3L into 4L
        x, y = (4, y - (4 - x)) if x + y >= 4 else (x + y, 0)
    elif rno == 8 and x > 0:  # Rule 8/10: Pour 4L into 3L
        x, y = (x - (3 - y), 3) if x + y >= 3 else (0, x + y)

    print(f"X = {x}")
    print(f"Y = {y}")

    if x == 2:
        print("The result is a Goal state")
        break
