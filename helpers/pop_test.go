package helpers_test

import (
	"algopractice/helpers"
	"reflect"
	"testing"
)

func TestPop(t *testing.T) {
	list := []string{"a", "b", "c"}
	pop := helpers.Pop(&list)

	if pop != "a" {
		t.Fail()
		t.Logf("Pop failed, got: %v, expected: a", pop)
	}

	if expected := []string{"b", "c"}; !reflect.DeepEqual(list, expected) {
		t.Fail()
		t.Logf("Pop failed to modify list in-place, got: %v, expected: %v", list, expected)
	}
}
