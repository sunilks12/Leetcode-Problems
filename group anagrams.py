lst=['eat','ate','tan','nat','bat']

dict_vals={}

for i in lst:
    dict_val={}
    for j in i:
        if j not in dict_val:
            dict_val[j]=1
        else:
            dict_val[j]=dict_val[j]+1
    dict_vals[i]=dict_val

print(dict_vals)


from collections import defaultdict

anagram_groups = defaultdict(list)

for word in dict_vals:

    char_counts = dict_vals[word]
    print("char count")
    print(char_counts)
    sorted_word = ''.join(sorted(word))  # Sort the characters of the word
    print(sorted_word)
    
    # Add the word to the corresponding anagram group
    anagram_groups[sorted_word].append(word)
print(anagram_groups.values())




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lst=defaultdict(list)
        for s in strs:
            key=''.join(sorted(list(s)))
            lst[key].append(s)

        output=[]
        for l in lst.values():
            output.append(l)
        return output






class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_vals={}
        

        for i in strs:
            dict_val={}
            for j in i:
                if j not in dict_val:
                    dict_val[j]=1
                else:
                    dict_val[j]=dict_val[j]+1
            dict_vals[i]=dict_val


        from collections import defaultdict

        anagram_groups = defaultdict(list)

        for word in dict_vals:

            char_counts = dict_vals[word]

            sorted_word = ''.join(sorted(word))  # Sort the characters of the 
            
            # Add the word to the corresponding anagram group
            anagram_groups[sorted_word].append(word)
        return anagram_groups.values()
        #print(anagram_groups.values())

