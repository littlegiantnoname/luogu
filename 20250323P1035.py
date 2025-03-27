k=int(input())
cnt,now=0,0
while True:
    now+=1/(cnt+1)
    if(now>k): 
        print(cnt+1)
        break
    else:
        cnt+=1