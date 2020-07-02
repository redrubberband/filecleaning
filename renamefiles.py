from scandir import getAllFiles

def main():
    currentDir = getAllFiles()                                                  #currentDir is the list of files in the working directory

    print("Scanning each files...")
    for file in currentDir:

        if file.is_file():

            filename = file.stem                                                #remove all the path, get just the filename (unfortunately without the extension)
            filename_format = file.suffix                                       #get the file extension
            filename = filename.lower()
            filename = filename.replace("-"," ")\
                                .replace("v1x","")\
                                .replace("v2u","")                              #remove all the unneeded characters
            
            wordlist = filename.split()
            newwordlist = []

            for word in wordlist:                                               #scan all the words and capitalize the selected ones
                
                #THIS CODE IS THE SAME AS THE UNCOMMENTED LINE, JUST CLEARER
                #if (word != "ga" and word != "ni"):
                #    newwordlist.append(word.capitalize())
                #else:
                #    newwordlist.append(word)
                
                newwordlist.append(word.capitalize() \
                    if word != "ga" \
                    and word != "ni" \
                    and word != "no" \
                    and word != "wa" \
                    and word != "is" \
                    and word != "and" \
                    and word != "a" \
                    else word)

            filename = " ".join(newwordlist)                                    #join the words together
            filename = filename[:1].upper() + filename[1:]                      #finally, capitalize the first character of the filename
            
            file.replace(filename+""+filename_format)                           #renames the file in the current directory
    print("Renaming finished.")




main()