#!/bin/env python3
import os
import dropbox

accesskey = ''


class TransferData():
    def __init__(self, accesskey):
        self.accesskey = accesskey

    def send(self, dir_from, dir_to):
        dbx = dropbox.Dropbox(self.accesskey)

        if(os.path.exists(dir_from)):
            for (root, dir, files) in os.walk(dir_from):
                for file in files:
                    filename = ''
                    if(root[-1] == '/'):
                        filename = root+file
                    else:
                        filename = root+"/"+file

                    if not os.path.isdir(filename):
                        with open(filename, 'rb') as file:
                            dbx.files_upload(
                                file.read(), "/"+dir_to+"/"+filename)

        else:
            print("path not found ")


def main():

    data = TransferData(accesskey)

    dir_from = input("enter dir to upload ")
    dir_to = input("enter dir to upload ")

    data.send(dir_from, dir_to)
    print("dir has been uploaded")


if __name__ == '__main__':
    main()
