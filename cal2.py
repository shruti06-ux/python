def add():
    ans=fn+sn
    print("add=",ans)

def sub():
    ans=fn-sn
    print("sub=",ans)
def mul():
    ans=fn*sn
    print("mul=",ans)
def tdiv():
    ans=fn/sn
    print("tdiv=",ans)
def fdiv():
    ans=fn//sn
    print("fdiv=",ans)
def mod():
    ans=fn%sn
    print("mod=",ans)
def power():
    ans=fn**sn
    print("power=",ans)

while True:
    ch=int(input("\n\nEnter choice:\n1.add\t2.sub\n3.mul\t4.tdiv\n5.fdiv\t6.mod\n7.power\n8.exit\n"))
    if ch==1:
        fn=int(input("enter 1st num:"))
        sn=int(input("enter 2nd num:"))
        add()
    elif ch==2:
        fn=int(input("enter 1st num:"))
        sn=int(input("enter 2nd num:"))
        sub()
    elif ch==3:
        fn=int(input("enter 1st num:"))
        sn=int(input("enter 2nd num:"))
        mul()
    elif ch==4:
        fn=int(input("enter 1st num:"))
        sn=int(input("enter 2nd num:"))
        tdiv()
    elif ch==5:
        fn=int(input("enter 1st num:"))
        sn=int(input("enter 2nd num:"))
        fdiv()
    elif ch==6:
        fn=int(input("enter 1st num:"))
        sn=int(input("enter 2nd num:"))
        mod()
    elif ch==7:
        fn=int(input("enter 1st num:"))
        sn=int(input("enter 2nd num:"))
        power()
    elif ch==8:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
  
