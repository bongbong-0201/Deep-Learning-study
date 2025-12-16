import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread(r"C:\Users\user\Desktop\이모티콘 - 아미야\01.png")

plt.imshow(img)
print(img.shape)  # shape: 모양(형태)을 보여줘!
plt.show()
