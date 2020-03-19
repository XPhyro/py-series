#!/usr/bin/env python3
# Calculate 0.01+0.002+0.0003+0.00004+...

from mpmath import *
import time
import datetime

MIN_DPS = 4

while True:
    s = input(f"To how many decimal points should the sum be calculated? (min={MIN_DPS})\n> ")
    try:
        s = int(s)
    except:
        continue
    if s >= MIN_DPS:
        mp.dps = s
        break

n = mp.dps * 10

s = mpf(0)

# Time is obtained twice not to interfere with the actual timing of the summation.
print(f"Initiated the summation on {datetime.datetime.now()}.\nSumming...")

t0 = time.time()

for i in range(n):
    s += (i + 1) * power(10, -2 - i)

t1 = time.time()

print(f"Completed the summation on {datetime.datetime.fromtimestamp(t1)}.\nWriting the results to the file \"sum\".")

s = str(s)

with open("sum", "w+") as f:
    f.write(f"Time started\t{t0}\nTime finished\t{t1}\nSum (=0.01+0.002+0.0003+...)\t")
    for i in s:
        f.write(i)
    f.write("\n")
    f.close()

print("Writing completed.")
