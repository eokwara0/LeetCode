

class Solution:

    def zigzag(self, word : str , rows : int ) -> str :
        
        # list of data
        # creates a 2-dimensional array
        data = [[ "" for x in range(len(word))] for x in range(rows)]

        # rows and columns counter 
        # bolean value end --> inidicates when the row counter reaches the last value in a column
        row , col , end = 0 , 0 , False

        # loops through the word
        for i in range( len( word ) ) :
            
            # checks if the row is at the beginning
            if row == 0:
                # row == 0 reset end to false
                end = False

            # checks if row has reached end
            if row == rows-1 :
                # aad character to the array
                data[row][col] = word[i]
                # increment column counter
                col += 1
                # decrement row --> goes back up the column
                row -= 1
                # set end to true
                end = True

            # checks if row counter is decreasing 
            elif row > 0 and end :
                    # add character to array at positio [row][column]
                    data[row][col] = word[i]

                    # increment column counter and decrement row counter
                    col += 1
                    row -= 1

            # if the top statement are not met 
            # add character to array and increment row counter
            else:
                data[row][col] = word[i]
                row += 1
            
        # returns word if rows == 1 else return the joined version of the array
        return word if rows == 1 else "".join(["".join(w) for w in data])



if __name__ == "__main__":
    sol = Solution()
    after = sol.zigzag("PAYPALISHIRING" , 1)
    print(after)