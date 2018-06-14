import io
#from PIL import Image
from PIL import Image
#import pytesseract
from wand.image import Image as wi

pdf = wi(filename = "test.pdf", resolution = 300)
pdf = pdf.convert('jpeg')

imageBlovsv = []

for img in pdfImage.sequence:
    imagePage = wi(image = img)
    imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
    im = Image.open(io.BytesIO(imgBlob))
    texr = pytesseract.image_to_string(im, lang = 'eng')
    recognized_text.append(text)

print(recongnized_text)
