#speed formula = 0.2083 miles or 1100ft  per 1 second
def lightningStrike():
        for i in range(10):
                t = float(input("input time here:"))
                s = 1100/1
                d = t*s
                d_in_miles = d/5280
                #print("speed of lightning= ",s)
                #print("distance of lightning = ",d,"feet")
                print(t,"seconds of delay, may indicate the Lightning Strike was about",d_in_miles,"miles away")

lightningStrike()
