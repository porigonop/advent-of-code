package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	fmt.Println("hello World !")
	file, err := os.Open("./1_input.txt")
	defer file.Close()
	check(err)

	scanner := bufio.NewScanner(file)
	/*
	   if line is greater than 64K, we need to add a buffer:
	   buf := make([]byte, 128000)
	   scanner.Buffer(buf, 128000)
	*/
	a := math.Inf(1)
	b := math.Inf(1)
	c := math.Inf(1)
	count := 0
	for scanner.Scan() {
		d, err := strconv.ParseFloat(scanner.Text(), 64)
		check(err)
		if b+c+d > a+b+c {
			count += 1
		}
		a = b
		b = c
		c = d
	}
	check(scanner.Err())
	fmt.Println(count)
}
