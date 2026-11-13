import argparse
import time

def timer(revisetime,breaktime):
    rUnit = revisetime[-1]
    bUnit = breaktime[-1]
    rRevisetime = int(revisetime[:-1])
    rBreaktime = int(breaktime[:-1])
    rRevisetime = correctUnit(rUnit, rRevisetime)
    rBreaktime = correctUnit(bUnit, rBreaktime)

    while True:
        startTime = time.perf_counter()
        
        breakStartTime = startTime + rRevisetime
        breakEndTime = breakStartTime + rBreaktime
        
        revisionLine = "Revision time! Remaining: " + prettyPrint(int(breakStartTime - time.perf_counter()))
        breakLine = "Break time! Remaining: " + prettyPrint(int(breakEndTime - time.perf_counter()))
        
        lineLength = max(len(revisionLine),len(breakLine))
        lineClearer = " "*lineLength
        
        while time.perf_counter() < breakEndTime:
            revisionLine = "Revision time! Remaining: " + prettyPrint(int(breakStartTime - time.perf_counter()))
            breakLine = "Break time! Remaining: " + prettyPrint(int(breakEndTime - time.perf_counter()))
            print(lineClearer,end='\r')
            if time.perf_counter() < breakStartTime:
                print(revisionLine,end='\r')
            else :
                print(breakLine,end='\r')
            time.sleep(1)

def correctUnit(unit, time):
    if unit == "s" : return time
    elif unit == "h" : return time*3600
    else : return time*60

def prettyPrint(time):
    if time < 60 :
        if time > 9 : return str(time)
        return "0"+str(time)
    if time < 3600 :
        rem = time % 60
        time = int((time-rem)/60)
        if time > 9 :  return str(time)+":"+prettyPrint(rem)
        return "0"+str(time)+":"+prettyPrint(rem)
    else : 
        rem = time % 3600
        return str(int((time-rem)/3600))+":"+prettyPrint(rem)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("revisetime",
                        help="Time to revise before a break")
    parser.add_argument("breaktime",
                        help="Length of break between revision chunks")
    args = parser.parse_args()
    timer(args.revisetime,args.breaktime)
