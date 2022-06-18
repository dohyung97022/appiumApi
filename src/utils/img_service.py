import io
import base64
from PIL import Image


def resize_base_64(base_64, width: int, height: int, format: str = 'PNG'):
    buffer = io.BytesIO()
    imgdata = base64.b64decode(base_64)
    img = Image.open(io.BytesIO(imgdata))
    new_img = img.resize((width, height))
    new_img.save(buffer, format=format)
    return str(base64.b64encode(buffer.getvalue()))[2:-1]
