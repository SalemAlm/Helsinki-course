# # Write your solution here
# number = 2
# while 2<=number<=30:
#     print(number)
#     number += 2

# Fix the program
# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while number > 0 :
#     print(number)
#     number -= 1

# print("Now!")
    
#    upper = int(input('Upper limit: '))
# number = 1
# while number<upper: 
#     print(number)
#     number+=1

# upper = int(input('Upper limit: '))
# number = 1
# while number<=upper: 
#     print(number)
#     number*=2

WORKING WITH STRINGS: 

# word = ''
# string = input('Please type in a string: ')
# num = int(input('Please type in an amount: '))
# word= word+string 
# print(word*num)

# string1= input('Please type in a string 1: ')
# string2= input('Please type in a string 2: ')
# if len(string1)>len(string2):
#     print(f'{string1} is longer')
# elif len(string2)>len(string1):
#     print(f'{string2} is longer')
# else: 
#     print("The strings are equally long")

# text = input('Please type in a string: ')
# for char in reversed(text):
#     print(char)
    

#     # Write your solution here
# text = input('Please type in a string: ')
# index= len(text)-1
# while index>=0: 
#     print(text[index])
#     index-=1 
    

#     # Write your solution here
# text = input('Please type in a string: ')
# if text[-2]==text[1]:
#     print(f'The second and the second to last characters are {text[1]}')
# else: 
#     print('The second and the second to last characters are different')

# wid= int(input('Width: '))
# print('#' * wid)

# tim=0
# wid= int(input('Width: '))
# hei= int(input('Height: '))
# while hei>tim: 
#     print('#' * wid)
#     tim+=1


# string= input("Please type in a string: ")
# while string!='': 
#     if string!='':
#         print(string)
#         print('-'*len(string))
#         string= input("Please type in a string: ")

#     elif string=='':
#         break
    

    # while True: 
    # string= input('Please type in a string: ')
    # if string=='':
    #     break
    # else: 
    #     print(string)
    #     print('-'*len(string))

# string=input('Please type in a string')
# ast=20-len(string)
# if len(string)<20:
#     print((ast*'*')+string)
# else: 
#     print(string)

# word=input('word ')
# frame_width=30
# padding_tot=30-2-len(word)
# left= padding_tot//2
# right=padding_tot-left

# le= ' '* left
# ri= ' '*right


# print(frame_width*'*')
# print('*'+le+word+ri+'*')
# print(frame_width*'*')


# index=0
# string=input('Please type in a string: ')
# while index<=len(string):
#     print(string[0:index])
#     index+=1

# string=input('Please type in a string: ')
# index=len(string)-1
# while index>=0:
#     print(string[index:])
#     index-=1

# letter = ['a', 'o', 'e']
# string = input('Please type in a string: ')
# while True:
#     for l in letter:
#         if l in string:
#             print(f"{l} found")
#         else:
#             print(f"{l} not found")
#     break


# number = int(input("Please type in a number: "))

# i = 1
# while i <= number:
#     if i + 1 <= number:
#         print(i + 1)
#     print(i)
#     i += 2