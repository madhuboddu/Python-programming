repete = True

while(repete == True):

    year = int(input("Enter a number"))

    leap = False

    if (year % 4 ) == 0 :
        if(year % 100 ) == 0 :
            if(year % 400 ) == 0 :
             print("its a leap year ")
            else :
             print("Its not a leap year")
        else:
         print("Its a leap year")
    else :
     print("its not a leap year")


    print("********************************************")


    rep = input("wish to try again ?????   Y or N")


    if(rep == 'y' or rep == 'Y'):
            repete = True
    else:

        repete = False


print("Thanks for playing")



