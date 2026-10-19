# description: Attempt 2
from earsketch import *
#chorus
def chorus(start, track = 1):
    set = [IRCA_PLENA_1_KEYS_E_MAJOR, 
           IRCA_PLENA_2_GUITARRA_E_MIXO, 
           RADICAL_START_KEYS_1, 
           MILKNSIZZ_CORRIDOS_STRINGS, 
           IRCA_PLENA_2_PIANO_DFLAT_MIXO,
           ENTREP_PERC_KICK_1,
           IRCA_PLENA_1_BAJO_A_MAJOR,
          ]
    for i in range(start + 1, start+15):
        if not (i>= start+6):
            makeBeat(set[0], track, i, "0", 1)
        if i>= 3:
            k_beat = "0--00-0-"
            makeBeat(set[5], track + 1, i , k_beat)
            b_beat = "0--0--0--0--0--0"
            if i > start + 2:
                makeBeat(set[6], track+ 2, i,b_beat)
            #fitMedia(set[3], track+3, start+4, start+8)
            #fitMedia(set[3], track+3, start+9, start+13)
            
            fitMedia(ENTREP_THEME_BRASS, track+4, start + 6, start+14)


#intro
fitMedia(RADICAL_START_KEYS_1, 1, 1, 3)
set = [IRCA_PLENA_1_KEYS_E_MAJOR,
       IRCA_PLENA_2_GUITARRA_E_MIXO, 
       RADICAL_START_KEYS_1, 
       MILKNSIZZ_CORRIDOS_STRINGS, 
       IRCA_PLENA_2_PIANO_DFLAT_MIXO,
       ENTREP_PERC_KICK_1,
       IRCA_PLENA_1_BAJO_A_MAJOR,
          ]
beat = "0---1--1010-1---"
makeBeat([set[5], set[4]], 1, 3, beat)
fitMedia(set[4], 1, 4, 6)

chorus(5)
#verse1

#verse2

setTempo(100)
