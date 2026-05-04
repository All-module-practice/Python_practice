# A pangram is a sentence that contains every single letter of the alphabet at least once. 
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(st):
    dicte={}
    
    for c in st:
        ch=c
        if c>='A' and c<='Z':
            ch=c.lower()
        if ch>='a' and ch<='z':
            if ch in dicte:
                dicte[ch]+=1
            else:
                dicte[ch]=1
    count=0
    
    for k,val in dicte.items():
        if k>='a' and k<='z':
            if val>=1:
                count+=1
    return True if count==26 else False
