#Amandeep Singh Ruid 145003464
def create_dictionary(idfilename, hwfilename, qzfilename, examfilename):
    ''' Creates a dictionary with key as student id and value is again a dictionary woth 3 keys
    hw,quiz and exam scoring scores as list '''
    score_dictionary={}
    
    file=open(idfilename,'r')
    for line in file:
        score_dictionary[line.replace('\n','')]={'hw':[],'quiz':[],'exam':[]}  #read student id
    file.close()
    

    file=open(hwfilename,'r')
    for line in file:
        if(line.replace('\n','')==''):
            continue
        student_id=line.split()[0]
        score_dictionary[student_id]['hw'].append(int(line.split()[1])) #read hw data
    file.close()
    
    file=open(qzfilename,'r')
    for line in file:
        if(line.replace('\n','')==''):
            continue
        student_id=line.split()[0]
        score_dictionary[student_id]['quiz'].append(int(line.split()[1])) #read quiz data
    file.close()

    file=open(examfilename,'r')
    for line in file:
        if(line.replace('\n','')==''):
            continue
        student_id=line.split()[0]
        score_dictionary[student_id]['exam'].append(int(line.split()[1])) #read exam data
    file.close()

    return score_dictionary
    

def create_graderoster(sdata_dict,outputfilename):
    ''' Calcluates stats and writes to roster file'''
    student_roster={} # dictionary where key is student_id and value is list [hw,quiz,exam,final_total,grade]
    
    for student_id in sdata_dict.keys():

        student_roster[student_id]=[]

        final_hw_score=0
        hw_scores=sdata_dict[student_id]['hw'] #set final hw score
        hw_scores=hw_scores[0:4]
        num_zero=len(hw_scores)-4
        for j in range(0,num_zero):
            hw_scores.append(0)
        hw_scores.remove(min(hw_scores))
        final_hw_score=round(float(sum(hw_scores)/10.0),2)
        student_roster[student_id].append(final_hw_score)

        final_quiz_score=0
        quiz_scores=sdata_dict[student_id]['quiz']
        quiz_scores=quiz_scores[0:8]
        num_zero=len(quiz_scores)-8
        for j in range(0,num_zero):
            quiz_scores.append(0)
        quiz_scores.remove(min(quiz_scores))
        quiz_scores.remove(max(quiz_scores))
        final_quiz_score=round(float(sum(quiz_scores)/10.0),2) #set final quiz score
        student_roster[student_id].append(final_quiz_score)

        final_exam_score=0
        exam_scores=sdata_dict[student_id]['exam']
        exam_scores=exam_scores[0:2]
        num_zero=len(exam_scores)-2
        for j in range(0,num_zero):
            exam_scores.append(0)
        final_exam_score=round(float(sum(exam_scores)/10.0),2) #ste final exam score
        student_roster[student_id].append(final_exam_score)

        total_score=round(final_hw_score+final_quiz_score+final_exam_score,2)
        student_roster[student_id].append(total_score)

        if(total_score>=90.0): #assign grade
            grade='A'
        elif(total_score>=85.0):
            grade='B+'
        elif(total_score>=80.0):
            grade='B'
        elif(total_score>=75.0):
            grade='C+'
        elif(total_score>=70.0):
            grade='C'
        elif(total_score>=60.0):
            grade='D'
        else:
            grade='F'

        student_roster[student_id].append(grade) #set grade
    max_hw=0
    min_hw=30
    avg_hw=0

    max_quiz=0
    min_quiz=30
    avg_quiz=0

    max_exam=0
    min_exam=40
    avg_exam=0

    f=open(outputfilename,'w') #write the roster
    f.write('%s' % ('RUID'.ljust(14)) + '' + '%s' % ('HW(30)'.rjust(10))+ '%s' % ('QUIZ(30)'.rjust(10)) + '%s' % ('EXAM(40)'.rjust(10)) + '%s' % ('TOTAL(100)'.rjust(12)) + '%s' % ('GRADE'.rjust(10)) + '\n')
    f.write('-'*(14+10+10+10+12+10+7)+ '\n')
    for studentid in list(student_roster.keys()):
        scores=student_roster[studentid]
        if(scores[0]>max_hw):
            max_hw=scores[0]
        if(scores[0]<min_hw):
            min_hw=scores[0]       
        avg_hw=avg_hw+scores[0]/len(student_roster.keys())



        if(scores[1]>max_quiz): #calculate stats
            max_quiz=scores[1]
        if(scores[1]<min_quiz):
            min_quiz=scores[1]       
        avg_quiz=avg_quiz+scores[1]/len(student_roster.keys())



        if(scores[2]>max_exam):
            max_exam=scores[2]
        if(scores[2]<min_exam):
            min_exam=scores[2]       
        avg_exam=avg_exam+scores[2]/len(student_roster.keys())


        
        f.write('%s' % (studentid.ljust(14)) + '' + '%s' % (str(scores[0]).rjust(10))+ '%s' % (str(scores[1]).rjust(10)) + '%s' % (str(scores[2]).rjust(10)) + '%s' % (str(scores[3]).rjust(12)) + '%s' % (str(scores[4]).rjust(10)) + '\n')

    f.write('\n')
    f.write('Maximum Homework Score : ' + str(max_hw)+ '\n') #write stats
    f.write('Minimum Homework Score : ' + str(min_hw)+ '\n')
    f.write('Average Homework Score : ' + str(avg_hw)+ '\n')


    f.write('Maximum Quiz Score : ' + str(max_quiz)+ '\n')
    f.write('Minimum Quiz Score : ' + str(min_quiz)+ '\n')
    f.write('Average Quiz Score : ' + str(avg_quiz)+ '\n')

    f.write('Maximum Exam Score : ' + str(max_exam)+ '\n')
    f.write('Minimum Exam Score : ' + str(min_exam)+ '\n')
    f.write('Average Exam Score : ' + str(avg_exam)+ '\n')


    f.close()
    

if __name__  == "__main__": #call the functions
    score_dictionary=create_dictionary('studentids.txt','hwscores.txt','quizscores.txt','examscores.txt')
    create_graderoster(score_dictionary,'graderoster.txt')
