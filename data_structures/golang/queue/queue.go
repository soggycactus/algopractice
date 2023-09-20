package queue

type Queue[T any] []T

func (q *Queue[T]) Push(v T) {
	*q = append(*q, v)
}

func (q *Queue[T]) Pop() T {
	v := (*q)[0]
	*q = (*q)[1:]
	return v
}

func (q *Queue[T]) Peek() T {
	return (*q)[0]
}

func (q *Queue[T]) Len() int {
	return len(*q)
}
