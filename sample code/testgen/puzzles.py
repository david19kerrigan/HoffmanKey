import random
sixtoseven = 1;

def puzzle0(initvals,escapeseq):
    return initvals == escapeseq

def puzzle2(posedge):
    return posedge in ["yes","y","YES","Y"]

def puzzle3(mac):
    return "//place \"`define " + mac +"\" in your code to run this test"

def puzzle4(normlogic):
    return "enter wire sizes of inputs and outputs ie. A,B 1 C 2 D,E 3 : "

def puzzle5(logicstring):
    return logicstring.split(" ")

def puzzle6(logicstring):
    return 
