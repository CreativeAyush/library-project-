import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd="admin",database="library1")
cursor=con.cursor()
print("="*80)
print("                                 AYUSH LIBRARY")
print("="*80)
print("                   Dont  Just  READ  Develop  New  Things||||")
print("-"*80)
print("-"*80)
print("-"*80)
print("THIS SOFTWARE IS PROTECTED BY PASSWORD. SO TAKE PERMISSION FROM AYUSH")
print("-"*80)
print("-"*80)
print("-"*80)
password ="ayushyadav"

for i in range(1000000000000):
    n=input("ENTER THE PASSWORD")
    j=3
    if(n==password):
        print("welcome")
        break
    else:
        print("WRONG-PASSWORD",j-i)
        print("-"*80)
        print("UNAUTHORISED ACCESS")
while True:
    choice=int(input("1->addbook\n2->issuebook\n3->returnbook\n4->deletebook\n5->display\n6->updatebooks\n->enter your choice-"))
    if choice==1:
        name=input("enter name of book")
        regno=input("enter code of book")
        bcode=input("total no of books")
        subject=input("enter subject")
        query="insert into issue values('{}',{},{},'{}')".format(name,regno,bcode,subject)
        cursor.execute(query)
        con.commit()
        print(">"*80)
        print("data entered succesfully")
        print(">"*80)
        print("thanku")
        print(">"*80)
    if choice==2:
        stuname=input("enter name of student")
        regno=input("enter registration no")
        bookcode=input("enter book code ")
        issuedate=input("enter issue date")
        issuebook='insert into issuebook values("{}",{},{},"{}")'.format(stuname,regno,bookcode,issuedate)
        cursor.execute(issuebook)
        con.commit()
        print(">"*80)
        print("book is issued to",stuname)
        print(">"*80)
        print("thanku")
        print(">"*80)
    if choice==3:
        stuname=input("enter name of the student")
        regno=input("enter registration no")
        bookcode=input("enter book code")
        issuedate=input("enter issue date")
        r=input("enter return date")
        t=input("enter todays date")
        query='insert into submit values("{}",{},{},"{}","{}","{}")'.format(stuname,regno,bookcode,issuedate,r,t)
        cursor.execute(query)
        con.commit()
        print(">"*80)
        print("RETURNED SUCCESSFULLY")
        print(">"*80)
        print("="*80)
        print("                         IS THERE ANY FINE ON THIS STUDENT")
        print("="*80)
        print(" enter the value for this month given below for other month charges will be 60 rupees")
        print("="*80)
        n2=int(input("enter todays date-"))
        n=int(input("date to submit book-"))
        a= n2 - n
        if (n2>n):
            print("this student have a fine of--Rs-",a)
            print("------------------------")
        elif (n2<n):
            print("-"*80)
            print("you still have a time to submit")
            print("-"*80)
            print("thanku")
            print(">"*80)
        else:
            print("you dont have any fine")
            print("="*80)
            print("thanku")
            print(">"*80)
    if choice==4:
        name=input("enter name of the book you want to delete")
        query="DELETE FROM issue WHERE name='{}'".format(name)
        cursor.execute(query)
        con.commit()
        print("="*80)
        print("deleted the record")
        print("="*80)
        print("thanku")
        print(">"*80)
    if choice==5:
        name=input("enter name of book you want to see its value")
        query="select * FROM issue WHERE name='{}'".format(name)
        cursor.execute(query)
        data=cursor.fetchone()
        print("="*80)
        print("BOOK DETAILS ARE GIVEN BELOW")
        print("BOOK NAME-",data[0])
        print("REG NO OF BOOK-",data[1])
        print("NO OF BOOKS-",data[2])
        print("SUBJECT OF BOOK-",data[3])
        print("="*80)
        print("thanku")
        print(">"*80)
    if choice==6:
        choice=int(input("1->update-name\n2->update-regno\n3->update-no-of-book\n4->update-subject\n->enter your choice-"))
        if choice==1:
            name=input("enter previous name of book-")
            name1=input("enter new name of book-")
            query="UPDATE issue SET name='{}' WHERE name='{}'".format(name1,name)
            cursor.execute(query)
            con.commit()
            print(">"*80)
            print("data updated succesfully")
            print(">"*80)
            print("thanku")
            print(">"*80)
        if choice==2:
            regno=input("enter previous regno of book-")
            regno1=input("enter new regno of book-")
            query="UPDATE issue SET regno={} WHERE regno={}".format(regno1,regno)
            cursor.execute(query)
            con.commit()
            print(">"*80)
            print("data updated succesfully")
            print(">"*80)
            print("thanku")
            print(">"*80)
        if choice==3:
            regno=input("enter name of book-")
            noofbooks1=input("enter new number of books-")
            query="UPDATE issue SET bcode={} WHERE name='{}'".format(noofbooks1,regno)
            cursor.execute(query)
            con.commit()
            print(">"*80)
            print("data updated succesfully")
            print(">"*80)
            print("thanku")
            print(">"*80)
        if choice==4:
            name=input("enter book regno-")
            name1=input("enter new subject-")
            query="UPDATE issue SET subject='{}' WHERE regno={}".format(name1,name)
            cursor.execute(query)
            con.commit()
            print(">"*80)
            print("data updated succesfully")
            print(">"*80)
            print("thanku")
            print(">"*80)
        
       
        
        
        
    
        
     
        
        
   

        
        
    
        
    
   
        
    
    
    

