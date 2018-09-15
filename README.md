# EC601_miniProject


# Task

this library will fetch certain numbers of images from a certain twitter account, then download the images and using google vision API to get labels for those images. And then generate a video with all the images with labels showed as subtitles.

# Usage

run the code below will do the whole thing with default settings
'''python
python main.py
'''

for cumstom settings, see below:  

'''Bash
--num
'''
int, the number of images to download, twitter only allow up to 3240 images
'''Bash
--name
'''
string, the twitter account to download from, remember to add "@"
'''Bash
--directory
'''
name of the directory to be created for saving the images
'''Bash
--output_name
'''
output video file names
