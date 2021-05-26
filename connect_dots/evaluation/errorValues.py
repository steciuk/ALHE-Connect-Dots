import numpy as np

def distance2D(line, point, score):
  licznik = np.abs(line[0]*point[0] + line[1]*point[1] + line[2] - score)
  mianownik = np.sqrt(line[0]**2 + line[1]**2)
  return licznik/mianownik

def calcError(line, point, score):
  s = 0
  for i in range(len(point)):
    s += line[i] * point[i]
  s += line[-1]
  return np.sqrt( (score - s)**2 )

def distance_ND(line, pts, l0=None, p0=None):
    """
    line defined between l0 and line 
    points defined between p0 and pts
    """
    # line origin other than (0,0,0,..)
    if l0 is not None:
        line = line-l0
    # points origin other than (0,0,0,..)
    if p0 is not None:
        pts = pts-p0
    dp = np.dot(pts,line)
    pp = dp/np.linalg.norm(line)
    pn = np.linalg.norm(pts, axis=1)
    return np.sqrt(pn**2 - pp**2)

def calcDistance(lin, point, score):
  if len(lin) != 3 and len(point) != 2:
    return distance2D(lin, point, score)
  else:
    """
    To powinno dzialac, ale cos jest nie tak. Nie wiem, egzamin z algebry pisalem dwa razy xd

    p1 = [1]*len(point)
    p2 = [2]*len(point)
    s1 = s2 = 0
    for i in range(len(point)):
      s1 += p1[i] * lin[i]
      s2 += p2[i] * lin[i]
    p1.append(lin[-1] + s1)
    p2.append(lin[-1] + s2)
    newPoint = list(point)
    newPoint.append(score)
    return distance_ND(line=np.transpose([p2]), pts=np.array([newPoint]), l0=np.transpose([p1]))
    """
    return -1
