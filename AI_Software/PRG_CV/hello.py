import numpy as np

a = np.array([-4.3, +2.3, 12.9, 8.99, 10.1, -1.2])
print(a)

a.sort()
print(a)

a.shape = (2, 3) #[2][3] 배열로 만들어줌
print(a)

print(type(a))

print(a[1][2])
