res_dic = {'z': [0, 0, 0, 1], 'f': [0, 0, 0, 8], 'a': [5, 3, 7, 1], 'b': [1, 0, 1, 0]}
aa = [1,2,3,4]

import numpy as np
print(np.array(aa[1:3]) > 1)
print((np.array(res_dic['z'][0:3]) > 0).all())