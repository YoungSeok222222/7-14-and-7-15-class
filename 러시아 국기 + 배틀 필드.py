# 1873. 상호의 배틀필드
# from collections import deque

# def battle(y,x):   
#     order = deque(input())
#     while order:
#         o = order.popleft()
#         if o=="S" and lst[y][x]=='<':
#             for i in range(W):
#                 dy,dx = y+move[2][0], x+move[2][1]
#                 if 0<=dy<W and 0<=dx<W and lst[dy][dx] !='_' and lst[dy][dx]!='#':
#                     if lst[dy][dx] == '*':
#                         lst[dy][dx] = '.'
#                         break
#                     else: lst[dy][dx] =='.'
            
    


# move = [[-1,0],[1,0],[0,-1],[0,1]]
# T = int(input())
# for tc in range(1,T+1):
#     H,W = map(int,input().split())
#     lst = [list(input()) for _ in range(H)]
#     o = int(input())
    
#     for i in range(H):
#         for j in range(W):
#             if lst[i][j]=="<":
#                 battle(i,j)
#                 break
    
    
# def dfs(idx,cnt):
    

#     for i in range(1,N-1):
        

#     pass
# 4613. 러시아 국기 같은 깃발
T = int(input())
for tc in range(1,T+1):
    N,M= map(int,input().split())
    lst = [list(input()) for _ in range(N)]
    cnt = 0
    for j in range(M):
        if lst[0][j] !='W': cnt +=1
        if lst[-1][j] !='R': cnt +=1
    B,R,W = 0,0,0 
    for i in range(1,N-1):
        for j in range(M):
            if lst[i][j] =="W": W += 1
            if lst[i][j] =="B": B += 1  
            if lst[i][j] =="R": R += 1
    if W>B and W>R: 
        for i in range(1,N-1):
            for j in range(M):
                if i<N-2 and lst[i][j] != 'W': cnt +=1
                if i==N-2 and lst[i][j] !='B': cnt +=1
    elif B>W and B>R:
        for i in range(1,N-1):
            for j in range(M):
                if lst[i][j] !='B': cnt +=1
    elif R>W and R>B:
        for i in range(1,N-1):
            for j in range(M):
                if i==1 and lst[i][j] !='B': cnt +=1
                if i>1 and lst[i][j] !='R': cnt +=1
    print(f"#{tc} {cnt}")

 
     


    

       


