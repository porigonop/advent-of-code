package main

import (
	"bufio"
	"os"
	"strings"
)

type BingoInt struct {
	number int
	marked bool
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}
func main() {
	file, err := os.Open("./3_input.txt")
	defer file.Close()
	check(err)

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	selected_numbers := strings.Split(scanner.Text(), ",")
	bingolines := [][]string{}
	for scanner.Scan() {
		line := scanner.Text()
		if line == "\n" {
			continue
		}
		bingolines = append(bingolines, strings.Fields(line))
	}
}
