#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
data = [[1, 2, 3], [4,5,6,], [7,8,9]]
def putar_data(data): # membuat func
    putar = np.rot90(data, k=3, axes=(1,0)) #fungsi np.rot memutar data, k= key , axes=1 (kolom)
    return putar
print(putar_data(data))


# In[ ]:




