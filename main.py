year = int(input("Enter the year you want to check: "))
if ((year%4 == 0) and (year%10 != 0)) or (year%400 == 0):
    print("Leap year.")
else:
    print("Normal year.")