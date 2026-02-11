# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(text, ending):
    # your code here...
    
    list1=list(text)
    list2=list(ending)
    
    list3=list1[-len(list2):]
    
    print(list3==list2)

t1="samurai"
e1="ai"

solution(t1,e1)
