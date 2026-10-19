# description: Full song, needs inputs
from earsketch import *

def drums(start, end, style):
    set = [ OS_CLAP01, OS_KICK05, OS_CLOSEDHAT02]
    if style == "hard":
        kc_beat = "0-10-0110-10-011"
        h_beat = "2-2-2-2-2-2-2-2-"
    elif style == "mid":
        kc_beat = "0-10-0--0-10-0--"
        h_beat = "--2---2---2---2-"
    else:
        kc_beat = "0-10----0-10----"
        h_beat = "--2+--2+--2+--2+"
    for i in range(start, end):
        makeBeat(set, 2, i, kc_beat)
        makeBeat(set, 3, i, h_beat)
        setEffect(2, VOLUME, GAIN, -5)

def sections(start, style):
    #sfx all
    melody = {"piano": "p", "guitar": "g", "bg": "z", "vocal" : "v" }
    if style == "verse1":
        #guitar, synth
        fitMedia(melody["bg"], 2, start, start + 5)
        drums(start, start + 10, "mid")
    elif style == "verse2":
        #synth, vocal
        drums(start, start + 10, "mid")
    elif style == "chorus":
        #guitar, synth, vocal
        drums(start, start + 10, "hard")
            

    
def practice():
    setTempo(120)
    drums(1, 20,"hard")

def main():
    setTempo(120)
    transitions = [OS_OPENHAT01,HOUSE_SFX_WHOOSH_011,]
    sfx = []
    melody = {"piano": "p", "guitar": "g", "bg": "z", "vocal" : "v" }
    #intro
    fitMedia(melody["piano"], 1, 1, 10)
    fitMedia(melody["bg"], 1, 5, 10)
    fitMedia(melody["guitar"], 1, 10, 15)
    drums(15, 20,"easy")
    #verse1
    sections(20, "verse1")
    #first chorus
    sections(30, "chorus")
    #verse2
    sections(40, "verse2")
    #prechorus
    fitMedia(melody["bg"], 2, 40, 50)
    fitMedia(melody["vocal"], 1, 45, 50)
    drums(45, 50, "easy")
    #(loud)chorus
    sections(50, "chorus")
    setEffect(10, VOLUME, GAIN, 10)
    #bridge
    fitMedia(melody["solo"], 1, 60, 70) #review
    drums(60, 70, "easy")
    #chorus
    sections(70, "chorus")
    #outro
    drums(80,84, "hard")
    drums(84,86, "mid")
    drums(86, 88, "easy")
    fitMedia(melody["vocal"], 1, 80,90)
    fitMedia(melody["guitar"], 2, 80,85)

#Program running
main()