near=[
    (-1,-1,0),(-1,0,-1),(0,-1,-1),
    (-1,0,0),(0,-1,0),(0,0,-1),
    (-1,0,1),(0,-1,1),(-1,1,0),(0,1,-1),(1,0,-1),(1,-1,0),
    (1,0,0),(0,1,0),(0,0,1),
    (1,1,0),(1,0,1),(0,1,1)
]

next=[
    (1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,-1,0),(1,0,-1),(0,1,-1)
]

def val1(tmpt,list):
    ans=0
    type=1
    p1=1
    p2=2
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
                    ans=ans+1*p1
                    if cnt0 == 2:
                        ans=ans+1*p1
                if cntt == 5 and cnt0 == 0 :
                    ans=ans+100000*p1
                if cntt == 3:
                    ans=ans+10*p1
                    if cnt0 == 2:
                        ans=ans+20*p1
                if cntt >= 4:
                    ans=ans+20*p1
                    if cnt0 == 2:
                        ans=ans+1000*p1
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
                    ans=ans-1*p2
                    if cnt0 == 2:
                        ans=ans-1*p2
                if cntt == 5 and cnt0 == 0 :
                    ans=ans-100000*p2
                if cntt == 3:
                    ans=ans-10*p2
                    if cnt0 == 2:
                        ans=ans-20*p2
                if cntt >= 4:
                    ans=ans-20*p2
                    if cnt0 == 2:
                        ans=ans-1000*p2
    return ans

#相比原ai.py，对棋盘进行了多步搜索，由于可以多步，按理说不需要ai.py中的相应的权值不同的做法
#但是，在实际操作中，发现了权值变化会导致无法使用alpha_beta剪枝，因此采取了只走奇数步的做法、
#该算法仍然可以进行优化
def dfs(tmpt,deepth,alpha=2147483647,beta=-2147483648):
    ableToMove=[]
    haveChess=[]
    for x in range(0,11):
        for y in range(0,11):
            for z in range(0,11):
                if tmpt[x][y][z] != 0 :
                    haveChess.append((x,y,z))
                    continue
                for (i,j,k) in near:
                    nx=x+i
                    ny=y+j
                    nz=z+k
                    if nx>10 or nx<0:continue
                    if ny>10 or ny<0:continue
                    if nz>10 or nz<0:continue
                    if tmpt[nx][ny][nz] != 0 :
                        ableToMove.append((x,y,z))
                        break
    if deepth == T*2-1:
        return ((),val1(tmpt,haveChess))
    anspoint=(0,0,0)
    ans=val1(tmpt,haveChess)
    for (x,y,z) in ableToMove :
        tval=0
        if deepth % 2 == 0 :
            tmpt[x][y][z] = 1
            tval=dfs(tmpt,deepth+1,alpha,beta)[1]
            tmpt[x][y][z] = 0
            if tval > ans:
                ans=tval
                anspoint=(x,y,z)
                beta=max(beta,tval)
        else :
            tmpt[x][y][z] = -1
            tval=dfs(tmpt,deepth+1,alpha,beta)[1]
            tmpt[x][y][z] = 0
            if tval < ans:
                ans=tval
                anspoint=(x,y,z)
                alpha=min(alpha,tval)
        if alpha <= beta :
           break
    return (anspoint,ans)



def nextstep(otable,t):
    global T
    T=t
    #alpha和beta值初始设为极大和极小
    point=dfs(otable,0,2147483647,-2147483648)[0]
    return point

if __name__ == '__main__':
    rFile = open("tmp.txt","r")
    global wFile 
    wFile = open("output.txt","w")
    tmpstr = rFile.read()
    tmplist = tmpstr.split("|")
    anslist = []
    for i in tmplist :
        tlist = []
        ttlist = i.splitlines()
        for j in ttlist :
            tplist = []
            tttlist = j.split()
            for k in tttlist :
                tplist.append(int(k))
            tlist.append(tplist)
        anslist.append(tlist)
    print(nextstep(anslist,2),file=wFile)
    rFile.close()
    wFile.close()
        
    
