#!/usr/bin/env python3
# coding: utf-8

# In[2]:
import cv2
import os
import sys
import numpy as np

class lane(object):
  def __init__(self, frame):
    self.frame = frame

  def grayscale(self):
    self.frame = cv2.cvtColor(self.frame , cv2.COLOR_RGB2GRAY)

  def gaussianblur(self):
    self.frame = cv2.GaussianBlur(self.frame, (5, 5), 0)
  
  def canny(self):
    self.frame = cv2.Canny(self.frame, 50, 150)

  def roi(self, vec):
    mask = np.zeros_like(self.frame)
    if len(self.frame.shape) == 3:
      mc = (255,) * self.frame.shape[2]
    else:
      mc = 255
    cv2.fillPoly(mask, vec, mc)
    masked = cv2.bitwise_and(self.frame, mask)
    return masked
  
  def rc(self):
    height, width = self.frame.shape[0:2]
    imshape = self.frame.shape
    x = np.shape(self.frame)[1]
    y = np.shape(self.frame)[0]
    vertices = np.array([[(10,y-50),(x -10,y-50),(x/2+40,y/1.65),(x/2-40,y/1.65)]],
                      dtype = np.int32)
    self.frame = self.roi(self.frame, vertices)


class window(object):
  def __init__(self, vid):
    self.vid = vid
  
  def display(self):
    cap = cv2.VideoCapture(self.vid)
    while cap.isOpened():
      ret, frame = cap.read()
      if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame', gray)
      if cv2.waitKey(1) == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
  if os.getenv("VID") is not None:
    window(sys.argv[1]).display()
  else:
    print("WE WANT  WANT IMG")

