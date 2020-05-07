import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open ('/home/edi/Pictures/IMG_9733.jpg').convert ('L').resize ((750,500))
im.show ()
ar = np.array (im)
#print (ar)
th = 160
#ar_bin = (ar > th) * 255 
#print (ar_bin)   
#plt.plot (ar_bin,color='C0') 
#plt.show ()