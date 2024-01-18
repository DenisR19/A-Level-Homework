def fizz_buzz(num1, num2, num3):
    for i in range(1, num3 + 1):
        if not i%num1 and not i%num2:
            print("FB", end=' ')
        elif i%num1 and not i%num2:
            print("F", end=' ')
        elif not i%num2 and i%num2:
            print("B", end=' ')
        else:
            print(i, end=' ')

with open("listH3-1.py", "r") as file:
    for line in file:
        nums = list(map(int, line.split()))
        fizz_buzz(*nums)
