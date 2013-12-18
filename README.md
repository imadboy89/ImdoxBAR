ImdoxBAR
========

Progress Bar in console mode, with this utile script you can now show your progress like professionals .
you can show a progressbar in the terminal in a very easy way .
an  animated loading added now ;) .

usage :
import it like : import ImdoxBAR
initialise it like : progbar = PrgBar(total) || while total  is the total of progress
put the progress bar updater in the loop where you doing your
treatment like : progbar.update(i)  || while 'i' is the current progress
see last condition (main="__main__") ; you can try it .

p = PrgBar(X)  // x is the total processes 
p.loadingBar()  // will update the loading thing
 OR p.update(i) // will update the progress bar with i the process achivied
