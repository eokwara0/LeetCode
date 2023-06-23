
'''
    The Goal of this challenge is to determine the median of two sorted arrays/lists
    You have to sort the list then find the median
'''
class Solution:

    # finds the median of two sorted arrays/lists
    def findMedianSortedArrays(self, nums1 : list , nums2 : list ) -> float:
        # length of the first array
        a1 = len(nums1) 

        # length of the second array
        a2 = len(nums2)

        # joining two arrays together
        nums = nums1 + nums2

        # sorting the lists using merge sort
        self.__mergeSort( nums , 0 , len(nums))

        # sum of the lengths
        sums = a1 + a2

        # middle index of the two lists
        midIndex = sums // 2

        # if the sum modulos 2 is not equal to 0
        # then we need to return the middle value at midIndex
        if sums % 2 != 0:
            return float(nums[midIndex]) # return the middle value at midIndex
        # if the sum modulos 2 is equal to 0
        # return the sum of the middle values at midIndex plus the value at midIndex-1 divided by 2
        elif ( sums % 2 ) == 0 :
            return float((nums[midIndex] + nums[midIndex -1])) / 2


    # merges two lists using their indices
    def __merge(self, sequence , start , mid , end):

        count = start
        lst = []
        x = start
        y = mid

        while x < mid and y < end:
            if sequence[x] < sequence[y]:
                lst.append((sequence[x] , count))
                count +=1 
                x +=1 
            else:
                lst.append((sequence[y] , count ))
                y += 1
                count += 1 

        while x < mid:
            lst.append((sequence[x] , count ) )
            count +=1
            x += 1
        while y < end:
            lst.append((sequence[y] , count ))
            count +=1 
            y+=1

        for i , j in lst:
            sequence[j] = i 
       
        # for w in range(len(lst)):
        #     sequence[start] = lst[w][0]
        #     start = start + 1

        

    # makes a recursive call to divide the sequence
    # until it only has a single element
    # then merge the lists into one and go up the recursion tree
    def __mergeSort(self,sequence , start , end):

        if start >= end -1:
            return

        mid = (start + end ) // 2


        self.__mergeSort(sequence , start , mid )
        self.__mergeSort( sequence , mid , end)
        self.__merge(sequence , start , mid , end)




if __name__ == "__main__":
    sol = Solution()
    seq = [3,2,2,3]
    seq2 = [3,2,2,3]
    solution = sol._findMedianSortedArrays( seq , seq2 )
    print(solution)

