
def create_grades_file(infilename, outfilename):
    """
    Read exam scores (3 per student) from infilename and write 
    letter grade for each student in outfilename.

    infilename: name of file to be read (a string)
    outfilename: name of file to be written (a string)
    """
    infile = open(infilename, 'r')
    outfile = open(outfilename, 'w')

    for line in infile:
        L = line.split()
        total_score = (int(L[1]) + int(L[2]) + int(L[3])) // 3
        if total_score >= 90:
            grade = 'A'
        elif total_score >= 80:
            grade = 'B'
        elif total_score >= 70:
            grade = 'C'
        elif total_score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        # outfile.write(L[0] + "   " + str(total_score) + "   " + grade + "\n")

        # Note that total score and letter grades may not be aligned by column

        # Rewrite above using string formatting
        outfile.write("%-16s %4d %3c\n"%(L[0], total_score, grade))

    infile.close()
    outfile.close()
    
