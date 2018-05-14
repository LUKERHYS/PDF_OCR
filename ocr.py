from wand.image import image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages9()[1]

req_image = []
final_text = []

image_pdf = Image(file="./PDF_FILE_NAME",
                  resolution=300)
image_jpg = image.pdf.convert('jpeg')


for img in image_jpg.sequence:
    img_page = Image(image=img)
    req_image.append(img_page.make_blob('jpeg'))

for img in req_image:
    txt = tool.image_to_string(
        PI.open(io.BytesIO(img)),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    final_text.append(txt)

def 

for stock in final_text:
    if stock == stock_ref
