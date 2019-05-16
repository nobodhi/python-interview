import numpy as np

def rotateMatrix(d):
  loops = int(d/2)
  print ("loops {}".format(loops))
  m = np.arange(0,d**2).reshape(d,d) # some randome input
  print (m)

  # loop through the matrix layer by layer
  rows, cols = m.shape
  top = m.copy()[:1]
  right = m.copy()[:,cols-1:]
  bottom = m.copy()[rows-1:,:]
  left = m.copy()[:,:1]

  # loop
  # swap everything out, and assign the new values back into the matrix
  # it flips differently depending on if you are going left or right

  print ("counter clockwise")

  (r,c) = top.shape
  # left
  m[:,:1] = np.flip(top.reshape(top.shape))
  
  (r,c) = left.shape
  # bottom 
  m[rows-1:,:] = left.reshape(c,r)
  
  (r,c) = right.shape
  # top 
  m[:1] = right.reshape(c,r)

  (r,c) = bottom.shape
  # right 
  m[:,cols-1:] = np.flip(bottom.reshape(c,r))

  print ("\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n".format(top,left,bottom,right,m))

  # print ("clockwise")

  # (r,c) = _top.shape
  # right = _top.reshape(c,r)

  # (r,c) = _left.shape
  # top = np.flip(_left.reshape(c,r))

  # (r,c) = _right.shape
  # bottom = np.flip(_right.reshape(c,r))

  # (r,c) = _bottom.shape
  # left = _bottom.reshape(c,r)

  # print ("\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n".format(top,left,bottom,right,m))
