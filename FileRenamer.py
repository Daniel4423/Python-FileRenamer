import os
def rename_files():
    #get file names from folder
    file_list = os.listdir(r"{replace with path of files to change}")
    #if you want to make sure you've got the right path, unhash next line
    #print(file_list)
    saved_path = os.getcwd()
    print("current working directory is " +saved_path)
    os.chdir(r"{replace with path of files to change}")
    print("NOW current working directory is " + os.getcwd())

    #for each file, rename files
    for file_name in file_list:
        print("Old Name - " + file_name)
        translation_table = str.maketrans("0123456789", "          ", "0123456789")
        os.rename(file_name, file_name.translate(translation_table))
        print("New Name - " + file_name.translate(translation_table))


    os.chdir(saved_path)
rename_files()
