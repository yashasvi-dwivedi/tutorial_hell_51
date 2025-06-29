class Solution(object):
    def isPalindrome(self, s):
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(solution.isPalindrome("race a car"))  # False
    print(solution.isPalindrome(" "))  # True
    print(solution.isPalindrome("bob"))
