#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
    precision = int(input("Decimal precision (1–10): "))
    target = round(math.pi, precision)

    start = time.time()

    pi = 0
    i = 0
    while round(pi, precision) != target:
        pi += 4 * (-1)**i / (2*i + 1)
        i += 1

    end = time.time()

    print(f"\nApproximated π: {round(pi, precision)}")
    print(f"Iterations:     {i}")
    print(f"Time taken:     {end - start:.4f} seconds")

if __name__ == '__main__':
    main()
