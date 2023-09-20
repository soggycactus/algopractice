package stack_test

import (
	"algopractice/data_structures/golang/stack"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestStack(t *testing.T) {
	stack := stack.Stack[int]{}
	stack.Push(1)
	stack.Push(2)
	stack.Push(3)

	assert.Equal(t, 3, stack.Len())
	assert.Equal(t, 3, stack.Pop())
	assert.Equal(t, 2, stack.Pop())
	assert.Equal(t, 1, stack.Pop())
	assert.Equal(t, 0, stack.Len())
}
