class Solution(object):
    def anagram(self, s, t):
        if len(s) != len(t):
            return False
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1
        for char in t:
            count[ord(char) - ord("a")] -= 1
            if count[ord(char) - ord("a")] < 0:
                return False
        return True


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.anagram("anagram", "nagaram"))
    print(s.anagram("rat", "car"))
    print(s.anagram("listen", "silent"))
