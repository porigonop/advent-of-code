package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func get_number_of_1s(list []string, len int) []int {
	number_of_1s := make([]int, len)
	for _, item := range list {
		for index, char := range item {
			number_of_1s[index] += int(char - '0')
		}
	}
	return number_of_1s
}

func get_gamma_epsilon(list []string, len_value int) (string, string) {
	number_of_1s := get_number_of_1s(list, len_value)
	gamma := make([]rune, len_value)
	epsilon := make([]rune, len_value)
	for index, number_of_1 := range number_of_1s {
		if number_of_1 >= (len(list)/2)+len(list)%2 {
			gamma[index] = '1'
			epsilon[index] = '0'
		} else {
			epsilon[index] = '1'
			gamma[index] = '0'
		}
	}
	return string(gamma), string(epsilon)
}

func select_numbers(list []string, len_value int, predicate func([]string, int) string) string {
	current_index := 0
	for len(list) > 1 {
		new_list := []string{}
		gamma := predicate(list, len_value)
		for _, elt := range list {
			if elt[current_index] == gamma[current_index] {
				new_list = append(new_list, elt)
			}
		}
		if len(new_list) <= 1 {
			return new_list[0]
		}
		list = new_list
		current_index += 1
	}
	panic("unreachable")
}

func get_gamma(list []string, len_val int) string {
	gamma, _ := get_gamma_epsilon(list, len_val)
	return gamma
}
func get_epsilon(list []string, len_val int) string {
	_, epsilon := get_gamma_epsilon(list, len_val)
	return epsilon
}
func main() {
	const len_of_value = 12
	lines := []string{}
	file, err := os.Open("./3_input.txt")
	defer file.Close()
	check(err)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}
	gamma, epsilon := get_gamma_epsilon(lines, len_of_value)
	gamma_int, err := strconv.ParseUint(gamma, 2, 64)
	check(err)
	epsilon_int, err := strconv.ParseUint(epsilon, 2, 64)
	check(err)
	fmt.Println(epsilon_int * gamma_int)
	oxygen := select_numbers(lines, len_of_value, get_gamma)
	co2 := select_numbers(lines, len_of_value, get_epsilon)
	fmt.Println(oxygen, co2)
	oxygen_int, err := strconv.ParseUint(oxygen, 2, 64)
	check(err)
	co2_int, err := strconv.ParseUint(co2, 2, 64)
	check(err)
	fmt.Println(oxygen_int * co2_int)

}
