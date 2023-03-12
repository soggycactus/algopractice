package trie

import "strings"

type Trie struct {
	Nodes      map[string]*Trie
	IsComplete bool
	Value      interface{}
}

func NewTrie() *Trie {
	return &Trie{
		Nodes: map[string]*Trie{},
	}
}

func (t *Trie) Add(nodes []string, value interface{}) {
	if len(nodes) == 0 {
		t.Value = value
		t.IsComplete = true
		return
	}

	lookup, ok := t.Nodes[nodes[0]]
	if !ok {
		lookup = NewTrie()
		t.Nodes[nodes[0]] = lookup
	}

	lookup.Add(nodes[1:], value)
}

func (t *Trie) Get(nodes []string) interface{} {
	if len(nodes) == 0 {
		if t.IsComplete {
			return t.Value
		}
		return nil
	}

	lookup, ok := t.Nodes[nodes[0]]
	if !ok {
		return ""
	}

	return lookup.Get(nodes[1:])
}

func (t *Trie) LongestCommonPrefix() string {
	result := []string{}
	cursor := t

	for {
		if len(cursor.Nodes) == 1 {
			if cursor.IsComplete {
				break
			}

			for key, value := range cursor.Nodes {
				result = append(result, key)
				cursor = value
			}
		} else {
			break
		}
	}

	return strings.Join(result, "")
}
