class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]


# Test cases
if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    s.rotate(nums1, k1)
    print(nums1)

    nums2 = [-1, -100, 3, 99]
    k2 = 2
    s.rotate(nums2, k2)
    print(nums2)
