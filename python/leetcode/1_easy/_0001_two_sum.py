class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
def main():
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))

if __name__ == "__main__":
    main()