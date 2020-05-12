#!/usr/bin/env python3

import time
import datetime
import input_helper as ih


with open("sequence", "r") as f:
    l = eval(f.readlines()[-1][9:])

with open("sum", "w+") as f:
    f.write(f"Terms computed\t{len(l)}\nSum\t")
    for i in str(sum(l)):
        f.write(i)
    f.write("\n")
    f.close()

print("Writing completed.")
