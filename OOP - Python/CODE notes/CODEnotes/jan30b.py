def max_scores(gradesfile, maxscoresfile):
    """
    Read exam scores (3 per student) from gradesfile and write the 
    maximum total score and maximum exam score for each exam into 
    maxscoresfile.

    gradesfile: name of file to be read
    maxscoresfile: name of file to be written
    """
    gfile = open(gradesfile, 'r')
    sfile = open(maxscoresfile, 'w')

    # masterlist is a list of lists. Each element of the list contains
    # one line of the file, which is split into a list.

    masterlist = [line.split() for line in gfile]


    maxtotal = max([int(item[1]) + int(item[2]) + int(item[3]) for item in masterlist])
    maxexam1 = max([int(item[1]) for item in masterlist])
    maxexam2 = max([int(item[2]) for item in masterlist])
    maxexam3 = max([int(item[3]) for item in masterlist])
    
    sfile.write(" Max total score: %5d\n"%(maxtotal))
    sfile.write("Max Exam 1 score: %5d\n"%(maxexam1))
    sfile.write("Max Exam 2 score: %5d\n"%(maxexam2))
    sfile.write("Max Exam 3 score: %5d\n"%(maxexam3))

    gfile.close()
    sfile.close()
    
    
