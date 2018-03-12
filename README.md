# Introduction
Our group set out to determine how the stylistic elements of a photograph would affect the success of style transfer. First, we collected an assortment of different images. Then, using an image editing API called "Cloudinary", we increased the contrast, blurriness, brightness, saturation, sepia, and red tint on each image in increments of 10%. We then passed these images through a style transfer neural network using the style of Edvard Munch's "The Scream". We compiled these images into a gallery and observed the results, noting the impact of transformations on the style transfer.

# Guide to Our Repo
## Running the Transformer and Stylizer
Our main file, Cloudinary.py, pulls down transformed versions of our images from Cloudinary, runs the images through the stylization network, and saves the stylized images to the results folder. To run it, simply delete all the images from the results folder and run Cloudinary.py. One should only run this file on a fast computer or with ample time on their hands, as it takes two hours on a very powerful machine.

Our secondary file, transformedPics.py, does the same thing as Cloudinary.py, but it skips the sylization step and saves the transformed images to the transformed_images foler. To run it, simply delete all the images from the transformed_images folder and run transformedPics.py. This program should only take about 10-15 minutes to complete.

## Image Folders
We have two image folders: results and transformed_images. The transformed_images folder has all the transformed images, while the results folder has the stylized version of the transformed images. We made these two folders so we could compare the inital image to the stylized image.

## Special Thanks
We'd like to thank Logan Engstrom for creating the [fast style transfer CNN](https://github.com/lengstrom/fast-style-transfer) that we used for the image stylization. We'd also like to give a shoutout to [Cloudinary](https://cloudinary.com/) for giving us 10,000 free image transformations. Finally, we'd like to thank [Ms. Pries](https://github.com/MsPries) for being a great mentor to us throughout the project period.
