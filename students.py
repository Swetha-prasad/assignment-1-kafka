import mysql.connector

mydb=mysql.connector.connect(host = 'localhost', user = 'root' , password = '' ,database= 'studentdb')

mycursor=mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add student')
    print('2 view all students')
    print('3 search a student')
    print('4 update the student')
    print('5 delete a student')
    print('6 exit')

    choice =int(input('enter an option: '))
    if(choice==1):
        print('student enter selected')
        name = input('enter the name')
        admno = input('enter the admissionnumber')
        college = input('enter the college name')
        rollnumber = input('enter the rollnumber')
        sql ='INSERT INTO `students`(`name`, `rollnumber`, `admno`, `college`) VALUES (%s,%s,%s,%s)'
        data = (name,rollnumber,admno,college)
        mycursor.execute(sql,data)
        mydb.commit()

    elif(choice==2):
        print('view student')  
        sql = 'SELECT * FROM `students`'
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        
        print('search a student')  
        adm = input("enter the admission number:")
        sql = 'SELECT `id`, `name`, `rollnumber`, `admno`, `college` FROM `students` WHERE admno = +add'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice==4):
        print('update the student')
        admnum = input("enter the admission number:")
        name = input('enter name to be updated:')
    
        college = input('enter the college name to be updated:')
        rollnumber = input('enter the rollnumber to be updated:')
        sql = "UPDATE `students` SET `name`='"+name+"',`rollnumber`='"+rollnumber+"',`admno`='"+admno+"',`college`='"+college+"' WHERE admno =" +admnum
        mycursor.execute(sql)
        mydb.commit()
        print("updated successfully.")
    elif(choice==5):
        print('delete the student') 
        adm = input("enter the admissionnumber:")
        sql = 'DELETE FROM `students` WHERE `admno`= +adm'
        mycursor.execute(sql)
        mydb.commit()
    elif(choice==6):
        break               
