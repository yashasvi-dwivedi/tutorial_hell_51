class Solution(object):
    def mergeArrays(self, nums1, nums2):
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j += 1
            elif nums1[i] == nums2[j]:
                merged.append(nums1[i])
                i += 1
                j += 1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        return merged


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 5, 10]
    nums2 = [4, 5, 6]
    print(s.mergeArrays(nums1, nums2))
