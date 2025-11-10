class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False

def main():
    s = Solution()
    print(s.isPalindrome(-121))

if __name__ == "__main__":
    main()