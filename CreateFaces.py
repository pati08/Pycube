
def permutations(max, min=(0, 0), step=1):
  out = []
  for val1 in range(min[0], max[0], step):
    for val2 in range(min[1], max[1], step):
      out.append([val1, val2])
  return out

def CreateFaces(size=3, pixelWidth=300, colors="base", gap = 0.05):
  """
  size = int for pieces width

  pixelWidth = num of pixels wide the cube is. by default, relies on width

  colors = a tuple of 7 tuples, 
  first being the color of the base cube (set to (-1,-1,-1) for it to be clear),
  base color is broken and i have no plans to fix it
  others being the colors of the faces
  """
  #list of points contains 4 corners then the distance determining point for rendering 
  if colors == "base":
    colors = ((35,35,35), (255, 255, 255), (255, 255, 000), (255, 000, 000),
                            (255, 125, 000), (000, 000, 255), (000, 255, 000))

  W = pixelWidth / 2
  squarewidth = pixelWidth / size

  c = 0

  shapes = []
  squaregap = (pixelWidth * 0.10) / (size)
  butt = .6
  c = 0
  for side in permutations(max=(3, 2)):  #gets the side
    c += 1
    for (x, y) in permutations(
        max=(size, size)):  #gets the 2d coords of the square in the side
      xshift, yshift = (pixelWidth / size) * x, (pixelWidth / size) * y
      DistanceDeterminingPoint = [-W+pixelWidth/size/2+xshift,-W+pixelWidth/size/2+yshift]

      if size != 1: #no buttons on a 1x1
        for i in range (2):
          """
          Please Ignore how horribly the next 120 lines are written. 
          I made these at 2 am last night and am too afraid to try to fix them
          this function runs very rarely so efficiency is not a goal.
          """
          #left
          if   x ==    0 and not(y==0 or y==size-1):
            square =[[[-W + squaregap*1.8 + xshift                   , -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift                   , -W - squaregap*1.8 + squarewidth + yshift],
                      [-W - squaregap*1.8 + xshift + butt*squarewidth, -W - squaregap*1.8 + squarewidth + yshift],
                      [-W - squaregap*1.8 + xshift + butt*squarewidth, -W + squaregap*1.8 + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))
            shapes.append(square)

          #right
          elif x == size-1 and not(y==0 or y==size-1):
            square =[[[-W - squaregap*1.8 + xshift +          squarewidth, -W - squaregap*1.8 + squarewidth + yshift],
                      [-W - squaregap*1.8 + xshift +          squarewidth, -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift + (1-butt)*squarewidth, -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift + (1-butt)*squarewidth, -W - squaregap*1.8 + squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))
            shapes.append(square)

          #bottom
          elif y ==    0 and not(x==0 or x==size-1):
            square =[[[-W - squaregap*1.8 + xshift + squarewidth , -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift               , -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift               , -W - squaregap*1.8 + butt*squarewidth + yshift],
                      [-W - squaregap*1.8 + xshift + squarewidth , -W - squaregap*1.8 + butt*squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))
            shapes.append(square)

          #top
          elif y == size-1 and not(x==0 or x==size-1):
            square =[[[-W + squaregap*1.8 + xshift               , -W - squaregap*1.8 + squarewidth+yshift],
                      [-W - squaregap*1.8 + xshift + squarewidth , -W - squaregap*1.8 + squarewidth+yshift],
                      [-W - squaregap*1.8 + xshift + squarewidth , -W + squaregap*1.8 + (1-butt)*squarewidth + yshift],
                      [-W + squaregap*1.8 + xshift               , -W + squaregap*1.8 + (1-butt)*squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))
            shapes.append(square)

          #top left
          elif y == size-1 and x == 0:
            square =[[[-W + squaregap*1.8 + xshift               , -W - squaregap*1.8 + squarewidth+yshift],
                      [-W - squaregap*1.8 + xshift + squarewidth , -W - squaregap*1.8 + squarewidth+yshift],
                      [-W - squaregap*1.8 + xshift + squarewidth , -W + squaregap*1.8 + (1-butt)*squarewidth + yshift],
                      [-1*(-W + squaregap*1.8 + (1-butt)*squarewidth + yshift), -W + squaregap*1.8 + (1-butt)*squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))

            shapes.append(square)
            square =[[[-W + squaregap*1.8 + xshift                   , -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift                   , -W - squaregap*1.8 + yshift + squarewidth],
                      [-W - squaregap*1.8 + xshift + butt*squarewidth, -1*(-W - squaregap*1.8 + xshift + butt*squarewidth)],
                      [-W - squaregap*1.8 + xshift + butt*squarewidth, -W + squaregap*1.8 + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))
            shapes.append(square)

          #top right 
          elif y == size-1 and x == size-1:
            square =[[[-W + squaregap*1.8 + xshift               , -W - squaregap*1.8 + squarewidth+yshift],
                      [-W - squaregap*1.8 + xshift + squarewidth , -W - squaregap*1.8 + squarewidth+yshift],
                      [-W + squaregap*1.8 + xshift + (1-butt)*squarewidth, -W + squaregap*1.8 + (1-butt)*squarewidth + yshift],
                      [-W + squaregap*1.8 + xshift               , -W + squaregap*1.8 + (1-butt)*squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))

            shapes.append(square)
            square =[[[-W - squaregap*1.8 + xshift +          squarewidth, -W - squaregap*1.8 + squarewidth + yshift],
                      [-W - squaregap*1.8 + xshift +          squarewidth, -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift + (1-butt)*squarewidth, -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift + (1-butt)*squarewidth, -W + squaregap*1.8 + (1-butt)*squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))
            shapes.append(square)

          #bottom right 
          elif y == 0 and x == size-1:
            square =[[[-W - squaregap*1.8 + xshift + squarewidth , -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift               , -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift               , -W - squaregap*1.8 + butt*squarewidth + yshift],
                      [-W + squaregap*1.8 + xshift + (1-butt)*squarewidth, -W - squaregap*1.8 + butt*squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))

            shapes.append(square)
            square =[[[-W - squaregap*1.8 + xshift +          squarewidth, -W - squaregap*1.8 + squarewidth + yshift],
                      [-W - squaregap*1.8 + xshift +          squarewidth, -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift + (1-butt)*squarewidth, -W - squaregap*1.8 + butt*squarewidth + yshift],
                      [-W + squaregap*1.8 + xshift + (1-butt)*squarewidth, -W - squaregap*1.8 + squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))
            shapes.append(square)

          #bottom left 
          elif y == 0 and x == 0:
            square =[[[-W - squaregap*1.8 + xshift + squarewidth     , -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift                   , -W + squaregap*1.8 + yshift],
                      [-W - squaregap*1.8 + xshift + butt*squarewidth, -W - squaregap*1.8 + butt*squarewidth + yshift],
                      [-W - squaregap*1.8 + xshift + squarewidth     , -W - squaregap*1.8 + butt*squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))

            shapes.append(square)
            square =[[[-W + squaregap*1.8 + xshift                   , -W + squaregap*1.8 + yshift],
                      [-W + squaregap*1.8 + xshift                   , -W - squaregap*1.8 + squarewidth + yshift],
                      [-W - squaregap*1.8 + xshift + butt*squarewidth, -W - squaregap*1.8 + squarewidth + yshift],
                      [-W - squaregap*1.8 + xshift + butt*squarewidth, -W - squaregap*1.8 + butt*squarewidth + yshift],
                      DistanceDeterminingPoint[:]],
                      (0,0,0), i-1, True]

            if c == 2 or c == 3 or c == 6:
              temp = square[0][0]
              square[0][0] = square[0][1]
              square[0][1] = temp
              temp = square[0][2]
              square[0][2] = square[0][3]
              square[0][3] = temp

            for corner in square[0]:
              corner.insert(side[0], W * ((side[1] * 2.04) - 1.02))
            shapes.append(square)

      #creates the stickers
      stickgap = (pixelWidth * gap) / (size)
      square = [[[-W + stickgap + xshift, -W + stickgap + yshift],
                 [-W + squarewidth - stickgap + xshift, -W + stickgap + yshift],
                 [-W + squarewidth - stickgap + xshift, -W + squarewidth - stickgap + yshift],
                 [-W + stickgap + xshift, -W + squarewidth - stickgap+ yshift],
                 DistanceDeterminingPoint],
                colors[c], 0,False]

      for corner in square[0]:
        corner.insert(side[0], W * ((side[1] * 2) - 1))
      shapes.append(square)
  return shapes
