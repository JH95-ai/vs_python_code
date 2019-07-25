#function means 修剪
#大于max的就使它等于max，小于min的就使它等于min

import numpy as np
x=np.array([1,2,3,5,6,7,8,9])
y=np.clip(x,3,8)
print(y)
