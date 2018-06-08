
#testgen.py - makes a test module FOR YOU in verilog

#global vars 
tab = "    "
tm=0#tab multiplier

#functions

#iterates through a posedge
def testiter():
    global file
    global tm
    global tab
    escapeseq = "XXX"
    example = "what vals to change? ie A 1 B 0 C[1:0] 2?"
    exit = "type \""+escapeseq+"\" to finish : "
    initvals = raw_input(example + exit)
    if initvals == escapeseq : return False                             #puzzle0
    vals = initvals.split(" ")
    for i in range(len(vals)//2):
        wr(vals[2*i] + "<=" + vals[2*i+1]+";")
    wr("@(posedge clock);")
    return True                                                         #puzzle1 A

#writes a string with good tabbing
def wr(string):
    global file
    global tm
    global tab    
    file.write(tm*tab +string+"\n")


#Actual Script

#Opens file that user typed.
title = raw_input("enter name of file to edit or create : ")
file = open(title,"a")  
posedge = raw_input("If you only want to make a few posedges type \"yes\" now. Otherwise press enter : ")
if (posedge in ["yes","y","YES","Y"]):                                  #puzzle2 A
    while testiter() : continue
else : 
    #Makes Test Module Header
    file.write("\n")
    mac = raw_input("enter test module macro : ")
    testmodule = raw_input("enter test module name ie. additionTester : ")
    tm=0
    wr("//place \"`define " + mac +"\" in your code to run this test")  #puzzle3 A
    wr("`ifdef "+ mac )
    wr("module {}();".format(testmodule))
    tm=1

    #Gets Module name params, input and output logic
    module = raw_input("enter module to be tested ie. adder #(3) addy : ")
    ins = raw_input("enter inputs and outputs in order ie. A,B,C,D : ")

    #Makes the input and output logic
    normlogic = "logic clock,reset;"
    wr(normlogic)
    logicstring = raw_input("enter wire sizes of inputs and "+          #puzzle4 A
        "outputs ie. A,B 1 C 2 D,E 3 : ")
    logiclist = logicstring.split(" ")                                  #puzzle5 A
    for i in range(len(logiclist)//2):
        one = 1;
        logicvars = logiclist[2*i]
        logicwires = int(logiclist[2*i+1]) - one                        #puzzle6
        wirestring = " "
        #identify quantity of wires
        if (logicwires != 0): wirestring = "["+str(logicwires)+":0] "
        if (logicwires == 0): logicvars = logicvars.replace("clock",",").replace("reset",",").replace(",,","")  #puzzle7
        if (logicvars == ",") : wr("logic"+wirestring + logicvars+";")
        
    #Makes the module
    module = module + "({});".format(ins)
    wr(module)

    #Makes the clock go forever
    wr("initial begin")
    tm = 2
    wr("clock=0;")
    wr("// Initialize the clock to 0")
    wr("forever #10 clock = ~clock; // Every #10, invert the clock")    #puzzle8
    tm = 1
    wr("end")
    wr("initial begin")

    #Sets up monitor and display statements
    variables = raw_input("enter comma sep. vars to monitor ie. A,B,C,D : ")
    varlist = variables.split(",")
    formatpart = "\""
    for v in varlist:
        formatpart = formatpart + v + " : " + "%d, "
    formatpart = formatpart + "\","
    tm=2
    wr("$display(\"" + testmodule + "\");")
    wr("$monitor($time,,"+formatpart+variables+");");                   #puzzle9

    #Flips the reset up and down at the start    
    wr("reset <= 1;")
    wr("// reset the FSM")
    wr("@(posedge clock); // wait for a positive clock edge")
    wr("@(posedge clock); // one edge is enough, but what the heck")
    wr("@(posedge clock);")
    wr("reset<=0;")

    #Posedges - this is where the actual testing is
    while testiter() : continue

    #Closing up the module
    wr("#1 $finish;")
    tm=1
    wr("end")
    tm=0
    wr("endmodule: "+testmodule)
    wr("`endif")
    
file.close()


        

