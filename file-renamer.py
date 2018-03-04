import os
from natsort import natsorted, ns
old_name=[]
new_name=[]
saved_path=r""
directory_path=r""
desired_name=r""
renamed = False
def rename_files():
    # 1- get the names of the files and sort them in the natural order
    global directory_path
    directory_path= raw_input("Enter the files path: ")
    global desired_name
    desired_name=raw_input("Enter your desired name: ")
    file_list=natsorted(os.listdir(directory_path),alg=ns.IC)
    print(file_list)
    global saved_path
    saved_path=os.getcwd()
    print("The current working directory is "+saved_path)
    os.chdir(directory_path)
    # 2- for each file, rename filename
    file_counter = 0
    while file_counter< len(file_list):
        file_full_name=file_list[file_counter]
        file_name,file_extention=os.path.splitext(file_full_name)
        print("Old Name: "+file_name)
        old_name.append(file_full_name)
        print("file extention is: "+file_extention)
        cur_name=desired_name+str(file_counter+1)+file_extention
        print("New Name: "+cur_name)
        new_name.append(cur_name)
        os.rename(file_full_name,cur_name)
        file_counter = file_counter + 1
    global renamed
    renamed=True
    print("renamed ="+str(renamed))
    os.chdir(saved_path)
def undo_rename_files():
    #1- if files are already renamed, switch the new names with the old names
    if renamed:
        os.chdir(directory_path)
        names_counter=0
        while names_counter< len(new_name):
            print("Old Name: "+new_name[names_counter])
            print("New Name: "+old_name[names_counter])
            os.rename(new_name[names_counter],old_name[names_counter])
            names_counter= names_counter + 1
        os.chdir(saved_path)
   #2- if the files are not renamed, you get an error     
    else:
        print("Sorry, you need to rename first to undo")
while True:
    mode= raw_input("Type either rename, undo, or exit modes: ")
    if mode=="rename":
        rename_files()
        
    elif mode=="undo":
        undo_rename_files()
    elif mode=="exit":
        break
    else:
        print("Sorry, wrong command")
#suggested features:
    # GUI for directory selection
