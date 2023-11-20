package solution

func maxArea(height []int) int {
	max := 0
	for l, r := 0, len(height)-1; l < r; {
		area, h := 0, 0

		if height[l] < height[r] {
			h = height[l]
			l++
		} else {
			h = height[r]
			r--
		}
		area = (r - l) * h
		if max < area {
			max = area
		}
	}
	return max
}
