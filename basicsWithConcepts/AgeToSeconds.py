def ageToSec():
    print("*********************************************")
    print("Welcome to Age Converter..!")
    userAge = input("Enter your AGE : ")
    convertedAge = int(userAge) * 12 * 30 * 24 * 60 * 60
    print("Congrats..!!, You Lived for {} Seconds...".format(convertedAge))
    print("*********************************************")

ageToSec()
