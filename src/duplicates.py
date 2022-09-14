class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data_ = {}
        for i in nums:
            try:
                data_[i] = data_[i] + 1
                if data_[i] > 1 :
                    return True
            except KeyError:
                data_[i] = 1
        return False
            
        
        
        
        
        