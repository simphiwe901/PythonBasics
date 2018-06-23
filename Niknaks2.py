# program called niknks that prompts the user to guess 4 mystery letter code
# Simphiwe Mchunu
# 25 July 2015

import random
def main():
 difficulty=int(input('Choose difficulty level (4 to 26):\n'))
 letters=list('abcdefghijklmnopqrstuvwxyz')[0: difficulty]
 print('The letters in the code are chosen from: {}.'.format(letters))
 secret_code=[]
 for i in range(4):
  rand_index=random.randint(0, len(letters)-1)
  letter=letters.pop(rand_index)
  secret_code.append(letter)
main()