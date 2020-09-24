from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def removenums(img, error=10):
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    for i in range(len(data["text"])):
        if data["text"][i]:
            w = data["width"][i]
            h = data["height"][i]
            l = data["left"][i]
            t = data["top"][i]

            img.paste((255, 255, 255), [l-error, t-error, l+w+error, t+h+error])
        
    return img

