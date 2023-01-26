# 다시 풀 문제
# 캐릭터의 좌표
def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy
    return [x,y]
  
# 다른 풀이
def solution(keyinput, board):
    now=[0,0]
    stan=abs(board[0])//2 
    stan1=abs(board[1])//2

    for i in keyinput:
        if i == "left" and now[0]-1 >= -stan:
            now[0] -= 1
        elif i == "right" and now[0]+1 <= stan:
            now[0] += 1
        elif i == "up" and now[1]+1 <= stan1:
            now[1] += 1
        elif i == "down" and now[1]-1 >= -stan1:
            now[1] -= 1
    return(now)
