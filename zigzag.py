

class Solution:

    def zigzag(self, word : str , rows : int ) -> str :
        
        # list of data
        data = [[ "" for x in range(len(word))] for x in range(rows)]

        # rows and columns counter 
        row , col , end = 0 , 0 , False

        for i in range( len( word ) ) :
            
            if row == 0:
                end = False


            if row == rows-1 :
                data[row][col] = word[i]
                col += 1
                row -= 1
                end = True

            elif row > 0 and end :
                    data[row][col] = word[i]
                    col += 1
                    row -= 1
            else:
                data[row][col] = word[i]
                row += 1
            
        return word if rows == 1 else "".join(["".join(w) for w in data])



if __name__ == "__main__":
    sol = Solution()
    after = sol.zigzag("PAYPALISHIRING" , 1)
    print(after)