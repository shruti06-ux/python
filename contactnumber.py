



import re
contact={}
def show_contact():
    srno=1
    print('srno','', 'mono', 'name')
    for mono,name in contact.items():
        print(srno, '  ', mono, name)
        srno=srno+1
while True:
    ch=int(input("\n\nEnter Choice:\n1.Add Contact\n2.TO Add New Contact\n3.Update Contact\n4.Delete Contact\n5.Show Contact\n6.Exit\n"))
    match ch:
        case 1:
            user=int(input("Enter a size of contactlist you want:"))
            for i in range(user):
                mono=input("Enter a mobile num:")
                a=re.fullmatch('[6-9][0-9]{9}',mono)
                if a!=None:
                    
                    name=input("Enter a name:")
                    contact.update({mono:name})
                else:
                    print('This number is not valid')
                
                
        case 2:
            print("TO ADD NEW CONTACT")
            mono=input("Enter a mobile number to add:")
            a=re.fullmatch('[6-9][0-9]{9}',mono)
            if a!=None:
                
                if mono in contact:
                    print("Mobile num is already exist in your contact,please try again!")
                else:
                    name=input("Enter a name to add:")
                    contact[mono]=name
                    print("CONTACT ADDED!")  
                    
            else:
                print('This number is not valid')
                
            
            
        case 3:
            print("UPDATE CONTACT")
            mono=input("Enter a mobile number to update:")
            a=re.fullmatch('[6-9][0-9]{9}',mono)
            if a!=None:
                 
                 if mono in contact:
                    name=input("Enter a name to update:")
                    contact.update({mono:name})
                    print("CONTACT UPDATED!")
                 else:
                    print("NO SUCH CONTACT TO UPDATE")
                 
            else:
                 print('This number is not valid')
           
        case 4:
            print("DELETE CONTACT")
            mono=input("Enter a mobile number to delete:")
            a=re.fullmatch('[6-9][0-9]{9}',mono)
            if a!=None:
                
                if mono in contact:
                    contact.pop(mono)
                    print("CONTACT DELETED!")
                else:
                    print("Mobile number is not in contact") 
            else:
                print('This number is not valid')
            
        case 5:
            ch1=int(input("\nEnter choice :\n1. SHOW ALL CONTACT\n2.SHOW PARTICULAR CONTACT\n"))
            if ch1==1:
                show_contact()
            elif ch1==2:
                print("SHOW ADDED CONTACT")
                mono=input("Enter a number to show:")
                if mono in contact:
                    print(mono, name)
                else:
                    print("This Contact is not in your list")
            
        
        case 6:
            print("EXITING.....")
            break
        case _:
            print("INVALID CHOICE!")

        


























               
