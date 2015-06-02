__author__ = 'ilya_rubinshteyn'

def interview_schedule():
    time = 12
    while time != 0:
        interviewer = input("Who holding the interview? ")
        applicant = input("Who is the applicant? ")
        time = input("At what time will the interview take place? ")
        day = input("What day will the interview take place? ")
        default_text = "{} will interview {} at {} on {}."
        output_text = default_text.format(interviewer,applicant,time,day)
        print("")
        print(output_text)
        print("%s will interview %s at %s on %s."%(interviewer,applicant,time,day))
        print("{} will interview {} at {} on {}.".format(interviewer,applicant,time,day))
        print(interviewer," will interview ",applicant," at ",time," on ",day,".", sep="")

        break
interview_schedule()
