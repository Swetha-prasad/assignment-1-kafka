import mysql.connector



mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'employeedb')

mycursor = mydb.cursor()
while True:



    print("select an option from the menu")



    print("1 add employee")



    print("2 view all employee")  



    print("3 search a employee")



    print("4 update the employee")    



    print("5 delete a employee")
    print("6 exit")



   



    choice = int(input('enter an option:'))



    if(choice==1):



        print('employee enter selected')

       

       

       



        empcode = input('enter the empcode')



        empname = input('enter the empname')



        designation = input('enter the designation ')



        salary = input('enter the salary')
        companyname = input('enter the company name')

       

        phno = input('enter the phn no')

       

        email = input('enter the email')

       

        password = input('enter the password')
        sql ='INSERT INTO `employee`(` `empcode`, `empname`, `designation`, `salary`, `companyname`, `phoneno`, `emailid`, `password`) VALUES ( (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (empcode,empname,designation,salary,companyname,phno,email,password)
        mycursor.execute(sql , data)


        mydb.commit()
    elif(choice==2):



        print('view employee')



    elif(choice==3):



        print('search employee')



    elif(choice==4):



        print('update employee')
        empcode = input('enter the empcode')



        empname = input('enter the empname to be updated')



        designation = input('enter the designation to be updated ')



        salary = input('enter the salary to be updated')
        companyname = input('enter the company name to be updated')

       

        phno = input('enter the phn no to be updated')

       

        email = input('enter the email to updated')

       

        password = input('enter the password to be updated')
        sql = "UPDATE `employee` SET =`empname`='"+empname+"',`designation`='"+designation+"',`salary`='"+salary+"',`companyname`='"+companyname+"',`phoneno`='"+phoneno+"',`emailid`='"+emailid+"',`password`='"+password+"' WHERE `empcode`="+empcode
        mycursor.execute(sql)
        mydb.commit()
        print("updated successfully.")



    elif(choice==5):



        print('delete employee')
        emcode = input("enter the empcode number:")
        sql = 'DELETE FROM `employee` WHERE `empcode`='+empcode
        mycursor.execute()




    elif(choice==6):



        break    

