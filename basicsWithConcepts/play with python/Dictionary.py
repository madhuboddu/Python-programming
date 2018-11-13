



dictionary1 = {'madhu': {'name':'madhu','phone':9493088624,'email':'b.madhu199@gmail.com','grade':'A'},
               'vishnu': {'name':'vishnu','phone':9000466766,'email':'y.vishnu55@gmail,com','grade': 'A+'},
               'manu': {'name':'Manohar','phone':9847720475,'email':'b.manu99@gmail.com','grade': 'A'}
               }





print(dictionary1.get(input("enter a name to get details")))


dictionary1.update('majoj' : {'name':'manoj','phone':9843420475,'email':'b.manoj199@gmail.com','grade': 'A'})





for name in dictionary1:
    print("{} ':' {} ".format( name ,dictionary1[name] ))



