package trie_test

import (
	"algopractice/data_structures/golang/trie"
	"strings"
	"testing"
)

func wordToArray(word string) []string {
	return strings.Split(word, "")
}

func TestTrie(t *testing.T) {
	tr := trie.NewTrie[string]()
	tr.Add(wordToArray("cat"), "hooray!")
	tr.Add(wordToArray("catt"), "hoorah!")
	tr.Add(wordToArray("cattermole"), "yes!")

	testCases := []struct {
		Word           string
		ExpectedResult string
	}{
		{
			Word:           "cat",
			ExpectedResult: "hooray!",
		},
		{
			Word:           "dog",
			ExpectedResult: "",
		},
		{
			Word:           "catt",
			ExpectedResult: "hoorah!",
		},
		{
			Word:           "cattermole",
			ExpectedResult: "yes!",
		},
	}

	for _, test := range testCases {
		nodes := wordToArray(test.Word)
		if result := tr.Get(nodes); result != test.ExpectedResult {
			t.Fail()
			t.Logf("Add/Get failed, expected: %v, got: %v", test.ExpectedResult, result)
		}
	}

	if result := tr.LongestCommonPrefix(); result != "cat" {
		t.Fail()
		t.Logf("LongestCommonPrefix failed, got: %v, expected: %v", result, "catt")
	}
}
