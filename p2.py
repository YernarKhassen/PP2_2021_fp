a = list(map(int,input().strip().split()))
cnt = 0
for i in a:
    if i:
        print(i)
    else:
        cnt+=1
while cnt >0:
    print(0)
    cnt-=1