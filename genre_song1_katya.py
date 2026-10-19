from earsketch import *

setTempo(125)
for i in range(1, 13, 4):
    fitMedia(KATEZERK_PIANO_MELODY_002, 1, i, i+4)
    fitMedia(KATEZERK_PIANO_CHORDS_001, 2, i, i+4)
    setEffect(2, VOLUME, BYPASS, 0, i, 0, i+1.9)
    setEffect(2, VOLUME, BYPASS, 1, i+1.9, 1, i+4)
fitMedia(TFLAMES_OMEN_VOX_CHOR_1, 7, 5, 13)
fitMedia(TFLAMES_OMEN_VOX_CHOR_1, 7, 24, 28)


for i in range(10, 13, 2):
    fitMedia(MILKNSIZZ_ADIOS_SHAKEY_SHAKER, 6, i, i +1)

fitMedia(AK_UNDOG_PERC_HATS_2, 3, 5, 13)
fitMedia(BOYKINZ_NIGHT_BEAT_808_1, 4, 9, 17)

fitMedia(SAMIAN_PEUP_BEAT_FULL, 3, 13, 17)
fitMedia(SAMIAN_PEUP_THEME_CHANT_1, 5, 13, 17)


fitMedia(SAMIAN_PEUP_PERC_SHAKER, 3, 17, 22)
fitMedia(SAMIAN_PEUP_THEME_FLUTE, 5, 17, 21)

for i in range(22, 29, 4):
    dif = 0
    m = i + dif
    fitMedia(KATEZERK_PIANO_MELODY_002, 1, m, m+4)
    fitMedia(KATEZERK_PIANO_CHORDS_001, 2, m, m+4)
    fitMedia(ENTREP_THEME_OUTRO_TRUMPET, 4, m, m+3)
    setEffect(2, VOLUME, BYPASS, 0, m, 0, m+1.9)
    setEffect(2, VOLUME, BYPASS, 1, m+1.9, 1, m+4)

for i in range(23, 30, 2):
    fitMedia(MILKNSIZZ_ADIOS_SHAKEY_SHAKER, 6, i, i + 1)
fitMedia(AK_UNDOG_PERC_HATS_2, 3, 22, 34)
fitMedia(SAMIAN_PEUP_THEME_STRINGS_4, 5, 30, 34)

setEffect(0, VOLUME, GAIN, -20, 1, 0, 2)
setEffect(0, VOLUME,GAIN, 0, 2)
setEffect(2, VOLUME, GAIN, -7)
setEffect(7, VOLUME, GAIN, -20,5, -25,13)
setEffect(3, VOLUME, GAIN, 0, 33, -50, 34)
setEffect(5, VOLUME, GAIN, 0, 20, -50, 21)
setEffect(5, VOLUME, GAIN, 0, 30, 0, 32)
setEffect(5, VOLUME, GAIN, 0, 32, -10, 33)
setEffect(5, VOLUME, GAIN, 0, 32, -10, 33)
setEffect(5, VOLUME, GAIN, -10, 33, -60, 34)



