import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D 
fig = plt.figure()
ax = Axes3D(fig)

img = mpimg.imread('./imgs/3.jpg')


r = []
g = []
b = []

for line in img:
    for pixel in line:
        temp_r, temp_g, temp_b = pixel
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

pddf  = pd.DataFrame({'red': r,
'blue': b,
'green': g})
df = pddf #fuck this solution
ax.scatter(r,g,b)


from scipy.cluster.vq import whiten 

df['scaled_red'] = whiten(df['red'])
df['scaled_blue'] = whiten(df['blue'])
df['scaled_green'] = whiten(df['green'])
#df.sample(n = 10)


from scipy.cluster.vq import kmeans 
cluster_centers, distortion = kmeans(df[['scaled_red', 'scaled_green', 'scaled_blue']], 2)

plt.close()
colors = []
r_std, g_std, b_std = df[['red', 'green', 'blue']].std()

print("This is my predominant color (1)RGB code") 
for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    colors.append(( scaled_r * r_std / 255, scaled_g * g_std / 255, scaled_b * b_std / 255))
    print("rgb (", 
          (int) (scaled_r * r_std), 
          ",", (int) (scaled_g * g_std), 
          ",", (int) (scaled_b * b_std), ")")


imgplot = plt.matshow(img)
plt.matshow([colors])
plt.show()