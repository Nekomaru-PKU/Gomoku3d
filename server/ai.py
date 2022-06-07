# code by @rongyiming
# optimized by @nekomaru-pku

# current perf est:
#   python: 2600ms ~ 3200ms
#   pypy:   400ms ~ 550ms

# import numpy as np

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

#val1函数为为当前棋盘估价的估价函数，根据五连，四连，三连等多种情况进行估价
#同时，相同的四连、三连等敌方的权重比我方大，防止为了下出我方四连而忽略对方四连的情况
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

def dfs(tmpt,deepth):
    ableToMove=[]
    haveChess=[]
    #将所有的可以下的位置加入ableToMove的list，将有棋子的位置加入haveChess的list
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
    if deepth == 1:
        return ((),val1(tmpt,haveChess))
    anspoint=(0,0,0)
    #预先将当前棋盘的估价函数作为最低的ans
    #理论上，我方下完棋后，棋盘的估价只会变高不会变低
    ans=val1(tmpt,haveChess)
    #遍历所有可以下的位置，对下完后的棋盘估价（deepth%2为了区分敌我，不过在该程序中只有一步棋，因此无用）
    for (x,y,z) in ableToMove :
        tval=0
        if deepth % 2 == 0 :
            tmpt[x][y][z] = 1
            tval=dfs(tmpt,deepth+1)[1]
            tmpt[x][y][z] = 0
            if tval > ans:
                ans=tval
                anspoint=(x,y,z)
        else :
            tmpt[x][y][z] = -1
            tval=dfs(tmpt,deepth+1)[1]
            tmpt[x][y][z] = 0
            if tval < ans:
                ans=tval
                anspoint=(x,y,z)
    return (anspoint,ans)


#通过调用nextstep函数来进行下一步的计算
def nextstep(otable):
    global table
    table = otable
    #写做dfs事实上只是一个对当前所有可下位置的遍历函数，在alpha_beta版本中才用作搜索
    point=dfs(table,0)[0]
    return point
