

class Solution:
    def findMedianSortedArrays(self, nums1 : list , nums2 : list ) -> float:
        len_a1 = len(nums1);
        len_a2 = len(nums2);

        if len_a1 %2 != 0 and len_a2 %2 == 0:
            return float( nums1[-1] )
        elif len_a1 %2 == 0 and len_a2 %2 !=0 and ( len_a1 != 0 or len_a2 != 0 ) :
            return float( nums2[-1] )
        elif len_a1 %2 == 0 and len_a2 %2 == 0:
            return float((nums1[-1] + nums2[-1])/2 )
        elif len_a1 %2 != 0 and len_a2 %2 != 0 :
            newList = nums1 + nums2
            lenList = len( newList )
            if lenList == 0:
