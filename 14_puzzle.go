package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func step(polymer []rune, pair_insertion map[string]string) []rune {
	new_list := make([]rune, 0)
	polymer_str := string(polymer)
	for index, char := range polymer_str {
		new_list = append(new_list, char)
		if len(polymer_str) < index+2 {
			break
		}
		poly_substr := polymer_str[index : index+2]
		if data, ok := pair_insertion[poly_substr]; ok {
			new_list = append(new_list, rune(data[0]))
		}
	}
	return new_list
}
func count_occurence(polymer []rune) map[string]int {
	occurence := make(map[string]int)
	for _, char := range polymer {
		if data, ok := occurence[string(char)]; ok {
			occurence[string(char)] = data + 1
		} else {
			occurence[string(char)] = 1
		}
	}
	return occurence
}
func number_of_occurence(polymer []rune, pair_insertion map[string]string, step_number int) map[string]int {
	for i := 0; i < step_number; i++ {
		polymer = step(polymer, pair_insertion)
	}
	return count_occurence(polymer)
}

func merge_map(map1 map[string]int, map2 map[string]int) map[string]int {
	for k, v := range map2 {
		if _, ok := map1[k]; !ok {
			map1[k] = v
		} else {
			map1[k] += v
		}
	}
	return map1

}

func dict_of_occurence(pair_insertion map[string]string, step_number int) map[string]map[string]int {
	ans := make(map[string]map[string]int)
	for key, _ := range pair_insertion {
		ans[key] = number_of_occurence([]rune{rune(key[0]), rune(key[1])}, pair_insertion, step_number)
	}
	return ans
}
func main() {
	//file, err := os.Open("./14_easy_input.txt")
	MAX_ITERATION := 40
	BULK_ITERATION := 20
	file, err := os.Open("./14_input.txt")
	defer file.Close()
	check(err)
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	polymer := strings.TrimRight(scanner.Text(), "\n")
	polymer_list := make([]rune, 0)
	for _, char := range polymer {
		polymer_list = append(polymer_list, char)
	}
	scanner.Scan() // \n
	pair_insertion := make(map[string]string)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " -> ")
		pair_insertion[line[0]] = line[1]
	}

	for i := 0; i < BULK_ITERATION; i++ {
		polymer_list = step(polymer_list, pair_insertion)
	}
	remove_char := make(map[string]int)
	occurence := make(map[string]int)
	dict_pair_to_occurence := dict_of_occurence(pair_insertion, MAX_ITERATION-BULK_ITERATION)
	var occurence_new map[string]int
	for index := 1; index < len(polymer_list)-1; index++ {
		occurence_new = dict_pair_to_occurence[string(polymer_list[index-1:index+1])]
		char := string(polymer_list[index])
		if data, ok := remove_char[char]; ok {
			remove_char[char] = data - 1
		} else {
			remove_char[char] = -1
		}
		occurence = merge_map(occurence, occurence_new)
	}
	occurence_new = dict_pair_to_occurence[string(polymer_list[len(polymer_list)-2:])]
	occurence = merge_map(occurence, occurence_new)
	occurence = merge_map(occurence, remove_char)
	fmt.Println(occurence)
	mi := 10000000000000
	ma := 0
	for _, v := range occurence {
		if v > ma {
			ma = v
		}
		if v < mi {
			mi = v
		}
	}
	fmt.Println(ma - mi)
}
