length,numbers=input().split()


length=int(length)
numbers=int(numbers)
trees=[]
no_trees=[]


for i in range(length+1):
    no_trees.append(True)
    
for i in range(numbers):
    trees.append(list(input().split()))
    
for i in range(len(trees)):
    for j in range(int(trees[i][0]),int(trees[i][1])+1):
        no_trees[j]=False
        
for i in range(length+1):
    if(no_trees[i]==True):
        cnt+=1
        
print(cnt)