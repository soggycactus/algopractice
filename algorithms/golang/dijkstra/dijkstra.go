package dijkstra

import (
	"math"
)

func NewGraph[V any]() *Graph[V] {
	return &Graph[V]{
		Vertices: map[string]*Vertex[V]{},
	}
}

type Graph[V any] struct {
	Vertices map[string]*Vertex[V]
}

type Vertex[V any] struct {
	Value V
	Edges map[string]*Edge[V]
}

type Edge[V any] struct {
	Weight float64
	Vertex *Vertex[V]
}

func (g *Graph[V]) AddVertex(key string, value V) {
	g.Vertices[key] = &Vertex[V]{
		Value: value,
		Edges: make(map[string]*Edge[V]),
	}
}

func (g *Graph[V]) AddEdge(srcKey, destKey string, weight float64) {
	src, ok := g.Vertices[srcKey]
	if !ok {
		return
	}

	dst, ok := g.Vertices[destKey]
	if !ok {
		return
	}

	src.Edges[destKey] = &Edge[V]{
		Weight: weight,
		Vertex: dst,
	}
}

func (g *Graph[V]) Neighbors(key string) []*Vertex[V] {
	lookup, ok := g.Vertices[key]
	if !ok {
		return nil
	}

	result := []*Vertex[V]{}

	for _, edge := range lookup.Edges {
		result = append(result, edge.Vertex)
	}

	return result
}

type result struct {
	distanceFromStart float64
	previousVertex    string
}

func (g *Graph[V]) ShortestPath(srcKey, destKey string) []string {
	_, ok := g.Vertices[srcKey]
	if !ok {
		return nil
	}

	results := make(map[string]result)
	unvisited := map[string]struct{}{}

	for key := range g.Vertices {
		if key == srcKey {
			results[key] = result{
				distanceFromStart: 0,
			}
		} else {
			results[key] = result{
				distanceFromStart: math.Inf(1),
			}
		}

		unvisited[key] = struct{}{}
	}

	current := srcKey
	for len(unvisited) > 0 {
		// for each neighbor of the current vertex, calculate the distance from the start
		// if the distance is lower than what has already been calculated, update it
		for key, edge := range g.Vertices[current].Edges {
			if _, ok := unvisited[key]; !ok {
				continue
			}

			distance := results[current].distanceFromStart + edge.Weight
			if distance < results[key].distanceFromStart {
				results[key] = result{
					distanceFromStart: distance,
					previousVertex:    current,
				}
			}
		}

		// Delete the current vertex from the unvisited list
		delete(unvisited, current)

		// Select the vertex with the minimum distance from the start, and restart the loop
		min := math.Inf(1)
		for key := range unvisited {
			result := results[key]
			if result.distanceFromStart < min {
				min = result.distanceFromStart
				current = key
			}
		}
	}

	final := []string{destKey}
	cursor := results[destKey]

	for {
		if cursor.previousVertex == "" {
			break
		}
		final = append(final, cursor.previousVertex)
		cursor = results[cursor.previousVertex]
	}

	return reverseSlice(final)
}

func reverseSlice[T any](s []T) []T {
	result := []T{}

	for i := len(s) - 1; i >= 0; i-- {
		result = append(result, s[i])
	}

	return result
}
