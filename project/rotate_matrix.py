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

  # top->left
  (r,c) = top.shape
  m[:,:1] = np.flip(top.reshape(c,r))
  
  # left->bottom 
  (r,c) = left.shape
  m[rows-1:,:] = left.reshape(c,r)
  
  # bottom->right
  (r,c) = bottom.shape
  m[:,cols-1:] = np.flip(bottom.reshape(c,r))

  # right->top
  (r,c) = right.shape
  m[:1,:] = right.reshape(c,r)

  # print ("\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n".format(top,left,bottom,right,m))
  print ("\n{}\n".format(m))

  print ("clockwise")

  # left-> top
  (r,c) = left.shape
  m[:1,:] = np.flip(left.reshape(c,r))

  # bottom->left
  (r,c) = bottom.shape
  m[:,:1] = bottom.reshape(c,r)

  # top->right
  (r,c) = top.shape
  m[:,cols-1:] = top.reshape(c,r)

  # right->bottom
  (r,c) = right.shape
  m[rows-1:,:] = np.flip(right.reshape(c,r))

  print ("\n{}\n".format(m))
