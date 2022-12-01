import sys
import os

day = sys.argv[1]
for file in os.listdir('.'):
    if file.startswith(day):
        raise FileExistsError()
open(f"{day}_easy_input.txt", "w+")
open(f"{day}_input.txt", "w+")
open(f"{day}_puzzle.py", "w+")