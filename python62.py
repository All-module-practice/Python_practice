# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# Example
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
# Note
# In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

def count_smileys(arr):
    count=0
    for ch in arr:
        isnot=False
        ise=isn=ism=0
        for i in ch:
            if i in ':;':
                if isn==1 or ism==1 or ise==1:
                    isnot=True
                    break
                else:
                    ise=1
            elif i in "-~":
                if ism==1 or isn==1:
                    isnot=True
                    break
                else:
                    isn=1
            elif i in ")D":
                if ism!=1:
                    ism=1
                else:
                    isnot=True
                    break
            else:
                isnot=True
            
        if isnot==False:
            count+=1
        print(f"{count}:{ch}")
    return count
