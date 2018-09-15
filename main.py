from download_imgs import get_all_images_url,save_imgs
from get_labels import write_srt
from convert import generate_video
import argparse,os

parser = argparse.ArgumentParser()
parser.add_argument('--num',default=10,type=int, help='the numbers of images to download')
parser.add_argument('--name',default="@JeremyClarkson",type=str, help='the twitter account to download images from')
parser.add_argument('--directory',default="images",type=str, help='directory to save all the images')
parser.add_argument('--output_name',default="\"movies.mp4\"",type=str, help='directory to save all the images')
args = parser.parse_args()
num = args.num
name = args.name
directory = args.directory
output_name = args.output_name



#saving images to ./images
#naming them as 1.jpg 2.jpg etc..
media_files = get_all_images_url(name,num)
print("saving "+str(len(media_files))+" "+directory)
save_imgs(media_files)

#using google vision to get labels of the images in the folder
#and then write as srt subtitles to srt files
print("\nsaving subtitles files")
write_srt(directory)

#generate_video with subtitle burned in using ffmpeg
print("generating video...")
generate_video(output_name)
