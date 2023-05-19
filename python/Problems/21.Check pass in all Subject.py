print('Result & average are printed')

def check():
       
    total = 0
    p = 0
    i =0
    while(i<=5):
        mark = int(input('Enter Ur mark :'))
        total = total + mark
        if mark >= 50:
            print("you have pased in this subject",i+1)
            p = p +1
        else:
            print("you have failed in subject ",i+1)
        i = i+1
    print("Total Secured in Exam is:",total)

    if (p==5):
        print("You have passed in all Subject")
        print("Your Average in Exam is",total/5)
    else:
        print("You have failed in Exam")



check()
