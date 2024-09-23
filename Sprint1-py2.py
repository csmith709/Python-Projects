#Written by Charity Smith
#Started on 22 Oct
#Finished 23 Oct
#Group 6

#Fun Interview Question
#Fizz Blizz Loop

for FizzBlizz in range (0,101):
    if FizzBlizz % 5 == 0 and FizzBlizz % 8 == 0:
        print("FizzBlizz")
    elif FizzBlizz % 5 == 0:
        print ("Fizz")
    elif FizzBlizz % 8 == 0:
        print ("Blizz")
    else:
        print(FizzBlizz)