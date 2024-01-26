import radioactivedecay as rd

inv = rd.Inventory({ 'Xe-142': 8.07E+06 }, 'Bq')

decayed = inv.decay(1, 'hr')

print(decayed.activities('Bq'))
