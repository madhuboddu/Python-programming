def ageConverter():
    print("Welcome to AGE CONVERTER")
    choiseAge = input("Enter age in sec (s) or years (y) ")

    if choiseAge == "s":
        rawAge  = input("enter age in seconds")
        convertedAge = int(rawAge)/60/60/24/365
        print("Congrats,You have lived for {} Years"".format(convertedAge))
    elif choiseAge == "y":
        rawAge  = input("enter age in Years")
        convertedAge = int(rawAge) * 60 *60 *24 * 365
        print("Congrats,You have lived for {} Seconds".format(convertedAge))
    else :
        print("Enter a valid choise...! ")

ageConverter()
