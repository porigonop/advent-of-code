

def main(input_string: str):
    list_of_elves = []
    list_of_calories = []
    for line in input_string.splitlines():
        if line == "":
            list_of_elves.append(sum(list_of_calories))
            list_of_calories = []
        else:
            list_of_calories.append(int(line))
    list_of_elves.append(sum(list_of_calories))


    # find the top three elves
    list_of_elves.sort(reverse=True)
    print(sum(list_of_elves[:3]))


if __name__ == "__main__":
    input_file = open("1_input.txt", "r")
    main(input_file.read())