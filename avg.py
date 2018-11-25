count=1 # if count=0 there is a chance to devide by zero
total=0
score=0
num=-9
score=int(input("Enter a score: "))
while score!=num:
    score=int(input("Enter a score: "))
    count+=1
    total=total+score
print("Average is " ,total/count)

    
    
