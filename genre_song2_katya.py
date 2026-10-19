# description: 
from earsketch import *

setTempo(120)
def intro(song_end):
    start = 1
    end = 5
    fitMedia(MILKNSIZZ_CHACARERA_LULLABY_BELL, 1, start, end)
    setEffect(1, PITCHSHIFT, PITCHSHIFT_SHIFT, 2, start, 2, end-0.5)
    setEffect(1, PITCHSHIFT, PITCHSHIFT_SHIFT, 2, end-0.5, -10, end)
    setEffect(1, PITCHSHIFT, BYPASS, 0, start, 0 ,end)
    setEffect(1, PITCHSHIFT, BYPASS, 1, end, 1 ,song_end)

    setEffect(1, VOLUME, GAIN, 2, start, 5, end)
    setEffect(1, VOLUME, BYPASS, 0, start, 0 ,end)
    setEffect(1, VOLUME, BYPASS, 1, end, 1 ,song_end)
    setEffect(1, VOLUME, GAIN, 0, end, 0, end+1)

    
def verse(num, song_end):
    if num == 1:
        start = 5
        end = 15
        for i in range((end-5)//2):
            m = i*2
            fitMedia(MILKNSIZZ_CHACARERA_LULLABY_BELL, 1, start+m, start+2+m)
        sound = [RD_TRAP_SUBBASS_3, MILKNSIZZ_MOODITO_ANALOG_BLEEP]
        for i in range(start+1, end-1, 5):
            fitMedia(sound[0], 4, i, i+2)
            fitMedia(sound[0], 4, i+2, i+3)
        for i in range(start, end-3, 5):
            fitMedia(sound[1], 5, i+3.25, i+4)
            fitMedia(sound[1], 5, i+4.25, i+5)
        setEffect(4, VOLUME, BYPASS, 1, 1, 1, 9)
        setEffect(4, VOLUME, GAIN, -60, 9)
        setEffect(4, VOLUME, BYPASS, 1, 1, 1, song_end)
        
        phase = 1
        for i in range(start, end, 2):
            if not phase == 3:
                fitMedia(HIPHOP_STOMP_BEAT_007, 2, i, i+2)
            else:
                sound = CIARA_SET_PERC_CLAP_1
                beat  ="0"
                makeBeat(sound, 3, i-0.36, beat, 3)
                fitMedia(HIPHOP_STOMP_BEAT_007, 2, i, i+2)
                phase = 1
            phase+= 1
    elif num == 2:
        start = 16
        end = 26
        fitMedia(HIPHOP_STOMP_BEAT_PART_002, 2, start-1, start)
        fitMedia(HOUSE_ROADS_PIANO_007, 1, start, end-1)
        setEffect(1, VOLUME, GAIN, -10, start,-10, end)
        setEffect(1, VOLUME, BYPASS, 1, start-5, 1, start)
        setEffect(1, VOLUME, BYPASS, 0, start, 0, end)
        setEffect(1, VOLUME, BYPASS, 1, end, 1, song_end)
        beat = "0--0----"
        for i in range(start + 2, end):
            makeBeat(MILKNSIZZ_OCEANS_PARTY_CLAPS, 3, i, beat, 8)
        #effects
        setEffect(3, VOLUME, BYPASS, 1, 1, 1, 18)
        setEffect(3, VOLUME, GAIN, -25)
        setEffect(3, VOLUME, BYPASS, 1, end, 1, song_end)
        setEffect(3, COMPRESSOR, BYPASS, 1, 1, 1, 18)
        setEffect(3, COMPRESSOR, COMPRESSOR_RATIO, 100)
        setEffect(3, COMPRESSOR, COMPRESSOR_THRESHOLD, -30)
        setEffect(3, COMPRESSOR, BYPASS, 1, end, 1, song_end)
        beat = "0++0++0++-0-0"
        for i in range(start + 1, end):
            makeBeat(CIARA_SET_KICK_2, 2, i, beat)
        e_beat = "0++0++0+0+0-000"
        for i in range(end - 1, end):
            makeBeat(HOUSE_ROADS_PIANO_007, 1, i, e_beat)

    elif num == 3:
        start = 26
        end = 33
        #transition
        fitMedia(HOUSE_SFX_WHOOSH_002, 6, start - 0.75, start+0.75)
        fitMedia(DUBSTEP_SFX_006, 2, start, start+0.75)
        setEffect(6, VOLUME, BYPASS, 1, 1, 1, start-1)
        setEffect(2, VOLUME, BYPASS, 1, 1, 1, start)
        setEffect(6, VOLUME, BYPASS, 0, start-1, 0, start+1)
        setEffect(2, VOLUME, BYPASS, 0, start, 0, start+1)
        setEffect(6, VOLUME, GAIN, -50, start-1, -20, start+1)
        setEffect(2, VOLUME, GAIN, -60, start, 0, start+1)
        setEffect(6, VOLUME, BYPASS, 1, start+1, 1, song_end)
        setEffect(2, VOLUME, BYPASS, 1, start+1, 1, song_end)
        for i in range(start, end-1, 2):
            fitMedia(MILKNSIZZ_CHACARERA_LULLABY_BELL, 1, i, 2+i)
        fitMedia(MILKNSIZZ_CHACARERA_LULLABY_BELL, 1, end-1, end+2)
        sound = [Y23_SYNTH_1, MILKNSIZZ_MOODITO_ANALOG_BLEEP]
        for i in range(start+1, end, 4):
            fitMedia(sound[0], 4, i, i+2)
            fitMedia(sound[0], 4, i+2, i+3)
        for i in range(start, end-3, 5):
            fitMedia(sound[1], 5, i+3.25, i+4)
            fitMedia(sound[1], 5, i+4.25, i+5)
        
        phase = 1
        for i in range(start + 1, end, 2):
            if not phase == 3:
                fitMedia(HIPHOP_STOMP_BEAT_007, 2, i, i+2)
            else:
                sound = CIARA_SET_PERC_CLAP_1
                beat  ="0"
                makeBeat(sound, 3, i-0.36, beat, 3)
                fitMedia(HIPHOP_STOMP_BEAT_007, 2, i, i+2)
                phase = 1
            phase+= 1



#1:main 2:drums 3:claps 4:bass 5:sfx
end = 35 + 20
intro(end)
verse(1, end)
verse(2, end)
verse(3, end)


    
