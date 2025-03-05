# file handling in python
path = "/home/arpit-parekh/files/from_my_batch.txt"

# file = open(path,"w")
# file = open(path,"a")
# file.write(" Weclome to Python")

print("File written successfully")
# file.close()

file1 = open(path,"r")
print(file1.read())
file1.close()

import os
# os.remove(path) to remove the file
# os.rename(path,"/home/arpit-parekh/files/from_my_batch.txt")

####################################################################################

image_url = "https://fastly.picsum.photos/id/369/536/354.jpg?hmac=UHUpu7ESHegJ7M748r7k90U7VaaMu5EuV2n4hAA49-Y"

download_path = "/home/arpit-parekh/files/meri_image.jpg"

import requests
response = requests.get(image_url)

print(response.content)

file = open(download_path,"wb")   # data is comming in byte stream
file.write(response.content)
print("Image Downloaded Successfully")
file.close()

#####################################################################################

songUrl = "https://file-examples.com/storage/fe435d6a5467c753ca23df4/2017/11/file_example_MP3_1MG.mp3"

repsonse =  requests.get(songUrl)

file = open("/home/arpit-parekh/files/mera_song.mp3","wb")
file.write(repsonse.content)
print("Song Downloaded Successfully")
file.close()
