near=[
    (-1,-1,0),(-1,0,-1),(0,-1,-1),
    (-1,0,0),(0,-1,0),(0,0,-1),
    (-1,0,1),(0,-1,1),(-1,1,0),(0,1,-1),(1,0,-1),(1,-1,0),
    (1,0,0),(0,1,0),(0,0,1),
    (1,1,0),(1,0,1),(0,1,1)
]

next=[
    (1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)
]

def val1(tmpt,list):
    ans=0
    type=1
    for (x,y,z) in list:
        if tmpt[x][y][z] == type:
            for (i,j,k) in next:
                cntt=0
                cnt0=0
                for d in range(0,6):
                    if x+d*i<11 and y+d*j<11 and z+d*k<11 :
                        tmp=tmpt[x+i*d][y+j*d][z+k*d]
                        if tmp == -type :
                            break
                        elif tmp == type:
                            cntt=cntt+1
                        else :
                            cnt0=cnt0+1
                        if cntt == 5:
                            break
                        if cnt0 == 2:
                            break
                if cntt == 2 and cnt0>0 :
                    ans=ans+1
                    if cnt0 == 2:
                        ans=ans+1
                if cntt == 5 and cnt0 == 0 :
                    ans=ans+100000
                if cntt == 3:
                    ans=ans+10
                    if cnt0 == 2:
                        ans=ans+20
                if cntt >= 4:
                    ans=ans+20
                    if cnt0 == 2:
                        ans=ans+1000
        if tmpt[x][y][z] == -type:
            for (i,j,k) in next:
                cntt=0
                cnt0=0
                for d in range(0,6):
                    if x+d*i<11 and y+d*j<11 and z+d*k<11 :
                        tmp=tmpt[x+i*d][y+j*d][z+k*d]
                        if tmp == type :
                            break
                        elif tmp == -type:
                            cntt=cntt+1
                        else :
                            cnt0=cnt0+1
                        if cntt == 5:
                            break
                        if cnt0 == 2:
                            break
                if cntt == 2 and cnt0>0 :
                    ans=ans-2
                    if cnt0 == 2:
                        ans=ans-2
                if cntt == 5 and cnt0 == 0 :
                    ans=ans-200000
                if cntt == 3:
                    ans=ans-20
                    if cnt0 == 2:
                        ans=ans-40
                if cntt >= 4:
                    ans=ans-20
                    if cnt0 == 2:
                        ans=ans-2000
    return ans

def dfs(tmpt,deepth,alpha,beta):
    ableToMove=[]
    haveChess=[]
    for x in range(0,11):
        for y in range(0,11):
            for z in range(0,11):
                if table[x][y][z] != 0 :
                    haveChess.append((x,y,z))
                    continue
                for (i,j,k) in near:
                    nx=x+i
                    ny=y+j
                    nz=z+k
                    if nx>10 or nx<0:continue
                    if ny>10 or ny<0:continue
                    if nz>10 or nz<0:continue
                    if table[nx][ny][nz] != 0 :
                        ableToMove.append((x,y,z))
                        break
    if deepth == T:
        return ((),val1(tmpt,haveChess))
    anspoint=(0,0,0)
    ans=val1(tmpt,haveChess)
    if deepth % 2 == 0:
        beta=max(beta,ans)
    else :
        alpha=min(alpha,ans)
    for (x,y,z) in ableToMove :
        tval=0
        if deepth % 2 == 0 :
            tmpt[x][y][z] = 1
            tval=dfs(tmpt,deepth+1)[1]
            tmpt[x][y][z] = 0
            if tval > ans:
                ans=tval
                anspoint=(x,y,z)
                beta=max(beta,tval)
        else :
            tmpt[x][y][z] = -1
            tval=dfs(tmpt,deepth+1)[1]
            tmpt[x][y][z] = 0
            if tval < ans:
                ans=tval
                anspoint=(x,y,z)
                alpha=min(alpha,tval)
        if alpha <= beta :
            break
    return (anspoint,ans)



def nextstep(otable,t):
    # global wFile
    # wFile=open("output.txt","w")
    global table
    table = otable
    global T
    # table=np.array(otable,dtype=int)
    # table.shape=(11,11,11)
    point=dfs(table,0,2147483647,-2147483648)[0]
    # wFile.close()
    return point
