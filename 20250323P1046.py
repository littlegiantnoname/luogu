apples_dis=[int(i) for i in list((input().split()))]
hand_dis=int(input())
cnt=0
for i in range(len(apples_dis)):
    if(30+hand_dis>=apples_dis[i-1]):
        cnt+=1
print(cnt)

