import random #calling library function for get random number
num=random.randint(1,20)#get random number between 1 and 20 ,defind it to num
count=0 #guessing count=0 
while count<=5:#excute this while count<=5
    guesn=int(input("Guess a number between 1 to 20: "))#input an integer for guessing number
    if num!=guesn:#if guesiing number not equal to that generated random number do the following thing
        print("Guessing is Wrong")#print like this
        if num>guesn:
            print("Guessing number is Low")#at the same time guessing number is lower than generated random number print like this
            count+=1#add 1 to count
        if  num<guesn:
            print("Guessing number is High")#at the same time guessing number is Higherthan generated random number print like this
            count+=1#add 1 to count
    else:
        print("Guess is Correct")#if guesiing number  equal to that generated random number 
        count+=1#add 1 to count
        break#break look and exit 
print("You took",count-1,"Times to guess correct Number")
if count>5:#if we took 5 times and didnt guess it corectly show this
    print("You reached maximum number of guessing ,The Correct number is :",num)


        
    
