year = int(input())

if year % 4 == 0 and not (year % 100 == 0):
    print("Leap")
else:
    if year % 400 == 0:
        print("Leap")
    else:
        print("Ordinary")
