# cook your dish here
def order(sentence):
    if not sentence:
        return ""
    words=sentence.split()
    l=len(words)
    list2=[None]*l
    for word in words:
        for ch in word:
            if ch.isdigit():
                num=int(ch)
                list2[num-1]=word
                break
    stre=" ".join(list2)
    return stre
    pass


sen="is2 Thi1s T4est 3a"
num=order(sen)

print(num)
