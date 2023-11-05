package solution

func isValid(s string) bool {
	stack := make([]rune, 0)
	m := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}
	for _, c := range s {
		left, ok := m[c]
		if !ok {
			stack = append(stack, c)
		} else if len(stack) == 0 || stack[len(stack)-1] != left {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}
