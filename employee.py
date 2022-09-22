import pdb
import csv
count=0
while True:
    print("1.Add")
    print("2.Edit")
    print("3.delete")
    print("4.view")
    print("5.Exit")

    choice = int(input("Enter youre choice:"))       
    if choice == 1:
        print('''
        ====================
        Add Employee Details
        ''')
        header = ["Id","FirstName","LastName","Email","phone","addres"]
        # open the csv xfile in the choice 1 and perform write opreation
        with open("emp.csv","r+") as emplyoee:
            # pdb.set_trace()
            empaloye = csv.reader(emplyoee)
            
            # count = 0
            lis = emplyoee.readlines()
            if lis:
                if emplyoee:
                    last=lis[-1]               
                if last:
                    count = last[0] 
            else:
                count=0
                empa = csv.writer(emplyoee,lineterminator="\n")
                empa.writerow(header)
        emplyoee.close()    
    #write the csv file here
        with open("emp.csv","a") as emp:
            write = csv.writer(emp,lineterminator='\n') 
            firstname = input("enter the FirstName:")
            lastname = input("enter the LasttName:")
            email = input("enter the Email:")
            if ('@' in email) and (email.count('@')==1):
                if(email[-4]=='.'): 
                    pass     
                else:
                    print("wrong email enter the @")
            else:
                print("wrong email enter the . ")   
                    
            while True:    
                try:
                    phone = int(input("enter the phone number:"))
                    break
                except ValueError:
                    print("invalid:enter the mobile number")
            address = input("enter the Addres:")  
            chek = input("are you sure wan't to save (y/n):")
            pdb.set_trace()
            
            if chek == "y":
                        write.writerow([int(count)+1,firstname,lastname,email,phone,address])
            if chek =="n":
                    continue
            
        emp.close()       
    elif choice == 2:
        print('''
        ====================
        Edit Employee Details
        ====================
        ''')
        with open("emp.csv","r")as emp:
            read =csv.reader(emp)
            eupdate=[]
            update =input("enter the id for update data:")
            # pdb.set_trace()
            for row in read :
                if  row[0] == str(update):
                    first=input("Enter the FirstName:")
                    if first:
                        row[1]=first
                    first=input("Enter the FirstName:")
                    if first:
                        row[2]=first
                    first=input("Enter the FirstName:")
                    if first:
                        row[3]=first
                    first=input("Enter the FirstName:")
                    if first:
                        row[4]=first
                    first=input("Enter the FirstName:")
                    if first:
                        row[5]=first    
                eupdate.append(row)
        emp.close()
        with open("emp.csv","w")as empl:
            writ = csv.writer(empl,lineterminator='\n')
            writ.writerows(eupdate) 
        empl.close()
    elif choice == 3:
        print('''
        ====================
        Delete Employee Details
        ====================
        ''')
        # to Delete employe data here 
        deleteemp = list()
        deleteinp =input("Enter the id to delete:")
        # read csv file first
        with open("emp.csv","r")as empdelete:
            read =csv.reader(empdelete)
            # pdb.set_trace
            for row in read:
                deleteemp.append(row)
                for data in row:
                    if data == deleteinp:
                        deleteemp.remove(row)
        empdelete.close()
    #    write csv file here 
        with open("emp.csv","w")as ewrite:
            write =csv.writer(ewrite,lineterminator="\n")
            write.writerows(deleteemp)
        ewrite.close()
    elif choice == 4:
        print('''
        ====================
        View Employee Details
        ====================
        ''') 
    #  used for view to two choice
        print("1.show all details")
        print("2.specific details")
        #show the 2 detail all data and specfic data of the employe data  
        choice1 = int(input("enter choice"))
        if choice1 == 1:
                print('''
                    ====================
                    View Employee All Details
                    ====================''')
            #PRINT THE all data of the csv file    
                with open('emp.csv','r')as empshow:
                    empallshow = csv.reader(empshow)
                    for row in empallshow:
                        print(row) 
                # to show all emp detain we call empshowa() function here
        elif choice1 == 2:
                print('''
                ====================
                View Employee specific Details
                ====================''')
    # to show employee specific details we call the showemp() function here
                with open("emp.csv","r")as emp:
                    specificid =csv.reader(emp)
                    id= input ("enter the name for specific detail:")
                    for row in specificid:

                        # print(row)
                        if row[0]==str(id) :
                            print(row)
                    emp.close()  
                  
        else:
            print("invalide choice")
    if choice == 5:
        break
    else:
        print("invalide choice")
