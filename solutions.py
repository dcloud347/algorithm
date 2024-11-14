class Solution:
    @staticmethod
    def findKthNumber(m: int, n: int, k: int) -> int:
        left = 1
        right = m * n
        # 二分法返回最小的结果
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            count = 0
            # 算出有多少数比mid更小
            for i in range(1, n + 1):
                count += min(mid // i, m)
            """
            我们的目标是找到符合条件的最小值
            确定了范围内一定会有答案 并且之前的步骤已经确定了范围内一定会有正确的值
            二分法最后都会聚拢到n和n+1之间
            mid会为n
            如果mid大于等于目标值的话 right会变为n mid也会变为n 结果为n
            如果mid小于目标值的话 left会变为n+1 结果为n+1
            """
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left
