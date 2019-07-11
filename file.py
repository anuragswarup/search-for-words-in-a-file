import os.path
from os import path
import os
os.mkdir('/root/PycharmProjects/cube_cinemas/cube')

file_names=[]
flag=0
def create_files():

    global file_names
    print("enter the number of file to add")
    k=int(input())
    for i in range(0,k):
        print("enter file name")
        sampletext= input()
        file_names.append(sampletext)
        path_name="/root/PycharmProjects/cube_cinemas/cube/"+sampletext
        l=list(map(str,input().split("\n")))
        with open(path_name, 'w') as filehandle:
            for listitem in l:
                    filehandle.write('%s\n' % listitem )


def search():
    global file_names
    global flag
    print("enter the word to search")
    search=input()
    length_list_filenames= len(file_names)

    for i in range(0,length_list_filenames):
        path_name = "/root/PycharmProjects/cube_cinemas/cube/"+file_names[i]
        with open(path_name, 'r') as f1, open(path_name+str(i), 'w') as f2:
            for line in f1:
                for word in line.split():
                    f2.write(word + '\n')
        arr=[]
        fo=open(path_name+str(i),"r")
        arr=fo.readlines()
        newarr = [x[:-1] for x in arr]
        check=len(newarr)

        for j in range(0,check):
            if newarr[j] == search:
                flag=1
                print("FILE "+ file_names[i]+" contains the word u searched for.")
                break;



        fo.close()






create_files() #CREATE A DIRECTORY AND FILES IN THEM
search()
if flag == 0:
    print("SORRY!! NO FILES HAVE THE WORD U REQUESTED FOR.")




