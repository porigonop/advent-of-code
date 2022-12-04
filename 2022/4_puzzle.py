
def overlap1(range_1, range_2):
  if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
    return True # range_2 is inside range_1
  if range_2[0] <= range_1[0] and range_2[1] >= range_1[1]:
    return True # range_1 is inside range_2
  return False


def overlap(range_1, range_2):
  if range_1[0] <= range_2[0] <= range_1[1]:
    return True # range_2[0] is inside range_1
  if range_1[0] <= range_2[1] <= range_1[1]:
    return True # range_2[1] is inside range_1
  if range_2[0] <= range_1[0] <= range_2[1]:
    return True # range_1[0] is inside range_2
  if range_2[0] <= range_1[1] <= range_2[1]:
    return True # range_1[1] is inside range_2
  return False



def print_range(range_):
  for i in range(0, 10):
    i = str(i)
    if i in range_:
      print(i, end="")
    else:
      print(".", end="")
  print("")
def main(puzzle_input: str):
  sum_overlap = 0
  for line in puzzle_input.splitlines():
    pairs = line.split(',')
    range_1 = [int(x) for x in pairs[0].split('-')]
    range_2 = [int(x) for x in pairs[1].split('-')]
    #print_range(range_1)
    #print_range(range_2)
    if overlap(range_1, range_2):
      sum_overlap += 1
      print("overlap")
  print(sum_overlap)
if __name__ == "__main__":
  puzzle_input = open("4_input.txt").read()
  #puzzle_input = open("4_easy_input.txt").read()
  main(puzzle_input)