import numpy as np
import sys
import time
import os

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def ProvaLibreria():
    print("Qui ci vanno tutte le funzioni fastidiose!!!")

def printRed(frase):
    print '\033[1;31m'+frase+'\033[1;m'

def printRedBlink(frase):
    print '\033[1;5;31m'+frase+'\033[1;m'

def printBlink(frase):
    print "\033[5;41;32m"+frase+"\033[0m"

def raw_default(prompt,dflt=None):
    if dflt:
        prompt = "%s [%s]: "% (prompt,dflt)
    response = raw_input(prompt)
    if not response and dflt:
        return dflt
    else:
        return response

def raw_defaultRed(prompt,dflt=None):
    if dflt:
        prompt = "%s [%s]: "% (prompt,dflt)
    response = raw_input("\033[1;31m"+prompt+"\033[1;m")
    if not response and dflt:
        return dflt
    else:
        return response

def MAD(vector):
    return np.median(np.fabs(vector - np.median(vector)))

def MAD30(vector):
    scarti = np.fabs(vector - np.median(vector))
    return np.sort(scarti)[int(round(len(vector)*0.30))]

def MAD_perc(vector,perc=0.30):
    scarti = np.fabs(vector - np.median(vector))
    return np.sort(scarti)[int(round(len(vector)*perc))]

def Dots(frase="Loading",num_point=3):
    for x in range(0,num_point+1):
        sys.stdout.write("\r"+frase+ "."*x)
        sys.stdout.flush()
        time.sleep(1)

def YesNo(question,dfl="n"):
    answer = str(raw_defaultRed(question + " y/n ",dfl))
    if answer == "y" or answer=="yy" or answer=="yes":
        statement = True
    else:
        statement =False
    return statement

def createPath(stringa,verbose=False):
    '''it does not return any objects but it only create the folders contained in the stringa parameter'''
    '''PLEASE, BE CAREFULL THAT IT WORKS ONLY FROM THE CURRENT FOLDER'''
    def splitPath(percorso):
        '''returns a vector of strings containing the folder to create'''
        folders = []
        folder = ""
        for i in range(len(percorso)):
            if (percorso[i]== "/" ):
                folders.append(folder)
                folder = ""
            else:
                folder = folder + percorso[i]
                if i == len(percorso)-1:
                    folders.append(folder)
        return folders
    elenco_cartelle = splitPath(stringa)
    if elenco_cartelle[0]==".":
        toDoPath = "."
    else:
        toDoPath = "./"+elenco_cartelle[0]
    if not os.path.isdir(toDoPath):
            os.mkdir(toDoPath)
    if verbose:
        printRed(elenco_cartelle[0])
    for i in range(1,len(elenco_cartelle)):
        if verbose:
            printRed(elenco_cartelle[i])
        toDoPath = toDoPath+"/"+elenco_cartelle[i]
        if not os.path.isdir(toDoPath):
            os.mkdir(toDoPath)
    return stringa
