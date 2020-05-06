from PIL import Image, ImageFilter
#Read image
im = Image.open( '18873.jpg' )
#Display image
im.show()

#Applying a filter to the image
im_sharp = im.filter( ImageFilter.SHARPEN )
#Saving the filtered image to a new file
im_sharp.save( 'image_sharpened.jpg', 'JPEG' )

#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()

#Applying blur filter to the image
im_blur = im.filter( ImageFilter.BLUR )

#Saving the filtered image to a new file
im_blur.save( 'image_blurred.jpg', 'JPEG' )

#Display blurred image
im_blur.show()