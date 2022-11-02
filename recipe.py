import mysql.connector



mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'recepedb')

mycursor = mydb.cursor()
while True:



    print("select an option from the menu")



    print("1 add recipename")



    print("2 view all recipes")  



    print("3 search a recipe")



    print("4 update the recipe")    



    print("5 delete a recipe")
    print("6 exit")




    choice = int(input('enter an option:'))



    if(choice==1):



        print('recipename enter selected')

       

       

       



        



        recipename = input('enter the recipename')



        category = input('enter the category ')



        taste = input('enter the taste')
        description = input('enter the description')

       

        price = input('enter the price')

       

        

       

        
        sql ='INSERT INTO `recepe`(`recipename`, `category`, `taste`, `description`, `price`)  VALUES (%s,%s,%s,%s,%s)'
        data = (recipename,category,taste,description,price)
        mycursor.execute(sql , data)


        mydb.commit()
    elif(choice==2):



        print('view recipename')



    elif(choice==3):



        print('search recipe')



    elif(choice==4):



        print('update recipe')



    elif(choice==5):



        print('delete recipe')



    elif(choice==6):



        break    
