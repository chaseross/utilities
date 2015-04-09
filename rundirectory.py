#This file goes to the new directory, runs latex on a .tex file, then outputs it as a pdf
#Then, the script will copy and paste the pdf from the working directory to the new directory. 


import sys
import os.path
import shutil


path = os.getcwd()
sourcepath = os.path.dirname(path) 

outputpath = os.path.join(sourcepath, "output")
os.chdir(path)



import os, shutil
folder = outputpath
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception, e:
        print e


os.system("rscript Sample_graph.R")



for line in os.popen("latexmk -pdf outline", "r"):
	sys.stdout.flush()
	
shutil.move('outline.pdf', outputpath) 
shutil.move('outline.aux', outputpath)
shutil.move('outline.fdb_latexmk', outputpath)
shutil.move('outline.fls', outputpath)
shutil.move('outline.out', outputpath)
shutil.move('outline.log', outputpath)
