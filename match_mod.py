# equals word
# Simphiwe Mchunu
# 25 August 2015

def equals(word_one,word_two):
    if len(word_one)==len(word_two)==1 and word_one[0].lower() == word_two[0].lower():
        return True
    elif len(word_one)!=len(word_two):
        return False
    elif word_one[0].lower() == word_two[0].lower():
        return equals(word_one[1:],word_two[1:])
    else:
        return False
    #return word_one[0].lower() == word_two[0].lower() and word_one[-1].lower() == word_two[-1].lower()
def query(pattern,word):
    if len(pattern)==len(word)==1:
        return True
    elif word=='' and len(pattern)!='':
        return False
    if pattern[0].lower()==word.lower()[0] or pattern[0]=='?' and word.isalpha(): 
        return query(pattern[1:],word[1:])       
def match(pattern,word):
    if len(pattern)==0 and len(word)>=0:
            return True
    elif pattern[0]=='*' and len(word)>0:
        return match(pattern[1:],word[:])
    elif pattern[0]==word[0]:
        return match(pattern[1:],word[1:])
    elif pattern[-2:]==word[-2:] and pattern[-1]==word[-1]:
        return True
    elif pattern[0]=='*' and pattern[-1]==word[-1]:
        return True
    elif len(pattern)==len(word) and pattern[0]!=word[0]:
        return False
    elif len(pattern)==1 and pattern[0]==word[-1] and len(pattern)<len(word):
        return True
    return False        