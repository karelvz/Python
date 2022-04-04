#ask user to input number
c0 = int(input("Enter a non-negative and non-zero integer: "))

steps = 0
while c0 > 0: #check if c0 is non-negative and non-zero
    if c0 != 1: #not equal to 1
        if c0 % 2 == 0: #check if number is even
            c0 /= 2
            steps += 1
            print(int(c0))
            continue
        else:
            c0 = 3*c0 + 1 #do this if the number is odd
            steps += 1
            print(int(c0))
    else:
        break

print("steps = ", steps)
