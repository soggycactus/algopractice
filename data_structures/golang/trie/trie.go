package trie

type Trie[K string | int, V any] struct {
	Nodes      map[K]*Trie[K, V]
	IsComplete bool
	Value      V
}

func NewTrie[K string | int, V any]() *Trie[K, V] {
	return &Trie[K, V]{
		Nodes: map[K]*Trie[K, V]{},
	}
}

func (t *Trie[K, V]) Add(nodes []K, value V) {
	if len(nodes) == 0 {
		t.Value = value
		t.IsComplete = true
		return
	}

	lookup, ok := t.Nodes[nodes[0]]
	if !ok {
		lookup = NewTrie[K, V]()
		t.Nodes[nodes[0]] = lookup
	}

	lookup.Add(nodes[1:], value)
}

func (t *Trie[K, V]) Get(nodes []K) V {
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

func (t *Trie[K, V]) LongestCommonPrefix() []K {
	result := []K{}
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

	return result
}
