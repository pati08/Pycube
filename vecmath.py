def crossproduct(vec1,vec2):

  return (
    vec1[1]*vec2[2]-vec1[2]*vec2[1],
    vec1[2]*vec2[0]-vec1[0]*vec2[2],
    vec1[0]*vec2[1]-vec1[1]*vec2[0])

def subtract(vec1,vec2):
  return (
    vec1[0]-vec2[0],
    vec1[1]-vec2[1],
    vec1[2]-vec2[2])

def dotprod(vec1,vec2):
  return (
    vec1[0]*vec2[0]+
    vec1[1]*vec2[1]+
    vec1[2]*vec2[2])

def trianglearea(p1,p2,p3):
  return 0.5 * abs((p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])))

def raycollison(origin,point,face,getintersect=False):
  """
  origin: (x,y,z) at the end of the ray
  point: (x,y,z) other end of the ray for direction
  face: ((x,y,z),()...) face that the ray might hit
  output: -> Bool
  """

  if type(face[-1]) != type([]):
    face = face[0]

  n = crossproduct(subtract(face[1],face[0]),subtract(face[2],face[0]))


  denom = dotprod(n,subtract(point,origin))
  if denom == 0:
    if getintersect:
      return False,(0,0,0)
    else: 
      return False

  t= dotprod(n,subtract(face[0],origin))/denom
  if t < 0:
    if getintersect:
      return False,(0,0,0)
    else: 
      return False

  intersect = [origin[i] + t * (point[i] - origin[i]) for i in range(3)]

  total_area = trianglearea(face[0], face[1], face[2]) + trianglearea(face[0], face[2], face[3])
  area_sum = (
      trianglearea(intersect, face[0], face[1])+
      trianglearea(intersect, face[1], face[2])+
      trianglearea(intersect, face[2], face[3])+
      trianglearea(intersect, face[3], face[0]))

  if getintersect:
    return round(total_area,7)==round(area_sum,7),intersect
  else: 
    return round(total_area,7)==round(area_sum,7)

def followline(point1,point2,distance):
  """
  takes a line given by two points and follows it a given distance, returning the point that it reaches.

  point1 and point2 are lists or tuples (x,y,z)
  distance is a float that determines how far from the closest point you a going
  distance of 0 is at point 1
  distance of 1 is at point 2
  distance of 2 makes point 2 the midpoint between 0 and 1
  """
  distance = distance*(point2[0]-point1[0])+point1[0]

  return [distance,
          ((distance-point1[0])/(point2[0]-point1[0]))*(point2[1]-point1[1])+point1[1],
          ((distance-point1[0])/(point2[0]-point1[0]))*(point2[2]-point1[2])+point1[2]]

def pointbetweenfaces(point1,point2,point3):
  """
  returns a bool based on if point 3 lies between the prallel faces that point1 and point2 make
  """
  return ((
  (((point2[1]-point1[1])*(point3[1]-point1[1])+(point2[2]-point1[2])*(point3[2]-point1[2]))/-(point2[0]-point1[0]))+point1[0]) < (
    point3[0]) < (
  (((point1[1]-point2[1])*(point3[1]-point2[1])+(point1[2]-point2[2])*(point3[2]-point2[2]))/-(point1[0]-point2[0]))+point2[0])) or (
  (
  (((point1[1]-point2[1])*(point3[1]-point2[1])+(point1[2]-point2[2])*(point3[2]-point2[2]))/-(point1[0]-point2[0]))+point2[0]) < (
    point3[0]) < (
  (((point2[1]-point1[1])*(point3[1]-point1[1])+(point2[2]-point1[2])*(point3[2]-point1[2]))/-(point2[0]-point1[0]))+point1[0]))
