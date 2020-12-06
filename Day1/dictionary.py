def ret(num):
    dic={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
    11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
    30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',0:''} # this and above 2 lines are actually single line
    return dic[num]

def toText(num,unit):
    n=int(num)
    ans=""
    if n <=20:
        ans= ret(n)
    else:
        ans= ret(n-(n%10))+" "+ret((n%10))
    ans=ans.strip()
    if len(ans)>0:
        return " "+ans+" "+unit
    else:
        return " "

num=input("enter a num: ")
num=str(int(num)) 
while len(num)<9: 
    num="0"+num
ans=toText( num[0:2],"Crore")+toText(num[2:4],"Lakh")+toText(num[4:6],"Thousand")+toText(num[6:7],"Hundred")+toText(num[7:9],"")
print (ans.strip())
