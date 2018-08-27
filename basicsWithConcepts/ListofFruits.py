




fruits = [ ]

fnum = 1
for x in range(5):
        fruits.append(input("fruit name {}  :".format(fnum)))
        fnum += 1

choice =  input("DO YOU WANT TO PRINT THE FRUITS LIST ?")

if choice == 'y':

        for x in fruits:
                print(x)
else :
     print("Thanks")







