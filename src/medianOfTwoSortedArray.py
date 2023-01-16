

class Solution:
    def findMedianSortedArrays(self, nums1 : list , nums2 : list ) -> float:
        len_a1 = len(nums1)
        len_a2 = len(nums2)
        nums = sorted(nums1 + nums2)
        sums = len_a1 + len_a2
        midIndex = sums // 2

        if sums % 2 != 0:
            return float(nums[midIndex])
        elif ( sums % 2 ) == 0 :
            return float((nums[midIndex] + nums[midIndex -1])) / 2



if __name__ == "__main__":
    sol = Solution()
    solution = sol.findMedianSortedArrays([1,2,3,3,5,34,3,34,32,3] , [4 , 5 , 6 ])

    print( solution )
        
