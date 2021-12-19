if __name__ == "__main__":
    input = open("./7_easy_input.txt")
    numbers = list(map(int, input.readline().strip().split(',')))
    min_fuel = 3000000000000000
    for i in range(max(numbers)):
        sum_fuel = 0
        for number in numbers:
            number_of_move = (number - i) * (1 if number - i > 0 else -1)
            sum_fuel += number_of_move * (number_of_move + 1)/2
        if sum_fuel < min_fuel:
            min_fuel = sum_fuel
    print(min_fuel)


