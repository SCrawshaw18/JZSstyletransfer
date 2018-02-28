import cloudinary
from PIL import Image
import requests
from io import BytesIO

cloudinary.config( 
  cloud_name = "ask-milton", 
  api_key = "571639764722334", 
  api_secret = "3BKj-omKqS4Gs8WtQZcnJFSbpN4" 
)

def findIndex(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

url=cloudinary.CloudinaryImage("Tiger_def9hk.jpg").image(effect="contrast:35")
pos=findIndex(url,"\"")
url=url[pos[0]+1:pos[1]]

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()