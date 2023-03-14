package helpers

func Pop[T any](list *[]T) T {
	value := (*list)[0]
	*list = (*list)[1:]
	return value
}
