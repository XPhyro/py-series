#!/usr/bin/env python3
# Calculate (0-sqrt(0)+(1-sqrt(1))+(2-sqrt(2))+...

import time
import datetime
import input_helper as ih

n = ih.get_pint("How many terms of the series should be computed?") 

s = 0

# Time is obtained twice not to interfere with the actual timing of the summation.
print(f"Initiated the summation on {datetime.datetime.now()}.\nSumming...")

t0 = time.time()

for i in range(n):
    s += i - pow(i, 0.5) 

t1 = time.time()

print(f"Completed the summation on {datetime.datetime.fromtimestamp(t1)}.\nWriting the results to the file \"sum\".")

s = str(s)

with open("sum", "w+") as f:
    f.write(f"Time started\t{t0}\nTime finished\t{t1}\nTerms computed\t{n}\nSum (=(0-sqrt(0))+(1-sqrt(1))+(2-sqrt(2)))\t")
    for i in s:
        f.write(i)
    f.write("\n")
    f.close()

print("Writing completed.")
