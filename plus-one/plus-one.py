class Solution:
    def plusOne(self, m: List[int]) -> List[int]:
        n = len(m)
        for i in range(n):
            idx = n - 1 - i
            if m[idx] == 9:
                m[idx] = 0
            else:
                m[idx] += 1
                return m
        return [1] + m
        
