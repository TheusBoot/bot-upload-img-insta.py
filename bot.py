import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

PhotoPath = "C:\\Users\\emailmartingcf1\\Desktop\\servidor-bot\\img\\marvel_braa"  # Change Directory to Folder with Pics that you want to upload

IGUSER = "user"  # Change to your Instagram USERNAME
PASSWD = "*****"  # Change to your Instagram Password
# Change to your Photo Hashtag

IGCaption1 = 'SUA LEGENDA' # você pode criar diversas legendas e por um random dentro do for e com isso cria diversas legendas

os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
print(ListFiles)
print("Total Photo in this folder:" + str(len(ListFiles)))

 #Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER, PASSWD)
igapi.login()  # login

for i, _ in enumerate(ListFiles):
    photo = ListFiles[i]
    print(photo)
    #rand = random.choice(IGCaption11)
    print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
    print("Now Uploading this photo to instagram: " + photo)
    igapi.uploadPhoto(photo, caption=IGCaption1, upload_id=None)
    os.remove(photo)
    # sleep for random between 60 - 120s
    n = randint(120,123)
    print("Sleep upload for seconds: " + str(n))
    time.sleep(n)
