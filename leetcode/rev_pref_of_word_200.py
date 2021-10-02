class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        final_result = ""
        count = 0
        flag = 0
        for i in word:
            count += 1
            if i == ch:
                final_result = self.rev_string(word, count)
                flag = 1
                return final_result
            

        if flag == 0:
            return word

    
    def rev_string(self, word, count):
        res = list(word[:count])
        res.reverse()
        value = "".join([str(i) for i in res]) + word[count:]
        return  value
        
        
if __name__ == "__main__":
    word = input("Please Enter a word\n")
    ch = input("Pleae Enter a Character\n")
    sln = Solution()
    result  = sln.reversePrefix(word, ch)  
    print(result)              
                
        