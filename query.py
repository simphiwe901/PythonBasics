def query(pattern,word):
   if len(pattern)==len(word):
      if len(pattern)==len(word)==0:
         return True
      if pattern[0]==word[0]:
         return query(pattern[1:],word[1:])
      elif pattern[0]=='?':
         if pattern[0]=='?' and len(pattern)==len(word)==1:
            return True
         return query(pattern[1:],word[1:])
   return False
def main():
   a = input('Enter pattern:\n')
   b = input('Enter word:\n')
   print(query(a,b))
main()