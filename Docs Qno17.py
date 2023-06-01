# Q17. Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )

def vote():
    age=int(input("enter your age?"))
    if age>=18:
        print("you are available to vote")
    else:
        print("sorry! you need to wait you can't vote😒🙏🙏")
vote()