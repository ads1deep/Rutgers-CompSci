
#Amandeep Singh  Ruid 145003464

def evaluate_essay(essayfilename): #evaluates essay as per elvel
    short_words=0 #num of short words
    medium_words=0 #num of medium words
    long_words=0 #num of long words
    num_words=0 # num of all words
    level_essay='' #level of essay
    file_handle=open(essayfilename,'r')
    text=file_handle.read().replace('\n',' ').replace('\t',' ') #handle new line and tabs
    for word in text.split(' '): #browse word by word
        num_words=num_words+1
        if len(word)>=1 and len(word)<=3:
            short_words=short_words+1 #short word
        elif(len(word)>=4 and len(word)<=6):
            medium_words=medium_words+1 #medium word
        elif(len(word)>=7):
            long_words=long_words+1 #long word
    file_handle.close() #close file
    if(long_words>=round(num_words/2)): #classify level
        level_essay='college level'
    elif(long_words>=short_words and long_words>=medium_words):
        level_essay='high school level'
    elif(medium_words>=short_words and medium_words>=long_words):
        level_essay='middle school level'
    elif(short_words>=medium_words and short_words>=long_words):
        level_essay='elementary school level'
    print('The level of essay is : ' + level_essay) #print level
         
    
        
