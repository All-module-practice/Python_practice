# Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, 
# and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]

def capitals(word):
    #your code here
    index_store=[]
    for i in range(len(word)):
        if word[i]>='A' and word[i]<='Z':
            index_store.append(i)
    return index_store
