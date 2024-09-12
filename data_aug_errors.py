import cv2, sys
import numpy as np
import os
from glob import glob

org = cv2.imread('org/pen_white.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('org', org)