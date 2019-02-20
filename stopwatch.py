import time
h=int(input("Enter the hour:"))
m=int(input("Enter the minute:"))
s=int(input("Enter the seconds:"))
hour=00
minutes=00
sec=00
while True:
    if sec<10 and minutes<10 and hour<10:
        print("0",str(hour),":","0",str(minutes),":","0",str(sec))
    elif sec>=10 and minutes<10:
        print("0",str(hour),":","0",str(minutes),":",str(sec))
    elif sec>=10 and minutes>=10 and hour<10:
        print("0",str(hour),":",str(minutes),":",str(sec))
    else:
         print(str(hour),":",str(minutes),":",str(sec))
        
    sec+=1
    if sec==60:
        minutes+=1
        sec=0
    if minutes==60:
        minutes=0
        hour+=1
    if hour==h and minutes==m and sec==s:
        if sec<10 and minutes<10 and hour<10:
            print("0",str(hour),":","0",str(minutes),":","0",str(sec))
        elif sec>=10 and minutes<10:
            print("0",str(hour),":","0",str(minutes),":",str(sec))
        elif sec>=10 and minutes>=10 and hour<10:
            print("0",str(hour),":",str(minutes),":",str(sec))
        else:
            print(str(hour),":",str(minutes),":",str(sec))
        break
    time.sleep(1)
        
