# print
# print("I am KING M")
# print(" I do know you so tell me about yourself?")
# num=5 
# num2=6
# print(        print("type in a valued reason why you where not here for your exam")'the sum is ',num+num2)
# num1=int(input("please enter your number for a prize!"))
# print("your prize is ", num1)
# num2=int(input("please write down your second number for the prize!!!"))
# print("the sum of your prizes is ", num1 + num2)
# name= input('Enter your name please')
# print(name)
# num=2125
# print(float(num))
# amount=int(input("please enter amount for PRIZE!!!!"))
# not1=amount//100
# not2=(amount%100)//50
# not3=((amount%100)%50)//10
# print("the not for 100 and ",not1)
# print("the not for 50 and!!",not2)
# print("the not for 10 and!!",not3)
# initial_cost=float(input("please enter your initial cost of this product"))
# selling_cost=float(input("please enter your selling cost for this product"))
# if selling_cost>initial_cost:
#     print('the selling price and the buying price is ',initial_cost,selling_cost)
#     profit=selling_cost-initial_cost
#     print("your total profit is",profit)
# else:
#     print("oops! seems like you have gotten lost")    
# print("think of any animal and i myself shall try gussing what that animal is!")
# has_4_legs=input("does it have four legs or not?(yes/no)").lower()
# is_it_an_pet=input("is it usually kept as a pet?(yes/no)").lower()
# can_fly=input('can it fly?(yes/no)').lower()
# if has_4_legs=="yes" and is_it_an_pet=="yes":
#     print("this is a dog or a cat try again human")
# elif has_4_legs=="yes" and is_it_an_pet=="no":
#     print("this cannot be anything other than a wild animal or a specific human")
# elif can_fly=="yes" and is_it_an_pet=="yes":
#     print("this can be a bird ")
# else:
#     print("I could could not guess i guess we aliens have underestimated humans we should cease this war ")
#     print("thank you for playing and wathing my short film it took a while to make")
# art_vetran_course=input("where you doing your art if not no if yes yes!(yes/no)")
# art_skills=int(input("your level of art is...0-1000"))
# if art_vetran_course=="yes":
#     print("You have now passed the test! We are proud of you!")
# else:
#     if art_skills <=100:
#         print("you have not passed the test sadly because your art skill was lower than 100")
# #     else:
# num=int(input("please enter a number"))
# sum=0
# for i in range (1,num+1):
#     sum+=i
#     print("\nsum = ",sum)
# string=input("please enter your string ")
# string2=("")
# for i in string:
#     string2=i+string2
# print("\n the original string= ",string)
# print("\n the reverse string is= ",string2)
# num=int(input("enter the value of a number "))
# sum=5
# i=1
# while i <=num:
#     sum+=i
#     i+=1
# print("\nsum=",sum)
# import random
# secret_number=random.randint(1,10)
# guess=None
# print("welcome to my games with squids SQUID GAME")
# print("guess a squid betwen 1 to 10 HHAHAHHAHHAHAHA")
# while guess != secret_number:
#     guess=int(input("ENTER A GUESS ANY GUESS!(1 TO 10)"))
#     if guess<secret_number:
#         print("too low you should try again HAHAHAHA")
#     elif guess >secret_number:
#         print('too high you bum try again')
#     else:
#         print('you passed now go back to your family :(')
string=input("enter  a word...")
char=input("please enter your character")
i=0
count=0 
while(i<len(string)):
    if(string[i]==char):
        count+=1
    i+=1
print("the total number of times ",char," has occured = ",count )