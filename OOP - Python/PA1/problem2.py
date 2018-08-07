# Amandeep Singh Ruid 145003464

def ubbidubbi_word(eword): #converts word to ubbi dubbi
    new_word='' #word to return
    word_length=len(eword)
    char_counter=0
    is_prev_vowel=0
    for character in eword:
        if(character=='a' or character=='e' or character=='i' or character=='o' or character=='u' or character=='y'): #if wovel
            if(character=='e' and char_counter==word_length-1 ): #if it is e and last character
                new_character=character #keep as it is
                is_prev_vowel=0 #mark that this one was not changed
            elif(is_prev_vowel==0): #if previous was not vowel and this one is
                new_character='ub'+character #replace this
                is_prev_vowel=1
            else:
                new_character=character
                is_prev_vowel=0
            if(character=='a' or character=='e' or character=='i' or character=='o' or character=='u' or character=='y'): #check if vowel is not marked as 0
                if(is_prev_vowel==0):
                    is_prev_vowel=1 # mark it 1
        else:
            new_character=character
            is_prev_vowel=0
        char_counter=char_counter+1
        new_word=new_word+new_character #append to new word
    return new_word


def ubbidubbi_sentence(esentence): #takes a sentence and returns translated 
    translated_sentence=''
    for word in esentence.split(' '):
        translated_sentence=translated_sentence+' '+ubbidubbi_word(word) #call the word by word translator by splitting at ' '
    return translated_sentence

def ubbidubbi_translator():
    print('Ubbi Dubbi Translator') #starting message
    choice='y' #starting choice
    while(choice=='y' or choice=='Y'): # run till user enters y
        sentence=input('Enter the English sentence:')
        print('Translation : ' + ubbidubbi_sentence(sentence)) #print the output
        choice=input('Do another? [y/n] : ')
    print('gubo ubin pubeace! guboodbubye!')
    
