import os
import sys

#Implement ideas like character count displaying, character count %, word count, %, based on user's choice (make everything funcitonal/as methods)
class File:
    file_name = ""
    corpus = ""
    char_count = {}
    total_chars = 0
    char_percentage = {}
    word_count = {}
    total_words = 0
    word_percentage = {}

    def __init__(self,filename):
        self.file_name = filename
        print("File loaded succesfuly")
        try:
            curr = open(file_name,'r',os.path.getsize(file_name)) #Make it as a package after everything is complement
            #Use psutil or resource module to get available memory
        except FileNotFoundError:
            print("File not found!")
            sys.exit(1)
        else:
            print("Reading the file...")
        #Make sure to close the file and end program if any exceptions are raised further down the code
        corpus = curr.read() #Any improvements to make this part memoryless?

           #print(corpus)
        for i in corpus:
            if not self.char_count.__contains__(i):
                self.char_count[i]=0
                self.char_count[i]+=1
                self.total_chars+=1
        #Any room for optimization - like adding the below code to the above one?
            sum = 0
            for key in self.char_count.keys():
                self.char_percentage[key] = 100*self.char_count[key]/self.total_chars
                #sum+=self.total_wordschar_percentage[key]
        #print(sum) #It exceeds 100 for some reason, check why it gives for example 100.0000000...001?

        for key,value in self.char_percentage.items():
            #print (key,value)
            pass

        word_count = {}
        i,j,n=0,0,int(len(corpus))
        print(type(n),type(i))
        nonalpha = {',','.','/',';','\'','[',']','\\','!','@','#','$','%','^','&','*','(',')','-','=','_','+','`','~','<','>','?',':','"','{','}','|','\n',' ','\t'}
        stops = {'.','!','?'}
        print(i,j,n)
        while (i<n and j<n):
            if(corpus[i] in nonalpha):
                i+=1
                continue
            j=i
            while(j<n and corpus[j] not in nonalpha):
                j+=1
            word = corpus[i:j]
            if not word_count.__contains__(word):
                word_count[word] = 0
            word_count[word]+=1
            i=j
    
        for key,value in word_count.items():
            #print(key,value)
            pass
        #Maybe convert the whole text to lowercase and replace nonalpha chars with ' ' - Both can be done in one loop
        #Try to use parallelization techniques if posssible for the loops
        sentence_count = 0
        
        #Try to find other useful statistics like: avg word length, most used word


        #Further implementations: searching specific words (like the line of appearance/index?)

        #CHATGPT suggestions - ^,generating word clouds, or analyzing sentiment of text
        #Test your script with various text files to ensure its robustness and handle different edge cases
        curr.close()
    
 
if __name__=="__main__":

    #Reading in the file location as command line argument
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Failed to enter the path with file name")
        sys.exit(1)
    print("Locating the file...")

    #Opening the file using the class 
    newfile = File(file_name) 
    


    
    '''
    #print(corpus)
    for i in corpus:
        if not char_count.__contains__(i):
            char_count[i]=0
        char_count[i]+=1
        total_chars+=1
    #Any room for optimization - like adding the below code to the above one?
    sum = 0
    for key in char_count.keys():
        char_percentage[key] = 100*char_count[key]/total_chars
        sum+=char_percentage[key]
    #print(sum) #It exceeds 100 for some reason, check why it gives for example 100.0000000...001?

    for key,value in char_percentage.items():
        #print (key,value)
        pass

    word_count = {}
    i,j,n=0,0,int(len(corpus))
    print(type(n),type(i))
    nonalpha = {',','.','/',';','\'','[',']','\\','!','@','#','$','%','^','&','*','(',')','-','=','_','+','`','~','<','>','?',':','"','{','}','|','\n',' ','\t'}
    stops = {'.','!','?'}
    print(i,j,n)
    while (i<n and j<n):
        if(corpus[i] in nonalpha):
            i+=1
            continue
        j=i
        while(j<n and corpus[j] not in nonalpha):
            j+=1
        word = corpus[i:j]
        if not word_count.__contains__(word):
            word_count[word] = 0
        word_count[word]+=1
        i=j
    
    for key,value in word_count.items():
        #print(key,value)
        pass
    #Maybe convert the whole text to lowercase and replace nonalpha chars with ' ' - Both can be done in one loop
    #Try to use parallelization techniques if posssible for the loops
    sentence_count = 0
    
    #Try to find other useful statistics like: avg word length, most used word


    #Further implementations: searching specific words (like the line of appearance/index?)

    #CHATGPT suggestions - ^,generating word clouds, or analyzing sentiment of text
    #Test your script with various text files to ensure its robustness and handle different edge cases
    curr.close()
    '''