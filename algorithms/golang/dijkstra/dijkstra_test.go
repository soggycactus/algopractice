package dijkstra_test

import (
	"algorithms/dijkstra"
	"reflect"
	"testing"
)

func TestDijkstra(t *testing.T) {
	graph := dijkstra.NewGraph[struct{}]()

	graph.AddVertex("a", struct{}{})
	graph.AddVertex("b", struct{}{})
	graph.AddVertex("c", struct{}{})
	graph.AddVertex("d", struct{}{})
	graph.AddVertex("d", struct{}{})
	graph.AddVertex("e", struct{}{})

	graph.AddEdge("a", "d", 1)
	graph.AddEdge("a", "b", 6)
	graph.AddEdge("d", "b", 2)
	graph.AddEdge("d", "e", 1)
	graph.AddEdge("b", "e", 2)
	graph.AddEdge("b", "c", 5)
	graph.AddEdge("e", "c", 5)

	if result, expected := graph.ShortestPath("a", "c"), []string{"a", "d", "e", "c"}; !reflect.DeepEqual(result, expected) {
		t.Fail()
		t.Logf("ShortestPath failed, got: %v, expected: %v", result, expected)
	}
}
