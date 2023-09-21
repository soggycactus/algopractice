package main

import "container/heap"

type Heap []int

func (h Heap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h Heap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h Heap) Len() int {
	return len(h)
}

func (h *Heap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *Heap) Pop() any {
	v := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	return v
}

func main() {
	items := &Heap{3, 2, 1, 5, 4}
	heap.Init(items)
	heap.Push(items, 6)

	for items.Len() > 0 {
		println(heap.Pop(items).(int))
	}
}
