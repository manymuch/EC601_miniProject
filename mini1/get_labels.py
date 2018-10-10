import argparse
import base64
import os
import googleapiclient.discovery

# transform time_in_seconds to hours:min:secs format
def get_time_format(time_in_seconds):
    assert type(time_in_seconds) == int
    hour = time_in_seconds/int(3600)
    hour_remain = time_in_seconds%int(3600)
    minute = hour_remain/int(60)
    seconds = hour_remain%int(60)

    #begin seconds of a subtitle for a image
    whole_str_1 = "%02d:%02d:%02d,000"%(hour,minute,seconds)

    time_in_seconds = time_in_seconds-1
    hour = time_in_seconds/int(3600)
    hour_remain = time_in_seconds%int(3600)
    minute = hour_remain/int(60)
    seconds = hour_remain%int(60)

    #end seconds of a subtitle for a image
    whole_str_2 = "%02d:%02d:%02d,000"%(hour,minute,seconds)

    #the whole line of a subtitle for a image
    whole_str = whole_str_2 + " --> " + whole_str_1
    return whole_str

# get a label of an image using google vision api
def onelabel(photo_file):
    """Run a label request on a single image"""


    service = googleapiclient.discovery.build('vision', 'v1')

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 1
                }]
            }]
        })

        response = service_request.execute()
        label = response['responses'][0]['labelAnnotations'][0]['description']
        return label

def write_srt(directory):

    #change to directory that stores all the images
    os.chdir(directory)
    files = os.listdir()

    # writting subtitles files
    with open("./../movies.srt",'w') as f:
        i = 0
        for file in files:
            i = i+1
            f.write("%s\n"%i)

            # write times
            f.write("%s\n"%get_time_format(i))

            #write labels
            f.write("%s\n"%onelabel(file))
            print("getting "+str(i)+" labels")
    os.chdir("./../")
