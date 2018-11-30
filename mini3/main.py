from download_imgs import get_all_images_url,save_imgs
from get_labels import write_srt
from convert import generate_video
from mysql import *

def mini1(num=10,name="@JeremyClarkson",directory="images",output_name = "\"movies.mp4\""):
    #saving images to ./images
    #naming them as 1.jpg 2.jpg etc..
    media_files = get_all_images_url(name,num)
    print("saving "+str(len(media_files))+" "+directory)
    save_imgs(media_files)

    #using google vision to get labels of the images in the folder
    #and then write as srt subtitles to srt files
    print("\nsaving subtitles files")
    label_list = write_srt(directory)

    #generate_video with subtitle burned in using ffmpeg
    print("generating video...")
    generate_video(output_name)
    return media_files, label_list

if __name__ == '__main__':

    print("welcome to EC601 mini project 3")
    print("please input your name")
    user_name = input()
    while True:
        print("-----------MENU----------------")
        print("1. mini project 1")
        print("2. show the table in database")
        print("3. search with certain key words")
        print("4. how many images a user has fetch?")
        print("5. clear datasets table")
        print("0. exit")
        choice = int(input())
        if choice == 1:
            print("please input the twitter account:")
            twitter_account = input()
            print("please input the number of images to fetch:")
            num = int(input())
            assert num>0,"please input a valid integer number"
            imgs,labels = mini1(num,twitter_account)
            assert len(imgs) == num, "number of urls from twitter is wrong"
            assert len(labels) == num, "number of labels from google vision is wrong"
            CursorObject = connect_mysql()
            for i in range(num):
                insert(CursorObject,user_name,twitter_account,imgs[i],labels[i])
        elif choice == 2:
            CursorObject = connect_mysql()
            printall(CursorObject)
        elif choice == 3:
            CursorObject = connect_mysql()
            print("please input keyword to search")
            keyword = input()
            search(CursorObject,keyword)
        elif choice == 4:
            print("please input the user name")
            user_name = input()
            CursorObject = connect_mysql()
            image_numbers = user(CursorObject,user_name)
            if image_numbers == 0:
                print("there is no this user")
            else:
                print("the user has fetch "+str(image_numbers)+str(" image(s)"))
        elif choice == 5:
            print("Are you sure to clear table? y/n")
            answer = input()
            if answer is ('y' or 'yes' or 'Yes' or 'Y' or 'YES'):
                CursorObject = connect_mysql()
                clear_table(CursorObject)
        elif choice == 0:
            print("bye")
            break
        else:
            print("wrong input")
