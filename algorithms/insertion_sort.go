package main

import "fmt"

// insertionSort implements the insertion sort algorithm on an array of integers
func insertionSort(array []int) {
	for i := 1; i < len(array); i++ {
		for i > 0 && array[i] < array[i-1] {
			temp := array[i]
			array[i] = array[i-1]
			array[i-1] = temp
			i--
		}
	}
}

func main() {
	array := []int{4, 5, 2, 1, 3, 6, 7, 8}
	println(fmt.Sprintf("%v", array))
	insertionSort(array)
	println(fmt.Sprintf("%v", array))
}
