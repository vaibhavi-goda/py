from PIL import Image
img=Image.open('slb.jpeg')
trans_img=img.transpose(Image.FLIP_LEFT_RIGHT)
trans_img.save('corrected.jpeg')
print("Done flipping")
'''import cv2
img=cv2.imread('slb.jpeg')
clahe=cv2.createCLAHE()
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
enh_img=clahe.apply(gray_img)
cv2.imwrite('enhanced.jpeg',enh_img)
print('Done enhancing')'''
