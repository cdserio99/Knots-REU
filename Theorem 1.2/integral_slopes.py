'''''''''''''''''''RULING OUT INTEGER CHARACTERISTIC SLOPES'''''''''''''''''''
#@gsagostini
#Last updated: 07/03/2019

##############################################################################
'''''''''''''''''''''''''''''''Packages'''''''''''''''''''''''''''''''''''''

import math
import time
import os
import subprocess
from pynput.keyboard import Key, Controller #Downloaded from Github
import win32gui                             #Package specific to Windows
import sys

##############################################################################
''''''''''''''''''''''''''''''''''Input'''''''''''''''''''''''''''''''''''''''

#Path to the SnapPy application. Note that the default output directory should
# be the directory of the script in order for it work.
SnapPy = "C:\Program Files (x86)\SnapPy\SnapPy.exe"

#List of DT Codes for links L = K U R U G that fit Piccirillo's algorithm,
# isotoped so that G is a simply meridian to the one-handle component R.
DT_List = "DT_List.txt"

##############################################################################
'''''''''''''''''''''''''''''Functions & Classes'''''''''''''''''''''''''''''

class Knot(object):
    def __init__(self, name, DT):
        self.name = str(name)
        self.one_handle = get_onehandle(DT)
        self.DT = str(DT)
        self.status = "Not tested"
        self.char_slopes = []
    def __str__(self):
        return "Knot " + self.name
    
def get_onehandle(DT_str):
#Input: a DT code string
    #Determines which component is the 1-handle, assuming it is unkonetted.
    if ",)" in DT_str:
        #Formats the DT code for this function.
        i = DT_str.index(",)")
        DT_str = DT_str[:i] + DT_str[i+1:]
    #Each component corresponds to a tuple in the DT code. In our string, the
    # tuples are separated by the ")" character.
    breaks = []
    for index in range(len(DT_str)):
        if ")" in DT_str[index:(index + 1)]:
            breaks.append(index)
    #The number of crossings in each component corresponds to the number of
    # integers on the DT-tuple. We count them by counting the commas.
    lengths = []
    lengths.append(DT_str.count(",",0, breaks[0]) + 1)
    lengths.append(DT_str.count(",", breaks[0] + 2, breaks[1]) + 1)
    lengths.append(DT_str.count(",", breaks[1] + 2) + 1)
    #The meridian will have a tuple of length 1 since it has only one crossing
    # and the knot K will have the longest tuple since it has crossings with
    # itself plus crossings with the 1-handle.
    meridian = lengths.index(1)
    k_knot = lengths.index(max(lengths))
    #The remaining integer is the length of the 1-handle tuple, and we want
    # its index (which in SnapPy corresponds to the component number).
    for cpt in (0,1,2):
        if cpt != meridian and cpt != k_knot:
            return cpt

def get_knotlist(filename):
#Input: name and DT code of a knot, strings
    #Initiates each line of the file as an instance of the class Knot, and 
    # adds all the Knot objects to a list.
    print("Converting the DT Code list...")
    #The DT Code list must be formatted as name#DTcode, with only one knot per
    # line. The DT Code should be in the format given by SnapPy.
    f = open(filename, "r")  
    knotlist = []
    for line in f:
        if ",\n" in line:
            knot = line.strip(",\n")
        else:
            knot = line.strip("\n")
        knot_fields = knot.split("#")                
        knot = Knot(knot_fields[0], knot_fields[1])
        knotlist.append(knot)
    f.close()
    return knotlist

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
 
def ToFront(window):
#Input: window name, string    
    #Brings a window to the foreground so that keyboard commands apply to it.
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if window in i[1]:
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break

def SnapPy_runandsave(filename, path, t=1.8):
#Input: Name of file to be open, location of SnapPy in the OS, time for the
#       commands to run [default for quick files].
    #Tells SnapPy to open a certain file, running its lines, and then saves a
    # file with the output.
    p = subprocess.Popen([path])
    time.sleep(2)
    ToFront("SnapPy")
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press("o")
    keyboard.release(Key.ctrl)
    keyboard.release("o")
    ToFront("Open file")
    keyboard.type(filename)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(t)
    #Sleeping time corresponds to the time for SnapPy to run the commands. It
    # should be greater given the complexity of the knot. For the INFO files, 
    # the default 1.8 second is usually enough.
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press("s")
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release("s")
    keyboard.type("[OUT] " + filename)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    p.terminate()

def infofile_writing(knot, one_hdle, DT):
#Input: Name of a knot (string), number of the one-handle component in SnapPy,
#       DT code as it runs on SnapPy.
    #Writes a .py file to be run by SnapPy that outputs the volume of the
    # manifold obtained by zero-filling on the one-handle component, the
    # volume of the exterior of a knot K, and the length of the 0-slope.
    try:
        f = open(knot + " [INFO].py", "x")
    except FileExistsError:
        os.remove(knot + " [INFO].py")
        f = open(knot + " [INFO].py", "x")
    f.write("X = Manifold('DT:" + DT + "')\n")
    f.write("X.dehn_fill((0,1)," + str(one_hdle) + ")\n")
    f.write("Z = X.filled_triangulation()\n")
    #f.write("Z.solution_type()\n")
    f.write("Kverify = Z.copy()\n")
    f.write("Kverify.dehn_fill((0,1),1)\n")
    f.write("Kfill = Kverify.filled_triangulation()\n")                
    #f.write("Kfill.solution_type()\n")                
    f.write("Kfill.identify()\n")                
    f.write("Kfill.volume()\n")
    f.write("Z.volume()\n")
    f.write("Z.cusp_translations()\n")
    f.close()
    
def get_info(knot):
#Input: Name of a knot (string) as it was saved on the output file.
    #Reads the info file outputted by SnapPy and collects the information.
    length_prime, Z_vol, Kfill_vol = False, False, False
    DT = True
    try: 
        f = open("[OUT] " + knot + " [INFO].py", "r")
    except FileNotFoundError:
        print("Could not find [OUT] [INFO] file.")
        return 0
    for line in f:
        if DT == True:
            if "Kfill.identify()\n" == line:
                if "#" not in next(f):
                    DT = False
                    print("There is a problem with this DT code.")
            elif "Kfill.volume()\n" == line:
                try: Kfill_vol = float(next(f).strip("#").strip("\n"))
                except: print("Could not find volume of K")                            
            elif "Z.volume()\n" == line:
                try: Z_vol = float(next(f).strip("#").strip("\n"))
                except: print("Could not find volume of Z")                   
            elif "Z.cusp_translations()\n" == line:
                try: length_prime = float(next(f).split(", ")[1].strip(")"))                        
                except: print("Could not find the Seifert longitude length")
    f.close()
    return (length_prime, Z_vol, Kfill_vol, DT)

def upper_bound(length, Z_vol, Kfill_vol):
#Input: Length of a slope m on a boundary component of a hyperbolic 3-manifold,
#       the volume of this manifold, the volume of the manifold K obtained by
#       surgery along m.
    #Using a discussed theorem, takes the information collected to calculate 
    # a boundary slope C for which any slope greater than C is characterizing.
    b1 = math.sqrt(3)/length
    b2 = (2*math.pi)/(math.sqrt(1 - ((Kfill_vol/Z_vol)**(2/3))))
    print("The length of the (n,1)-framing of K is greater than or equal to",
          round(b1, 3), "times |n| and greater than", round(b2, 3), ".\n")
    C = math.floor(b2/b1)
    return C

def testfile_writing(knot, one_hdle, DT, C): 
#Input: Name of a knot (string), number of the one-handle component in SnapPy,
#       DT code as it runs on SnapPy, bound for the integral characterizing
#       slopes.
    #Writes a .py file to be run by SnapPy that asks for the volume of the 
    # manifolds obtained by n-surgery on the family of knots Kn' for all the 
    # values of n that we could not prove generally.
    try:
        f = open(knot + " [TEST].py", "x")
    except FileExistsError:
        os.remove(knot + " [TEST].py")
        f = open(knot + " [TEST].py", "x")
    f.write("X = Manifold('DT:" + DT + "')\n")
    f.write("X.dehn_fill((0,1)," + str(one_hdle) + ")\n")
    f.write("Z = X.filled_triangulation()\n")
    f.write("Z.solution_type()\n")
    f.write("Z.volume()\n")
    f.write("Kverify = Z.copy()\n")
    f.write("Kverify.dehn_fill((0,1),1)\n")
    f.write("Kfill = Kverify.filled_triangulation()\n")                
    f.write("Kfill.solution_type()\n")                
    f.write("Kfill.identify()\n")                
    f.write("Kfill.volume()\n")
    #Now, for each integral slope in the range [-C, C], Snappy will have to
    # run the following commands.
    for i in range (-C, C + 1):
        f.write("Z.dehn_fill((" + str(i) + ",1),0)\n")
        f.write("Knprime = Z.filled_triangulation()\n")
        f.write("Knprime.solution_type()\n")
        f.write("Knprime.volume()\n")
        f.write("Knprime.identify()\n")
    f.close()

def is_complete(knot, C):
    complete = True
    try:
        f = open("[OUT] " + knot + " [TEST].py", "r")
        lines = []
        for line in f:
            lines.append(line)
        f.close()
        if str(C) not in lines[-12]:
            complete = False
    except FileNotFoundError:
        print("Could not find file [OUT] " + knot + " [TEST].py")
        complete = None
    return complete

def ProofByHand(knot):
#Input: Name of the knot (string).
    #Runs the test file and records the results, completing the proof.
    f = open("[OUT] " + knot + " [TEST].py", "r")      
    slopes = []
    lines = []
    special = []
    i = 0
    for line in f:
        lines.append(line.strip("\n"))
        if "Kfill.volume()" in line:
            volume = float(next(f).strip("#"))
            print("The exterior of K has volume", volume, "\n")
        elif "Knprime.volume()" in line:
            volume_nprime = float(next(f).strip("#"))
            if volume_nprime <= volume or volume_nprime - volume < 0.001: 
                surgery = lines[i - 7]
                print(surgery, "yields volume", volume_nprime, "\n")
                special.append((surgery, volume_nprime, i + 3))
        i += 1
    f.close()
    if len(special) >= 1:
        if len(special) == 1:
            print("Snappy identifies this knot as:")
        else:
            print("Snappy identifies these knots respectively as:\n")
        for j in range(len(special)):
            identification = lines[special[j][2]]
            print(identification)
            if "[]" in identification:
                if abs(special[j][1]  - volume) < 0.001:
                    print("But the volume of the knot exterior matches " + 
                          "that of " + knot + ". So the slope might be " +
                          "characteristic.\n")
                    slopes.append(special[j][0][13:special[j][0].index(",")])
                else:
                     print("But the volume of the knot exterior does not " + 
                           "match that of " + knot + ". So the slope is " + 
                           "not characteristic.\n")             
            elif knot in identification:
                    print("So the slope might be characteristic.\n")
                    slopes.append(special[j][0][13:special[j][0].index(",")])
            elif "10_16" in knot:
                if "10_16" in identification:
                    print("So the slope might be characteristic.\n")
                    slopes.append(special[j][0][13:special[j][0].index(",")]) 
            else:
                    print("So the slope is not characteristic.\n")
        print("The exteriors of all other knots Kn' have greater volume " + 
              "than the exterior of K.\n")
    else:
        print("The exteriors of all knots Kn' have greater volume " + 
              "than the exterior of K.\n")
    return slopes

def clear_out(knot):
    try:
        os.remove("[OUT] " + knot + " [INFO].py")
    except FileNotFoundError:
        pass
    try:
        os.remove("[OUT] " + knot + " [TEST].py")
    except FileNotFoundError:
        pass

def algorithm(knots, path, clear=False):
    verified = 0
    failed = []
    zero = []
    one = []
    more = []
    for i in range(len(knots)):
        if clear == True:
            clear_out(knots[i])
        print ("-"*40)
        print(str(knots[i]) + "\n")
        infofile_writing(knots[i].name, knots[i].one_handle, knots[i].DT)
        SnapPy_runandsave(knots[i].name + " [INFO].py", path)
        surgery_info = get_info(knots[i].name)
        if type(surgery_info) == int:
            print("\nWe could not verify the Theorem for this knot.")
            failed.append(knots[i])
            knots[i].status = "Problem on the [INFO] file."
        elif False in surgery_info:
            print("\nWe could not verify the Theorem for this knot.")
            failed.append(knots[i])
            if surgery_info[3] == False:
                knots[i].status = "Problem on the DT code"
            else:
                if surgery_info[0] == False:
                    knots[i].status = "Problem on Z.cusp_translations()"
                elif surgery_info[1] == False:
                    knots[i].status = "Problem on the volume of Z"
                elif surgery_info[2] == False:
                    knots[i].status = "Problem on the volume of K"
        else:    
            C = upper_bound(surgery_info[0], surgery_info[1], surgery_info[2])
            print("Thus, for all integers n such that |n| > ", C, " n is " +
                  "not a characterizing slope for this knot: the exterior " + 
                  "of Kn' certainly has greater volume than the exterior " +
                  "of K. Let's check for the other " + str(2 * C + 1) + " " +
                  "integral slopes.\n")
            testfile_writing(knots[i].name, knots[i].one_handle,
                             knots[i].DT, C)
            SnapPy_runandsave(knots[i].name + " [TEST].py", path, C/2)
            k = 1
            if is_complete(knots[i].name, C) == None and k < 5:
                SnapPy_runandsave(knots[i].name + " [TEST].py", SnapPy, C*k)
                k += 1
            while is_complete(knots[i].name, C) == False and k < 5:
                os.remove("[OUT] " + knots[i].name + " [TEST].py")
                SnapPy_runandsave(knots[i].name + " [TEST].py", SnapPy, C*k)
                k += 1
            if is_complete(knots[i].name, C) != True:
                print("\nWe could not verify the Theorem for this knot.")
                knots[i].status = "Problem on the [TEST] file"
                failed.append(knots[i])
            else:
                knots[i].char_slopes.append(ProofByHand(knots[i].name))
                if len(knots[i].char_slopes) == 0:
                    print("Therefore, the knot " + knots[i].name + " has " +
                          "no integral characteristic slopes.")
                    zero.append(knots[i])
                elif len(knots[i].char_slopes) == 1:
                    print("Therefore, the knot " + knots[i].name + " has at" +
                          " most one integral characteristic slope: " +
                          str(knots[i].char_slopes[0]))
                    one.append(knots[i])
                else:
                    slopes = ""
                    for j in range(len(knots[i].char_slopes)):
                        slopes = slopes + str(knots[i].char_slopes[j]) + " " 
                    print("Therefore, the knot " + knots[i].name + " has at" +
                          " most " + str(len(knots[i].char_slopes)) + 
                          " integral characteristic slopes: " + slopes)
                    more.append(knots[i])
                knots[i].status = "Verified"
                verified += 1
    print("#"*40)
    print("\nThe program examined", verified, "out of", len(knots), "knots.")
    if len(one) != 0:
        print(len(one), "knots have at most one integer " +
              "characterizing slope.")
    if len(zero) != 0:
        print(len(zero), "knots have no possible integer " +
              "characterizing slope:")
        for knot in zero:
            print(knot.name)
    if len(more) != 0:
        print(len(more), "knots have several possible integer" +
              " characterizing slopes: ", more)
        for knot in more:
            print(knot.name)
    return failed
    
##############################################################################
    
sys.stdout = open("output.txt", "x")

trial = 1
fail = algorithm(get_knotlist(DT_List), SnapPy)
while trial < 5 and len(fail) != 0:
    print("#"*40)
    print("\nWe will try again for the knots we could not examine:")          
    fail = algorithm(fail, SnapPy, True)
    trial += 1
if len(fail) != 0:
    print("#"*40)
    print("\nPlease check individually the following knots:")
    for knot in fail:
        print(knot.name, "-", knot.status)