class Solution:
    @staticmethod
    def findKthNumber(m: int, n: int, k: int) -> int:
        left = 1
        right = m * n
        while left < right:
            mid = (left + right) // 2
            count = 0
            # 算出有多少数比mid更小
            for i in range(1, n+1):
                count += min(mid // i, m)
            if count >= k:
                right = mid-1
            else:
                left = mid+1
        return left
