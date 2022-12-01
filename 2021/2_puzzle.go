package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}
func parseLine(line string, aim int) (int, int, int) {
	line_split := strings.Split(line, " ")
	text := line_split[0]
	value, err := strconv.Atoi(line_split[1])
	check(err)
	if text == "forward" {
		return value, value * aim, 0
	}
	if text == "up" {
		return 0, 0, -value
	}
	if text == "down" {
		return 0, 0, value
	}
	panic("Unreachable")
}
func main() {
	fmt.Println("hello world !")
	file, err := os.Open("./2_input.txt")
	defer file.Close()
	check(err)

	scanner := bufio.NewScanner(file)
	pos_h := 0
	depth := 0
	aim := 0
	for scanner.Scan() {
		text := scanner.Text()
		new_pos_h, new_depth, new_aim := parseLine(text, aim)
		pos_h += new_pos_h
		depth += new_depth
		aim += new_aim

	}
	fmt.Println("position: ", pos_h, " depth: ", depth, "multiplied: ", depth*pos_h)
}
