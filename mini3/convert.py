import os,io
import subprocess





def generate_video(output_name,if_rmsrt=True):
    #using ffmpeg command
    command = "ffmpeg -f image2 -pattern_type glob -framerate 1 -i \'./images/*.jpg\'  -vf \"scale=\'min(1280,iw)\':min\'(720,ih)\':force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2, subtitles=\'movies.srt\'\" %s"%output_name

    subprocess.call(command,shell=True)
    # default setting will remove str files after the video has been generated
    if if_rmsrt==True:
        rmsrt = "rm movies.srt"
        subprocess.call(rmsrt,shell=True)
        rmimg = "rm -rf ./images"
        subprocess.call(rmimg,shell=True)





#backup command that wooooorks!
# command = "ffmpeg -f image2 -pattern_type glob -framerate 1 -i \'./images/*.jpg\'  -vf \"scale=\'min(1280,iw)\':min\'(720,ih)\':force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2, subtitles=\'movie.srt\'\" \"movies.mp4\""
# subprocess.call(command,shell=True)
