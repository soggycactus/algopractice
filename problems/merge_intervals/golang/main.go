package main

import (
	"log"
	"math"
	"reflect"
)

func mergeIntervals(x [][]int) [][]int {
	result := [][]int{x[0]}
	last := len(result) - 1

	overwrite := func(x, y []int, key int) {
		value := []int{
			int(
				math.Min(float64(x[0]), float64(y[0])),
			),
			int(
				math.Max(float64(x[1]), float64(y[1])),
			),
		}

		result[key] = value
	}

	for i := 1; i < len(x); i++ {
		switch {
		case result[last][1] >= x[i][0]:
			overwrite(result[last], x[i], last)
		case result[last][0] == x[i][0] && result[last][1] < x[i][0]:
			overwrite(result[last], x[i], last)
		case result[last][1] < x[i][0]:
			result = append(result, x[i])
			last++
		}
	}

	return result
}

func main() {
	type testCase struct {
		Input    [][]int
		Expected [][]int
	}

	testCases := []testCase{
		{
			Input:    [][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}},
			Expected: [][]int{{1, 6}, {8, 10}, {15, 18}},
		},
		{
			Input:    [][]int{{1, 4}, {4, 5}},
			Expected: [][]int{{1, 5}},
		},
		{
			Input:    [][]int{{1, 4}, {0, 4}},
			Expected: [][]int{{0, 4}},
		},
		{
			Input:    [][]int{{1, 4}, {2, 3}},
			Expected: [][]int{{1, 4}},
		},
	}

	for _, test := range testCases {
		if result := mergeIntervals(test.Input); !reflect.DeepEqual(result, test.Expected) {
			log.Printf("test case %v failed - got: %v, wanted: %v", test.Input, result, test.Expected)
		}
	}
}
