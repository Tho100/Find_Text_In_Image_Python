import pytesseract as pts
import cv2

img = cv2.imread("C:\\users\\HP\\DOcuments\\my folder\\yourmom.png")

# Print the text of the image

def text_image(text) -> str:
    print(text)

get_text = pts.image_to_string(img) # Find the text
print(get_text)

cv2.imshow('Your Mom',img)
cv2.waitKey(0)
