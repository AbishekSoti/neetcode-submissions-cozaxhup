class Solution:

    def encode(self, strs: List[str]) -> str:
        s =""

        for word in strs:
            len(word)
            
            s +=str(len(word)) + "#" + word
        #print(s)
        return s
        
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        starting_point=0# where to start reading the list from
        counter = 0 # how long is the list
        i = 0 # the iterator/position of hashtag

        while i<len(s):
            if s[i] == "#":
                #print(starting_point)
                #print(i)

                counter = int(s[starting_point:i])

                decoded_list.append(s[i+1:i+counter+1])
                #print(decoded_list)
                i+=counter+1
                starting_point=i

            else:
                i+=1
            
        return decoded_list