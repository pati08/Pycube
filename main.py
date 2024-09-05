import math
import pygame
import random

from vecmath import *
from CreateFaces import CreateFaces
"""
[ or ] to change Fov
Scroll to zoom
Hold right click to rotate 
Left click an button to turn a face
r to scramble
WASDQE also rotates the cube
, or . to change the size of the cube
f to print the framerate to console
L to enable debug thing that looks kinda cool
O or P to adjust drag
"""

screen_width, screen_height = (600,600)
#changes the window size

cubesize = 3
#changes the width in pieces

sensitivity = 100.0
#higher = slower
#changes how much the cam rotates with the mouse

turn_rate = 9
#changes how many degrees per frame they are turned

drag = 1.0
# 0<=drag<1. anything outside this ange will cause sillyness

gap = 0.00
#changes the gap between faces, reccomended 0 to 0.1

#dont changes anything below unless you know what you're doing
pygame.init()
pygame.display.set_caption('Cube')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
Main = pygame.Surface((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
Brack_pressed = False
F_pressed = False
comma_pressed = False
period_pressed = False
r_pressed = False

Fov = 1000.0
Zoom = 10.0
degrees_to_turn=0
z_rotation,y_rotation,x_rotation=0,0,0 #how much the cube is turning, for momentum
rotation_direction = (0,0,0) #the point that the cube is roating about


def RenderScreen(Faces):
  Faces = sorted(Faces, key=lambda x: distance3D((x[0][4]),(Fov,0,0)),reverse=True)
  for face in Faces:
    RenderPoly(face[0], face[1],button=face[3],another=face[2])

def RenderPoly(Polygon, color=(0, 0, 0),button=False,another=0):
  """
  Input a list of (x,y,z) points and (r,g,b) color
  """
  points = []

  for Point in Polygon[0:4]:
    points.append(ToScreenCoords(Point))
  if button and another >= 0:
    pygame.draw.polygon(screen, color, points,5)
  elif another >= 0:
    pygame.draw.polygon(screen, color, points)

def ToScreenCoords(Point2):
  """
  Input the point in (x,y,z)
  optionally the Fov of the cam and Zoom
  """
  Value = (Fov * (Zoom/100) - Fov) / (Point2[0] - Fov)
  return ((Value * (Point2[1])) + screen_width / 2,
          -(Value * (Point2[2])) + screen_height / 2)

def distance3D(point1, point2):
  return ((point1[0] - point2[0])**2) + ((point1[1] - point2[1])**2) + (
      (point1[2] - point2[2])**2)

def RotateShape(Shape, axis, degrees):
  """
  the shape as a list of points (x,y,z) 
  the axis to rotate on "x" "y" or "z"
  the radians to rotate by, can use math.pi 
  """
  strtocoord = {
    "x":[1,0,0],
    "y":[0,1,0],
    "z":[0,0,1]}

  if isinstance(axis,str):
    axis = strtocoord[axis]
  axis = list(axis)

  OutputShape = []

  mult = 1/(math.sqrt(axis[0]**2+axis[1]**2+axis[2]**2))

  axis[0]=axis[0]*mult
  axis[1]=axis[1]*mult
  axis[2]=axis[2]*mult

  cosin = (1-math.cos(math.radians(degrees)))
  coth = math.cos(math.radians(degrees))
  sith = math.sin(math.radians(degrees))
  for point in Shape:
    out = [0,0,0]
    out[0]=(point[0]*(coth+(axis[0]**2)*cosin)+
            point[1]*(axis[0]*axis[1]*cosin-axis[2]*sith)+
            point[2]*(axis[0]*axis[2]*cosin+axis[1]*sith))

    out[1]=(point[0]*(axis[0]*axis[1]*cosin+axis[2]*sith)+
            point[1]*(coth+(axis[1]**2)*cosin)+
            point[2]*(axis[1]*axis[2]*cosin-axis[0]*sith))

    out[2]=(point[0]*(axis[0]*axis[2]*cosin-axis[1]*sith)+
            point[1]*(axis[1]*axis[2]*cosin+axis[0]*sith)+
            point[2]*(coth+(axis[2]**2)*cosin))   

    OutputShape.append(out)
  return OutputShape

Faces = CreateFaces(size=cubesize,pixelWidth=screen_width/2,gap=gap)

#does the starting rotation so it looks better and fixes some errors with it being perfectly aligned on (0,0,0)
for face in Faces:
  face[0] = RotateShape(face[0], "z", 145)
  face[0] = RotateShape(face[0], "y", -45)
  face[0] = RotateShape(face[0], "x", 45)

while running:
  Faces = sorted(Faces, key=lambda x: distance3D((x[0][4]),(Fov,0,0)),reverse=False)

  #shows how the faces are sorted if l is pressed
  #change the size to fix
  if pygame.key.get_pressed()[pygame.K_l]:
    color = -1
    for face in Faces:
      color+=1

      face[1]=(255*color/len(Faces),255*color/len(Faces),255*color/len(Faces))
      # face[1]=(max(min(255,510*color/len(Faces)-250),0),max(min(255,510*color/len(Faces)-250),0),max(min(255,510*color/len(Faces)-250),0))

  #randomization logic
  if pygame.key.get_pressed()[pygame.K_r] and not r_pressed:
    r_pressed = True
    for i in range (5):
      for face in Faces:
        if random.random()<.1 and face[3] and face[2]==-1:
          point1 = followline(face[0][0],face[0][1],1.8)
          point2 = followline(face[0][1],face[0][0],1.8)
          for face in Faces:
            if face[2] == 0 and pointbetweenfaces(point1,point2,face[0][4]):
              face[2] = 1
          rotation_direction = subtract(point1,point2)
          for face in Faces:
            if face[2] == 1:
              face[0] = RotateShape(face[0],rotation_direction,90)
              face[2] = 0
  elif r_pressed and not pygame.key.get_pressed()[pygame.K_r]:
    r_pressed = False

  #turn face logic
  if pygame.mouse.get_pressed()[0] and not degrees_to_turn and not aready_turned:
    gx,gy = pygame.mouse.get_pos()
    if gx-screen_width/2 == 0 : gx+=1
    if gy-screen_height/2 == 0: gy+=1

    i= -1

    for face in Faces:
      if raycollison((Fov,0,0),(Fov*Zoom/100, gx-screen_width/2,-gy+screen_height/2),face[0]) and not (face[3] and face[2] == 0):
        if face[3] and face[2] == -1:
          point1 = followline(face[0][0],face[0][1],1.8)
          point2 = followline(face[0][1],face[0][0],1.8)
          for face in Faces:
            if face[2] == 0 and pointbetweenfaces(point1,point2,face[0][4]):
              face[2] = 1
          rotation_direction = subtract(point1,point2)
          degrees_to_turn= 90
          aready_turned = True
        break
  if not pygame.mouse.get_pressed()[0]:
    aready_turned = False

  #turn animation logic
  if degrees_to_turn:
    degrees_to_turn-=turn_rate
    for face in Faces:
      if face[2] == 1:
        face[0] = RotateShape(face[0],rotation_direction,turn_rate)
    if degrees_to_turn == 0:
      for face in Faces:
        if face[2] == 1:
          face[2] = 0

  #cube size changing logic
  if pygame.key.get_pressed()[pygame.K_COMMA] and not comma_pressed:
    if cubesize>1:
      cubesize, Faces, comma_pressed = cubesize-1, CreateFaces(cubesize-1,gap=gap), True
      for face in Faces:
        face[0] = RotateShape(face[0], "z", 145)
        face[0] = RotateShape(face[0], "y", -45)
        face[0] = RotateShape(face[0], "x", 45)
  elif comma_pressed and not pygame.key.get_pressed()[pygame.K_COMMA]: 
    comma_pressed = False
  if pygame.key.get_pressed()[pygame.K_PERIOD] and not period_pressed:
    cubesize, Faces, period_pressed = cubesize+1, CreateFaces(cubesize+1,gap=gap), True
    for face in Faces:
      face[0] = RotateShape(face[0], "z", 145)
      face[0] = RotateShape(face[0], "y", -45)
      face[0] = RotateShape(face[0], "x", 45)
  elif period_pressed and not pygame.key.get_pressed()[pygame.K_PERIOD]:
    period_pressed = False

  #zoom control and exiting the program
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEWHEEL:
      if   event.y < 0:
        Zoom += 10
      elif event.y > 0:
        Zoom -= 10 

  #allows to check fps
  if pygame.key.get_pressed()[pygame.K_f] and not F_pressed:
    print("fps:", clock.get_fps())
    F_pressed = True
  elif not pygame.key.get_pressed()[pygame.K_f] and F_pressed:
    F_pressed = False

  #fov control
  if pygame.key.get_pressed()[pygame.K_LEFTBRACKET]: Fov *= 0.995
  elif pygame.key.get_pressed()[pygame.K_RIGHTBRACKET]: Fov *= 1.005

  #allows key rotation
  if pygame.key.get_pressed()[pygame.K_q]:x_rotation+=20
  if pygame.key.get_pressed()[pygame.K_s]:y_rotation+=20
  if pygame.key.get_pressed()[pygame.K_d]:z_rotation+=20
  if pygame.key.get_pressed()[pygame.K_e]:x_rotation-=20
  if pygame.key.get_pressed()[pygame.K_w]:y_rotation-=20
  if pygame.key.get_pressed()[pygame.K_a]:z_rotation-=20

  #allows adjusting drag
  if pygame.key.get_pressed()[pygame.K_o]:drag *= 1.1
  if pygame.key.get_pressed()[pygame.K_p]:drag *= 0.9

  #allows mouse rotation
  tz, ty = pygame.mouse.get_rel()
  if pygame.mouse.get_pressed()[2]:
    y_rotation+=ty*1.8
    z_rotation+=tz*1.8

  [rotation_direction] = RotateShape([rotation_direction], "y", y_rotation / sensitivity)
  [rotation_direction] = RotateShape([rotation_direction], "z", z_rotation / sensitivity)
  [rotation_direction] = RotateShape([rotation_direction], "x", x_rotation / sensitivity)

  for face in Faces:
    face[0] = RotateShape(face[0], "y", y_rotation / sensitivity)
    face[0] = RotateShape(face[0], "z", z_rotation / sensitivity)
    face[0] = RotateShape(face[0], "x", x_rotation / sensitivity)

  #slows rotation to create air resistance 
  z_rotation*=drag
  y_rotation*=drag
  x_rotation*=drag

  pygame.display.flip()
  screen.fill((4,0,50))

  RenderScreen(Faces)
  clock.tick(60)


