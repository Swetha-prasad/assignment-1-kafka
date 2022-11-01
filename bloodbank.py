import mysql.connector



mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'bloodbankdb')

mycursor = mydb.cursor()
while True:



    print("select an option from the menu")



    print("1 add bloodbankname")



    print("2 view all bloodbank")  



    print("3 search a bloodbank")



    print("4 update the bloodbank")    



    print("5 delete a bloodbank")
    print("6 exit")




    choice = int(input('enter an option:'))



    if(choice==1):



        print('bloodbank enter selected')

       

       

       



        



        name = input('enter the name')



        address = input('enter the address ')



        contno = input('enter the contno')
        donarid = input('enter the donarid')

       

        patientid = input('enter the patientid')

       

        bloodgroup = input('enter the blood group')

       

        
        sql ='INSERT INTO `bloodbank`( `name`, `address`, `contno`, `blood group`, `donarid`, `patientid`) VALUES (%s,%s,%s,%s,%s,%s)'
        data = (name,address,contno,bloodgroup,donarid,patientid)
        mycursor.execute(sql , data)


        mydb.commit()
    elif(choice==2):



        print('view bloodbankname')



    elif(choice==3):



        print('search bloodbank')



    elif(choice==4):



        print('update bloodbank')



    elif(choice==5):



        print('delete bloodbank')



    elif(choice==6):



        break    

