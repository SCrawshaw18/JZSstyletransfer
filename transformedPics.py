#simply pulls transfomred images from cloudinary and saves them to a folder.
import cloudinary
from PIL import Image
import requests
from io import BytesIO
import numpy as np

cloudinary.config( 
  cloud_name = "ask-milton", 
  api_key = "571639764722334", 
  api_secret = "3BKj-omKqS4Gs8WtQZcnJFSbpN4" 
)

def findIndex(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

imgnames = ['Stadium_pp9rdb.jpg' , 
'Skyline_k2f9fc.jpg' ,
'Rainbow_rcvmad.jpg' ,
'Hockey_bpmj3i.jpg' ,
'Dog_aeri2n.jpg' ,
'Protest_netix6.jpg' ,
'Fire_k4fopt.jpg' ,
'Maple_nzwqzr.jpg' ,
'Beach_dc0anp.jpeg' ,
'Construction_hjn4cc.jpg' ,
'Dice_ekav7t.jpg' ,
'Car_kaixqa.jpg' ,
'Tiger_def9hk.jpg' ,
'Baby_r4vbbd.jpg' ,
'Desert_zsmnhl.jpg'] # possible names for all images uploaded to Cloudinary
 
mods = ['tint',
'saturation',
'brightness',
'sepia',
'contrast',
'blur'] # possible image modifications/manipulations using Cloudinary libraries

num = 10 # number of degress of manipulations we will do for each mod

for i in range(len(imgnames)): #for testing
	for j in range(len(mods)): #for testing
		for k in range(num): # runs for different levels of mod for 'num' times
			url=cloudinary.CloudinaryImage(imgnames[i]).image(effect=mods[j] + ":" + str((k+1)*10)) # set url for image along with modification
			x = imgnames[i].index("_")
			name=imgnames[i][:x] + "-" + mods[j] + "-" + str((k+1)*10)
			print("%s, %s"%(imgnames[i],name))
			pos=findIndex(url,"\"")
			image=requests.get(url[pos[0]+1:pos[1]]).content
			with open("transformed_images/%s.jpg"%(name), 'wb') as handler:
				handler.write(image)