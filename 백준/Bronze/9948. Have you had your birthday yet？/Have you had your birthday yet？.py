import sys
input = sys.stdin.readline

month = ["January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"]

while True:
    day, mon = input().split()
    day = int(day)

    if day == 0:
        break
    mon = month.index(mon)+1

    if mon == 2 and day == 29:
        print("Unlucky")
    elif mon < 8:
        print("Yes")
    elif mon > 8:
        print("No")
    else:
        if day == 4:
            print("Happy birthday")
        elif day < 4:
            print("Yes")
        else:
            print("No")