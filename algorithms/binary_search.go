package main

import (
	"fmt"
	"log"
	"sort"
)

func binarySearch(array []int, target int) (*int, error) {
	left := 0
	right := len(array) - 1

	for left <= right {
		mid := left + ((right - left) / 2)

		switch {
		case array[mid] == target:
			return &mid, nil
		case array[mid] < target:
			left = mid + 1
		case array[mid] > target:
			right = mid - 1
		}
	}

	return nil, fmt.Errorf("value %v not in array", target)
}

func main() {
	array := []int{4, 5, 3, 6, 7, 8, 12, 11, 1, 11, 45, 72}
	target := 6
	sort.Slice(array, func(i, j int) bool {
		return array[i] < array[j]
	})

	println(fmt.Sprintf("%v", array))
	index, err := binarySearch(array, target)
	if err != nil {
		log.Fatal(err)
	}
	println(fmt.Sprintf("value %d at index %d", target, *index))

	target = 12
	index, err = binarySearch(array, target)
	if err != nil {
		log.Fatal(err)
	}
	println(fmt.Sprintf("value %d at index %d", target, *index))
}
