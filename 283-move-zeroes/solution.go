func moveZeroes(nums []int) {
	zeroStart := 0
	for i, v := range nums {
		if v != 0 {
			nums[zeroStart], nums[i] = nums[i], nums[zeroStart]
			zeroStart++
		}
	}
}
