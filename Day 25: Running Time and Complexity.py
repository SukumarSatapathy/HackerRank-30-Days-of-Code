import math
for item in [int(input()) for k in range(int(input()))]:
    prime = True
    if item == 1:
        print("Not prime")
        continue

    for i in range(2, int(math.sqrt(item)) +1 ):
        if item % i == 0:
            prime = False
            break
    print("Prime" if prime else "Not prime")
