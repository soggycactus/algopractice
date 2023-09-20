package queue_test

import (
	"algopractice/data_structures/golang/queue"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestQueue(t *testing.T) {
	queue := queue.Queue[int]{}

	queue.Push(1)
	queue.Push(2)
	queue.Push(3)

	assert.Equal(t, 3, queue.Len())
	assert.Equal(t, 1, queue.Peek())
	assert.Equal(t, 1, queue.Pop())
	assert.Equal(t, 2, queue.Peek())
	assert.Equal(t, 2, queue.Pop())
	assert.Equal(t, 3, queue.Peek())
	assert.Equal(t, 3, queue.Pop())
	assert.Equal(t, 0, queue.Len())
}
