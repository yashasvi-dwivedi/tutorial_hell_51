class Solution(object):
    def clearDigits(self, s):
        res = ""
        for c in s:
            if c.isdigit():
                if res:
                    res = res[:-1]
            else:
                res += c
        return res


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.clearDigits("abc123def456"))
    print(sol.clearDigits("hello123world"))
    print(sol.clearDigits("cb34"))
    print(sol.clearDigits("cleardigits123"))
