import sys
import os

day = sys.argv[1]
for file in os.listdir('.'):
    if file.startswith(day):
        raise FileExistsError()
open(f"{day}_easy_input.txt", "w+")
open(f"{day}_input.txt", "w+")
puzzle = open(f"{day}_puzzle.py", "w+")
puzzle.write(f"def main(puzzle_input: str):\n")
puzzle.write(f"    pass\n")
puzzle.write("if __name__ == \"__main__\":\n")
puzzle.write("  puzzle_input = open(\"{}_input.txt\").read()\n".format(day))
puzzle.write("  puzzle_input = open(\"{}_easy_input.txt\").read()\n".format(day))
puzzle.write("  main(puzzle_input)".format(day))