#-----------------------------
#reading_files.py
#Sedric Asuncion
#-----------------------------

## ----- Functions ----- ##
def read_file():
    #imports file into a variable
    file = open('Code-langs.txt', 'r')
    
    #saves content to a variable
    script = file.read()
    
    #prints the whole script
    print(script)
    
    #close the file
    file.close
    
## ----- Main Code ----- ##
read_file()