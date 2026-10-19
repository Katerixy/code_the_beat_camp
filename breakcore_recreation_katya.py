# description: breakcore
from earsketch import *
#break samples
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
    if start != start//1:
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
        print(m)
        if not end == m:
            makeBeat(kick_snare, ks_track, m, ks_beat)
            makeBeat(ride, r_track, m, r_beat)
        else:
            break
#i want to add (3 volume for 9, 5 to 10), (10 to 17, and -40 to 25) of track 2.
#i run function. it adds (9,10) and (17, 25) to VOLUME_SET[2]
#VOLUME_SET = {"1": [(9,10), (17,25)]], "2": [()]}
#at the end of main, ORGANIZE sets, run other function and give it all the sets
#for set in sets: for track in set: for tuple in set:
#add effect in that place, remove effect from last value in last tuple in set till first value in this tuple
def main():
    setTempo(120)
    break_set = {"kick" : ENTREP_PERC_KICK_1, "snare" : MILKNSIZZ_CALIENTE_DEPTH_SNARE, "hihat" : YG_NEW_HIP_HOP_HIHAT_2}
    think_break(1,2)
    think_break(2.25, 3)

def test():
    setTempo(120)
    think_break(2.5, 12)
    amen_break(13,21)
#calling functions
test()




