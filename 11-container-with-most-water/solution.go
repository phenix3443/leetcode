// -*- coding:utf-8; -*-
func maxArea(height []int) int {
	m := 0

	for l, r := 0, len(height)-1; l < r; {
		area := 0
		if height[l] < height[r] {
			area = (r - l) * height[l]
			l++
		} else {
			area = (r - l) * height[r]
			r--
		}

		if m < area {
			m = area
		}
	}
	return m
}
