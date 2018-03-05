import cloudinary
from PIL import Image
import requests
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

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

colors = ['b','r','g','k','y','m'] # colors used for graphing
marker = ['o','^','v','*','+','x'] # markers of data points used for graphing
 
mods = ['tint',
'saturation',
'brightness',
'sepia',
'contrast',
'blur'] # possible image modifications/manipulations using Cloudinary libraries

num = 10 # number of degress of manipulations we will do for each mod

for i in range(1): #for testing
#for i in range(len(imgnames)): #runs through all images
	for j in range(1): #for testing
	#for j in range(len(mods)): #runs through all mods
		print(imgnames[i].split("_")[0] + ': ' + mods[j])
		images = [] # construct empty list used to store images pulled from Cloudinary
		#error = [] #uncomment when you input error using neural net

		for k in range(num): # runs for different levels of mod for 'num' times
			url=cloudinary.CloudinaryImage(imgnames[i]).image(effect=mods[j] + ":" + str((k+1)*10)) # set url for image along with modification
			pos=findIndex(url,"\"")
			images.append(Image.open(BytesIO(requests.get(url[pos[0]+1:pos[1]]).content))) # adds image to 'images' list
			#run images[k] through neural network
			#error.append(error from neural network)

		##############graphing
		plt.scatter([10*x for x in range(num)], np.random.rand(num), s=np.pi*8, c=colors[j], marker=marker[j], alpha=0.5, label=mods[j]) # automatically adjusts axes based on numbers
		#plt.scatter([10*x for x in range(num)], error, s=np.pi*8, c=colors[j], marker=marker[j], alpha=0.5, label=mods[j]) # automatically adjusts axes based on numbers
			# use this scatter if using error from neural network

	plt.legend(loc="upper center", ncol=3, fancybox=True)
	plt.xlabel("% of Modification")
	plt.ylabel("Error")
	plt.title(imgnames[i].split("_")[0])
	plt.show()
	#plt.savefig(imgnames[i].split("_")[0]) #use this line if you want to save the figures as .png instead of displaying them
		# it's worth noting that this will save the image of the graph in the same folder is the .py file

#images[0].show()