from typing import List


'''
    From this project i learnt about in Place algorithms
    This is when you write algorithms that don't use up extra space to compute 
    rather they achieve the same outcome by swaping and rearranging values in a data set.

'''
class Solution():

    # The merge function is derived from the merge sort algorithm
    # the function takes in the starting index , middle index and ending index 
    # and along with the value that you want to change it rearranges the values according to 
    # you specifications
    def __merge(self,nums,start:int, mid:int, end:int, val:int ):

        # list to store the rearranged values
        list_ = [] 

        # count to keep track of the index
        count = start

        # add all the values from start to mid along with their indices
        # whilst ignoring the numbers that match with @{val}
        for i in range(start, mid):
            if nums[i] !=val:
                list_.append((nums[i] , count ) )
                count += 1  # increment count

        # add all the values from mid to end along with their indices
        # whilst ignoring the numbers that match with @{val}
        for j in range(mid, end):
            if nums[j] !=val:
                list_.append((nums[j] , count))
                count += 1 # increment counter

        # add the values remaining values that match @[val]
        for w in range(start, end):
            if nums[w] == val:
                list_.append((nums[w] , count))
                count += 1 

        # swap the indices with the correct values
        for x , y  in list_:
            nums[y] = x



    # this function runs recursively to find and merge values 
    # and its based on the merge sort algorithm
    def __sortElements(self,nums:List[int] , val : int , start:int , end:int):

        if start >= end-1:
            return
        mid = (start+end)//2

        self.__sortElements( nums , val , start, mid)
        self.__sortElements( nums , val,mid,end )
        self.__merge(nums, start, mid, end, val)
        # print(nums)




    # removeElement calls __sortElement()
    def _removeElements(self,nums:List[int], val: int) -> int:
        self.__sortElements( nums , val , 0 , len(nums) )
        return len(nums) - len(list(filter(lambda x: x == val , nums )))


if __name__ == "__main__":

    #testing
    sol = Solution()
    nums = [3,2,2,2,4,3,6,7,3,232,3]
    number = sol._removeElements(nums,3)
    print(number)
    print(nums , number, sep="\n") 
