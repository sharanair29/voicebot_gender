
from STTvoice import *
from Predict import *

import time

from subprocess import Popen, PIPE



def run_R(file):
    # COMMAND WITH ARGUMENTS
    cmd = ["Rscript", "/Users/hlabs/Desktop/hoop/voicebot/gendervoice/ExtractFeatures.R", file]

    p = Popen(cmd, cwd="/Users/hlabs/Desktop/hoop/voicebot/gendervoice/",      
                stdin=PIPE, stdout=PIPE, stderr=PIPE)     
    output, error = p.communicate()

    # PRINT R CONSOLE OUTPUT (ERROR OR NOT)
    if p.returncode == 0:            
        print('R OUTPUT:\n {0}'.format(output))            
    else:                
        print('R ERROR:\n {0}'.format(error))




def gender():

    record()

    time.sleep(4) # I assigned a 4 second sleep period to avoid the code to overwrite itself and ExtractFeatures to run on the previously generated wav file

    run_R(file = "/Users/hlabs/Desktop/hoop/voicebot/gendervoice/ExtractFeatures.R")

    run()


gender()