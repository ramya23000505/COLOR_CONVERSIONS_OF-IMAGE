

import cv2
from google.colab.patches import cv2_imshow

# In[ ]:


#1.	Read and Display an Image
```
import cv2
img=cv2.imread('anime.jpg',1)
img=cv2.resize(img,(400,300))
cv2.imshow('show',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

# In[ ]:


#2.	Draw Shapes and Add Text
```
import cv2
image=cv2.imread('anime.jpg')
print(image.shape)
```
# In[ ]:


#3.Image Color Conversion
```
import cv2
img = cv2.imread('anime.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)

hsv1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv1)

hsv2 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv2)

gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray1)

gray2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

# In[ ]:

#4.Access and Manipulate Image Pixels
import random
import cv2
img=cv2.imread('anime.jpg',1)
re=cv2.resize(img,(300,300))
for i in range (150,200):
    for j in range(re.shape[1]):
        re[i][j]=[random.randint(0,255),
                       random.randint(0,255),
                       random.randint(0,255)] 
cv2.imshow('part image',re)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[ ]:

#5.Image Resizing
import cv2
img=cv2.imread('anime.jpg',1)
re=cv2.resize(img,(400,400))
tag =re[150:200,110:160]
re[110:160,150:200] = tag
cv2.imshow('cut image',re)
cv2.waitKey(0)
cv2.destroyAllWindows()
# In[ ]:

#6.	Image Cropping
# In[ ]:
import cv2
img=cv2.imread('anime.jpg',1)
re=cv2.resize(img,(400,400))
tag =re[150:200,110:160]
re[110:160,150:200] = tag
cv2.imshow('cut image',re)
cv2.waitKey(0)
cv2.destroyAllWindows()

#7.Image Flipping
import cv2
img=cv2.imread('anime.jpg',1)
re=cv2.resize(img,(400,400))
tag =re[150:200,110:160]
re[110:160,150:200] = tag
cv2.imshow('cut image',re)
cv2.waitKey(0)
cv2.destroyAllWindows()
# In[ ]:

#8.Write and Save the Modified Image
import cv2
img=cv2.imread('anime.jpg')
re=cv2.resize(img,(400,300))
cv2.imwrite('display.jpg',re)
cv2.imshow('display',re)
# In[ ]:
