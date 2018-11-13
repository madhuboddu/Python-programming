a = lambda x : x**2


doit = 1



while doit == 1 :

    inputs = int(input("Enter the value to find the square...  : "))

    print("The square of the number is : {}".format(a(inputs)))


    choice = int(input("press 1 to continue and 0 to exit !!!!!"))

    if choice == 1 :
        doit = 1
    else :
        doit = 0


print("Thanks for playing the game")



