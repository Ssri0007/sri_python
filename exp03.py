import math
def ball_collide(x1,y1,r1,x2,y2,r2):
  distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
  print("Distance between the two balls:",distance)
  r=r1+r2
  print("Sum of radii:",r)
  if distance<=r:
    print("They are collindng")
    return True
  else:
    print("They are not collinding")
    return False
c1=ball_collide(4,4,3,2,2,,3)
print(c1)
c2=ball_collide(100,200,20,200,100,10)
print(c2)

    
