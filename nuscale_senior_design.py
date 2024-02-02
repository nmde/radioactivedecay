import radioactivedecay as rd
import json as json

inv = rd.Inventory({
'Kr-85': 8.07E+06,
'Kr-85m': 5.59E+11,
'Kr-87': 3.83E+12,
'Kr-88': 2.35E+12,
'Kr-89': 1.61E+14,
'Kr-91': 2.67E+15,
'Kr-92': 6.44E+15,
'Kr-93': 2.93E+15,
'Xe-133': 1.23E+11,
'Xe-135': 1.76E+12,
'Xe-135m': 1.24E+13,
'Xe-137': 2.33E+14,
'Xe-138': 6.10E+13,
'Xe-139': 1.01E+15,
'Xe-140': 2.06E+15,
'Xe-141': 6.05E+15,
'Xe-142': 3.13E+15,
'I-129': 4.94E+00,
'I-131': 1.46E+10,
'I-132': 1.80E+12,
'I-133': 2.88E+11,
'I-133m': 1.28E+15,
'I-134': 7.77E+12,
'I-135': 8.66E+11,
'I-136': 1.55E+14,
'I-136m': 9.56E+13,
'I-137': 4.06E+14,
'I-138': 8.00E+14,
'I-139': 1.07E+15,
'I-140': 6.71E+14,
'Cs-134': 4.69E+07,
'Cs-137': 5.21E+07,
'Cs-138': 2.73E+13,
'Cs-139': 8.56E+13,
'Cs-140': 6.55E+14,
'Cs-141': 1.28E+15,
'Cs-142': 1.19E+16,
'Cs-143': 6.10E+15,
'Cs-144': 3.68E+15,
'Sr-89': 1.17E+07,
'Sr-91': 1.92E+09,
'Sr-92': 7.48E+09,
'Sr-93': 1.65E+11,
'Sr-94': 9.82E+11,
'Sr-95': 2.56E+12,
'Sr-96': 4.40E+13,
'Sr-97': 5.12E+13,
'Sr-98': 1.66E+13
}, 'Bq')


decayed = inv.decay(1, 'hr').activities('Bq')

bins = [0, 0, 0, 0, 0, 0];

with open('radioactivedecay/nuscale_senior_design/nuclides.json') as nuclides_json:
    nuclide_data = json.load(nuclides_json)
    for nuclide in decayed.keys():
        gammas = nuclide_data[nuclide]['gammas']
        for energy in gammas.keys():
            e = float(energy)
            if e < 1:
                bins[0] += decayed[nuclide] * gammas[energy]
            elif e < 2:
                bins[1] += decayed[nuclide] * gammas[energy]
            elif e < 3:
                bins[2] += decayed[nuclide] * gammas[energy]
            elif e < 4:
                bins[3] += decayed[nuclide] * gammas[energy]
            elif e < 5:
                bins[4] += decayed[nuclide] * gammas[energy]
            else:
                bins[5] += decayed[nuclide] * gammas[energy]

print(bins)

