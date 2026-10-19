# description: glitch in laptop, code not in order
kalimba =KATEZERK_KALIMBA
from earsketch import *


beat3="0+--0+-0+0+-0+--"
bass=KATEZERK_LOW_BASS
for i in range(13, 17):
    makeBeat(bass, 4, i, beat3)
for i in range(26, 29):
    makeBeat(bass, 4, i, beat3)
setEffect(4, VOLUME, GAIN, 10, 13, 10, 16)
fitMedia(KATEZERK_DIRTY_BASS, 4, 29.5, 37)
setEffect(4, VOLUME, GAIN, -5, 29, -15, 34 )
setEffect(4, VOLUME, GAIN, -15, 34,-55, 36)
beat2 = "------0+++-------0+++----0+0+"
fitMedia(KATEZERK_SNAP, 1, 37, 37.0625)
setEffect(5, VOLUME, GAIN, -15, 28, -15,38)
setEffect(5, PITCHSHIFT, PITCHSHIFT_SHIFT, -2,28,-2,38)
makeBeat(kalimba, 5, 28, beat2)
setTempo(140)
setEffect(6, VOLUME, GAIN, -10, 29, -60, 33)
fitMedia(KATEZERK_WIND_CHIMES, 3, 26, 41)
".- - / - .... . / .- .. .-. .--. --- .-. -"
morse = "0++0+++--0+++----0+++--0++0++0++0++--0++----0++0+++--0++0++--0++0+++0++--0++0+++0+++0++--0+++0+++0+++--0++0+++0++--0+++"
makeBeat(kalimba, 5, 18, morse, 16)
setEffect(5, VOLUME, GAIN, -15, 1, -15, 26)
setEffect(5, PITCHSHIFT, PITCHSHIFT_SHIFT, 4,1,4,26)


fitMedia(KATEZERK_PITCHED_BASS, 3, 1, 4.2)
fitMedia(KATEZERK_DIRTY_BASS, 4, 2.5, 10)
fitMedia(KATEZERK_DRUM_BOW, 2, 13,14)
fitMedia(KATEZERK_616911_TRASHCAN_STUDIOS_005_NEWARK_AIRPORT_AMBIENCE_ANNOUNCEMENT_AUDIOTRIMMER_COM_, 6, 1.5,33.25)
#fitMedia(KATEZERK_LOW_BASS, 3, 12, 16)

setEffect(6, VOLUME, GAIN, -10, 1, -10, 61)
setEffect(1, VOLUME, GAIN, -15)
setEffect(2, VOLUME, GAIN, -10)
setEffect(4, VOLUME, GAIN, 0, 9, -40, 10)
setEffect(4, VOLUME, BYPASS, 1, 1, 1, 9)
setEffect(4, VOLUME, BYPASS, 0, 9, 0, 61)



#break drums
def amen_break(start, finish, ks_track = 1, r_track = 2):
    kick_snare = [ENTREP_PERC_KICK_1, MILKNSIZZ_CALIENTE_DEPTH_SNARE]
    ride = YG_NEW_HIP_HOP_HIHAT_2
    r_beat = "0-0-0-0-0-0-0-0-"
    phase = 1
    for i in range(start,finish):
        if phase == 1 or phase == 2:
            ks_beat = ks_beat = "0-0-1--1-1001--1"
        elif phase == 3:
            ks_beat = "0-0-1--1-10---1-"
        else:
            ks_beat = "-1001--1-10---1-"
            phase = 0
        makeBeat(kick_snare, ks_track, i, ks_beat)
        makeBeat(ride, r_track, i, r_beat)
        phase += 1

def think_break(start, finish, ks_track = 1, r_track = 2):
    kick_snare = [ENTREP_PERC_KICK_1, MILKNSIZZ_CALIENTE_DEPTH_SNARE]
    ride = YG_NEW_HIP_HOP_HIHAT_2
    ks_beat = "0---1--1010-1---"
    r_beat = "0-0-0-0-0-0-0-0-"
    fraction = False
    if not start == int(start):
        new_start = int(start)
        dif = start - new_start
        start = new_start
        fraction = True
    for i in range(start, finish):
        if fraction == True:
            m = i + dif
            end = finish - dif
        else:
            m = i  
            end = finish
        if not end == i:
            makeBeat(kick_snare, ks_track, m, ks_beat)
            makeBeat(ride, r_track, m, r_beat)
        else:
            break

#samples
phase = 1
for i in range(1, 12*3, 12):
    print(phase)
    if phase == 1:
        amen_break(i+3, i+12)
    elif phase == 2:
        think_break(i+3,i+12)
        phase = 0
    phase += 1

