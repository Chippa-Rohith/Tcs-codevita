n=int(input())
holes=list(map(int,input().split(' ')))
m=int(input())
balls=list(map(int,input().split(' ')))
no_balls_can_a_hole_contain=[[i+1,0] for i in range(len(holes))]
no_balls_can_a_hole_contain=no_balls_can_a_hole_contain[::-1]
holes=[(holes[i],i+1) for i in range(len(holes))]
holes=holes[::-1]
ball_positions=[0]*len(balls)
for i in range(len(balls)):
  for j in range(len(holes)):
    if no_balls_can_a_hole_contain[j][1]!=no_balls_can_a_hole_contain[j][0] and balls[i]<=holes[j][0]:
      no_balls_can_a_hole_contain[j][1]+=1
      ball_positions[i]=holes[j][1]
      break

print(ball_positions)    



  
