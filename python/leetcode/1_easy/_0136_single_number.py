class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # result = 0

        # for num in nums:
        #     result ^= num
        # return result
        

        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                return nums[i]
            
        return -1

def main():
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))
    print(s.singleNumber([2, 2, 1]))

if __name__ == "__main__":
    main()