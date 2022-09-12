
from timeit import timeit

class Solution:
    def containsDuplicate( self , nums: list[int]) -> bool :
        
        
                
        return False 
    
        
    def list_operation( self , nums: list[int] , limit : int, value : int  ) -> bool  :
        print( nums , value )
        if value in nums or len(nums) <= limit  :
            return True
        else :
            return self.list_operation( nums[ : len(nums)//2] , limit , value  )
    
    
    
    
    
if __name__ == "__main__":
    solution = Solution()
    data = [1,2,3,4]
    print(timeit( lambda : solution.containsDuplicate( data ) , number= 1 ))