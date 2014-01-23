##Progress Bar in console mod .
##usage :
##import it like : import progBar
##initialise it like : progbar = PrgBar(total) || while total  is the total of progress
##put the progress bar updater in the loop where you doing your
##treatment like : progbar.update(i)  || while i is the current progress
##see last condition (__name__="__main__") ; you can try it .
###############################################################################################
import time,sys
from math import ceil
from datetime import datetime,timedelta

class PrgBar():

    def __init__(self,total,step=10,prgBat_char="="):
        self.prgBar_char = prgBat_char
        self.step = step
        self.total = total
        self.k=self.ww=self.type=self.round=0
        self.prcs=[]
    def setup(self):
        sys.stdout.write("[%s]" % (" " * (self.step*2+1)))
        sys.stdout.flush()
        sys.stdout.write("\b" * (self.step*2+2)) # return to start of line, after '['

    def update(self,i,desc=""):
        if i == self.total/self.step*self.k :
            sys.stdout.write("\b" * (self.step*2+4+self.k))
            print "[%s%s]\t%s"%(self.prgBar_char*(self.k)," "*(self.step-self.k+2),ceil(((i+1)/float(self.total))*100)),
            print "%",
            if desc!="":
                print "[%s]"%desc,

            self.k+=1
            self.prcs.append(i)
            sys.stdout.flush()

    def loadingBar(self):
        now = datetime.now()
        dd = timedelta(0,0.1)
        try:
            if now -dd > self.lasttime :
                if self.type == 0: sys.stdout.write("\b/")
                if self.type == 1: sys.stdout.write("\b-")
                if self.type == 2: sys.stdout.write("\b\\")
                if self.type == 3: sys.stdout.write("\b|")
                self.type += 1
                if self.type == 4: self.type = 0
                sys.stdout.flush()
                self.lasttime = now
        except AttributeError ,e:
            print "%s\n"%e
            self.lasttime = now
            sys.stdout.write("Loading...  ")
            sys.stdout.flush()






###########################################
###        usage :  #######################
##p = PrgBar(X)  // x is the total processes 
##p.loadingBar()  // will update the loading thing
## OR p.update(i) // will update the progress bar with i the process achivied
if __name__ == "__main__":
    p = PrgBar(5230,50)
    for i in range(5230):
        #p.update(i)
        p.loadingBar()
        time.sleep(0.005)
