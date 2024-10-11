# Extracted from https://stackoverflow.com/questions/6444548/how-do-i-get-the-picture-size-with-pil
def get_image_dims(file_path):
    from PIL import Image as pilim
    im = pilim.open(file_path)
    # returns (w,h) after rotation-correction
    return im.size if im._getexif().get(274,0) < 5 else im.size[::-1]

