class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        outNums = []

        for key in nums1:
            Find = False
            Exist = False
            for data in nums2:
                print(key, ':', Find, Exist)
                if data == key:
                    Find = True
                if Find and data > key:
                    outNums.append(data)
                    Exist = True
                    break
            if Exist == False:
                outNums.append(-1)
            print(key, ":", outNums)
        return outNums

nums1 = [4,1,2]
nums2 = [1,3,4,2]

x = Solution()
print(x.nextGreaterElement(nums1, nums2))
