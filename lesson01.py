
# word = input('Enter a word: ')
# num = int(input('Enter a number: '))

# try:
#   print(word*num)
# except:
#   print('enter a actual integer and word')


# count = 1
# while count < 4:
#   print(count)
#   count +=1

# for i in range(5):
#   print('this is iteration',i)
#   i=i+1

import random
n = random.randint(1,10)
print(n)
print(abs(-3))

num_list=[3,5,-1,6,2]
print(sum([1,3,4]))
max = max(num_list)
min = min(num_list)
print(max)
print(min)
rand_let = random.choice('random')
coin = ['head', 'tail']
side = random.choice(coin)
deck = ['a','b','c']
random.shuffle(deck)
print(deck)
string = 'hello'
print(string[1])
string = 'hello'[2:5]
print(string)
print(sorted('listen'))
dice = random.randint(1,6)
print(dice)