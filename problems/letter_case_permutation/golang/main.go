package main

import (
	"fmt"
	"strings"
)

var (
	letters = map[string]struct{}{
		"a": {},
		"b": {},
		"c": {},
		"d": {},
		"e": {},
		"f": {},
		"g": {},
		"h": {},
		"i": {},
		"j": {},
		"k": {},
		"l": {},
		"m": {},
		"n": {},
		"o": {},
		"p": {},
		"q": {},
		"r": {},
		"s": {},
		"t": {},
		"u": {},
		"v": {},
		"w": {},
		"x": {},
		"y": {},
		"z": {},
	}
)

func letterCasePermutation(s string) []string {
	answers := []string{}

	for i := 0; i < len(s); i++ {
		if _, ok := letters[strings.ToLower(string(s[i]))]; ok {
			if len(answers) == 0 {
				answers = append(answers, strings.ToLower(string(s[i])))
				answers = append(answers, strings.ToUpper(string(s[i])))
			} else {
				length := len(answers)
				for j := 0; j < length; j++ {
					answers[j] += strings.ToLower(string(s[i]))
					answers = append(answers, answers[j][:len(answers[j])-1]+strings.ToUpper(string(s[i])))
				}
			}
		} else {
			if len(answers) == 0 {
				answers = append(answers, string(s[i]))
			} else {
				for j := 0; j < len(answers); j++ {
					answers[j] += string(s[i])
				}
			}
		}
	}

	return answers
}

func main() {
	s := "a1b2"
	fmt.Println(letterCasePermutation(s))
}
