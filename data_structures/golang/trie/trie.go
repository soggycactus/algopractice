package trie

import "strings"

type Trie[V any] struct {
	Nodes      map[string]*Trie[V]
	IsComplete bool
	Value      V
}

func NewTrie[V any]() *Trie[V] {
	return &Trie[V]{
		Nodes: map[string]*Trie[V]{},
	}
}

func (t *Trie[V]) Add(nodes []string, value V) {
	if len(nodes) == 0 {
		t.Value = value
		t.IsComplete = true
		return
	}

	lookup, ok := t.Nodes[nodes[0]]
	if !ok {
		lookup = NewTrie[V]()
		t.Nodes[nodes[0]] = lookup
	}

	lookup.Add(nodes[1:], value)
}

func (t *Trie[V]) Get(nodes []string) V {
	if len(nodes) == 0 {
		if t.IsComplete {
			return t.Value
		}
		return *new(V)
	}

	lookup, ok := t.Nodes[nodes[0]]
	if !ok {
		return *new(V)
	}

	return lookup.Get(nodes[1:])
}

func (t *Trie[V]) LongestCommonPrefix() string {
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
