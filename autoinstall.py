import os

while True:
 link = input("Insert link: ")
 os.system("git clone " + link)
 print("Done!")
