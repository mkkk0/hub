import os

#------------------------------------------------------------------------------------
#-  script names wanted filetypes with same name as their parent directory name is  -
#------------------------------------------------------------------------------------

#asking user for input 
def userinput(name1, name2):
    possibilities = ["y", "n", "q"]
    while True:
        userinput = str(input("Do you want to rename file \n{} \nto \n{}? [y/n/q]\n".format(name1, name2)))
        userinput.lower()
        if userinput in possibilities:
            return userinput

def main():
    #insert path
    path = ""

    #which kind of filetypes to name
    filetype = ".mp4"

    #substrings to filter out unwanted directories
    substring = "Run"
    substring2 = "run"

    #go through dirs and files in given path
    for root, dirs, files in os.walk(path, topdown=True):
        #go through files
        for filename in files:

            #if given subtring names in directory then proceeded 
            if substring in root or substring2 in root:

                #if wanted filetype matches to file then proceeded
                if filetype in filename:

                    #splitting the path to get building block for new_name
                    head_tail = os.path.split(root)

                    old_name = root + "\\" + filename

                    #new_name build from root + splitted root + filetype
                    new_name = root + "\\" + head_tail[1] + filetype

                    #asking user input for what to do for file
                    useroption = userinput(old_name, new_name)

                    #if user chooses "y" then the file will be renamed
                    if useroption == "y":
                        os.rename(old_name, new_name)
                        print("The old name was {}".format(old_name))
                        print("The new name is {}".format(new_name))

                    #if user chooses "q", the user will quit program    
                    elif useroption == "q":
                        exit()
                        

main()
