import numpy as np
#a = {'world':{'1':0,'2':1,'3':0,'4':3}}
a = [[1,2,3],[7,2,3]]
a = np.array(a)
b = [1,4]
b=np.array([b]).T
#a=np.array(a)
# k = [x!=0 for x in a['world']]
# b = np.sum([a['world'][x]!=0 for x in a['world']], axis=0)

# div = np.sum(a, axis=0)
# print(div)
# a=a/div
# for x in a['world']:
#     print(x)
#print(k)
k = np.linalg.norm(a-b, axis=0)
print(k)
