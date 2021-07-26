package main

import "fmt"

func swap(array []int, a, b int) {
	temp := array[a]
	array[a] = array[b]
	array[b] = temp
}

func partition(array []int, start, end int) int {
	pivot := end

	var itemFromLeft, itemFromRight int
	for {
		for i := start; i <= end; i++ {
			if array[i] >= array[pivot] {
				itemFromLeft = i
				break
			}
		}

		for i := end; i >= 0; i-- {
			if array[i] < array[pivot] {
				itemFromRight = i
				break
			}
		}

		if itemFromLeft >= itemFromRight {
			break
		}

		swap(array, itemFromLeft, itemFromRight)
	}

	swap(array, itemFromLeft, pivot)
	return itemFromLeft
}

func quicksort(array []int, start, end int) {
	if start < end {
		pivot := partition(array, start, end)
		quicksort(array, start, pivot-1)
		quicksort(array, pivot+1, end)
	}
}

func main() {
	array := []int{2, 6, 5, 3, 8, 7, 1, 0}
	println(fmt.Sprintf("%v", array))
	quicksort(array, 0, len(array)-1)
	println(fmt.Sprintf("%v", array))
}
