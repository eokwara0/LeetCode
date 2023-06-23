
# Solution Class for implementing a solution
class Solution:
    
    ## validates if a list of integers contains duplicates
    ## if True return true 
    ## if It does not contain duplicates return false 
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Empty dictionary
        data_ = {}
        
        # Iterates over the nums and adds a key value pair to the dictionary
        # with the key being the number and the value being the number of occurrences
        for i in nums:
            #try catch statement
            try:
                
                # Increments if value is already present
                # and checks if the value is greater than 1 
                data_[i] = data_[i] + 1
                if data_[i] > 1 :
                    return True
                
            except KeyError:
                # if value is not present
                # add the value as a key and set the value to 1 
                data_[i] = 1
                
        # return false if no value has duplicates
        return False
            
        
        
        
        
        