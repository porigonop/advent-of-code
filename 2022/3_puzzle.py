from pprint import pprint
PRIORITY = {
  letter: index + 27 for index, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
} | {
  letter: index + 1 for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz")
}

def main1(puzzle_input: str):
  rucksacks = []
  sum_priority = 0
  for line in puzzle_input.splitlines():
    rucksacks.append(line)
    if len(rucksacks) == 3:
      for item in rucksacks[0]:
        if item in rucksacks[1] and item in rucksacks[2]:
          sum_priority += PRIORITY[item]
          break
      rucksacks = []
  print(sum_priority)



def main(puzzle_input: str):
  sum_priority = 0
  for line in puzzle_input.splitlines():
    comp1 = line[:len(line)//2]
    comp2 = line[len(line)//2:]
    for item in comp1:
      if item in comp2:
        sum_priority += PRIORITY[item]
        # print(PRIORITY[item])
        break
  print(sum_priority)
            

if __name__ == "__main__":
  puzzle_input = open("3_input.txt").read()
  puzzle_input = open("3_easy_input.txt").read()
  main(puzzle_input)