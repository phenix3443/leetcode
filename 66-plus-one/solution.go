// -*- coding:utf-8; -*-

func plusOne(digits []int) []int {
	lastNot9 := -1
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] == 9 {
			digits[i] = 0
		} else {
			lastNot9 = i
			break
		}
	}
	if lastNot9 == -1 {
		digits = append([]int{1}, digits...)
	} else {
		digits[lastNot9]++
	}
	return digits
}
