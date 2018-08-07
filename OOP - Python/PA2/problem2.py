#Amandeep Singh Ruid 145003464
def remove_extra_whitespaces(infile,outfile):
    ''' Removes white spaces '''
    f=open(infile)
    f2=open(outfile,'w')
    for line in f:
        if line=='\n':
            continue
        formatted_line=' '.join(line.split())+'\n\n'
        f2.write(formatted_line)
    f.close()
    f2.close()


def adjust_linelength(infile,outfile):
    ''' Restrict length of line to 60 characters'''
    f=open(infile,encoding='utf-8')
    f2=open(outfile,'w')
    data=f.read().split('\n')
    #print(data)
    for line in data:
        if len(line)==0:
            continue
        formatted_line=''
        char_counter=0
        for word in line.split():
            if(char_counter+len(word+' ')<=60): #space available for more on this line
                formatted_line=formatted_line+word+' '
                char_counter=char_counter+len(word)
            else:
                formatted_line=formatted_line+'\n'+word+' ' #60 char over
                char_counter=0
                char_counter=char_counter+len(word)
        #print(formatted_line)
        f2.write(formatted_line)
        f2.write('\n\n')
                
        
    f.close()
    f2.close()

def essay_stats(infile,outfile):
    '''finds and writes stats for essay'''
    f=open(infile)
    f2=open(outfile,'w')
    non_blank_lines=0
    num_words=0
    sum_word_len=0
    avg_word_len=0
    for line in f:
        if line!='\n':
            non_blank_lines=non_blank_lines+1
            num_words=num_words+len(line.split()) #get stats
            for word in line.split():
                #print(word)
                #print(len(word))
                sum_word_len=sum_word_len+len(word)
    avg_word_len=sum_word_len/(1.0*num_words)
    f2.write('In the file essay.txt' + '\n\n')
    f2.write('Number of (non-blank) lines : ' + str(non_blank_lines)+'\n')
    f2.write('Number of words : ' + str(num_words)+'\n')
    f2.write('Average of word length : ' + str(avg_word_len)+'\n')
        

def format_essay():
    '''Calls all functions in order'''
    file_name=input('Enter file containing essay : ')
    remove_extra_whitespaces(file_name,file_name[0:-4]+'_neb.txt')
    print(file_name[0:-4]+'_neb.txt'+ '   Created')
    adjust_linelength(file_name[0:-4]+'_neb.txt',file_name[0:-4]+'_final.txt')
    print(file_name[0:-4]+'_final.txt'+'   Created')
    essay_stats(file_name[0:-4]+'_final.txt',file_name[0:-4]+'_stats.txt') 
    print(file_name[0:-4]+'_stats.txt'+ '   Created')
          
if __name__=='__main__': #call functions
    format_essay()
