from earsketch import *
lead_track = 1
bass_track = 2
drum_track = 3
sfx_track = 4

setTempo(140)

lead_track = 1
bass_track = 2
drum_track = 3
sfx_track = 4

#Intro

#Part 1
kick = OS_KICK06
beat1 = "0--0--0--0--0-0-0"
for measure in range(1,9):
    makeBeat(kick, 5, measure, beat1)
fitMedia(RD_EDM_RAVECHORD_1, lead_track, 1, 9)
fitMedia(RD_EDM_MAINBEAT_1, drum_track, 3, 9)
fitMedia(AK_UNDOG_PAD_1, bass_track, 5, 9)

fitMedia(RD_EDM_RAVECHORD_3, lead_track, 9, 16)
fitMedia(RD_EDM_MAINBEAT_8, drum_track, 9, 16)

#Part 2
beat2 = "0--0--0--0--"
for measure in range(16,20):
    makeBeat(kick, 5, measure, beat2)
fitMedia(RD_EDM_RAVECHORD_1, lead_track, 16, 24)

#Part 2.1
fitMedia(RD_EDM_MAINBEAT_1, drum_track, 16, 20)
fitMedia(AK_UNDOG_PAD_1, bass_track, 16, 20)
for i in range(4):
    fitMedia(RD_POP_TRINKLELEAD_1, sfx_track, 16.375+i, 17.1+i)


#Part2.1
fitMedia(HOUSE_MAIN_BEAT_002, drum_track, 20, 30)
for i in range(3):
    fitMedia(AK_UNDOG_PAD_2, bass_track, 20 +i*4, 24+i*4)
fitMedia(RD_EDM_RAVECHORD_2, 6, 23, 27)
fitMedia(RD_EDM_RAVECHORD_2, lead_track, 27, 36)

#Part 3 (repeat 1)
for measure in range(36,47):
    makeBeat(kick, 5, measure, beat1)
fitMedia(RD_EDM_RAVECHORD_1, lead_track, 36, 47)
fitMedia(RD_EDM_MAINBEAT_1, drum_track, 36, 47)
fitMedia(AK_UNDOG_PAD_1, bass_track, 36, 47)
for i in range(0, 12, 2):
    fitMedia(RD_POP_TRINKLELEAD_1, sfx_track, 36.375+i, 37.1+i)

#Outro
sound= AK_UNDOG_808_1
beat = "----0"
for i in range(47, 48):
    makeBeat(sound, 6, 47, beat, 8)

#Effects
setEffect(sfx_track, VOLUME, GAIN, -5)
setEffect(6, VOLUME, GAIN, -60, 23, 0, 25)
effect_start= 44
effect_end = 47
setEffect(lead_track, VOLUME, GAIN, 0, 1, 0, effect_start)
setEffect(bass_track, VOLUME, GAIN, 0, 1, 0, effect_start)
setEffect(drum_track, VOLUME, GAIN, 0, 1, 0, effect_start)
setEffect(5, VOLUME, GAIN, 0, 1, 0, effect_start)
setEffect(lead_track, VOLUME, GAIN, 0, effect_start, -50, effect_end)
setEffect(bass_track, VOLUME, GAIN, 0, effect_start, -40, effect_end)
setEffect(drum_track, VOLUME, GAIN, 0, effect_start, -60, effect_end)
setEffect(5, VOLUME, GAIN, 0, effect_start, -60, effect_end)


