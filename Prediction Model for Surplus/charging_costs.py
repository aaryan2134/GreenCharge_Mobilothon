import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fixed_slow = 0.03
time_slow = 0.02
energy_slow = 0.009

fixed_fast = 0.038
time_fast = 0.077
energy_fast = 0.018

peak = 0.2816
mid = 0.1459
off = 0.0702

iec = 0.001

iva = 0.23

n = 0.5 
bateria = 82*n
tempo_slow = (11 * 60)*n
tempo_fast = ((3 * 60) + 45)*n


preco_slow_peak = fixed_slow + (time_slow * tempo_slow) + (energy_slow*bateria) + (peak*bateria) + (iec*bateria)
preco_slow_peak = preco_slow_peak + preco_slow_peak*iva

preco_slow_mid = fixed_slow + (time_slow * tempo_slow) + (energy_slow*bateria) + (mid*bateria) + (iec*bateria)
preco_slow_mid = preco_slow_mid + preco_slow_mid*iva

preco_slow_off = fixed_slow + (time_slow * tempo_slow) + (energy_slow*bateria) + (off*bateria) + (iec*bateria)
preco_slow_off = preco_slow_off + preco_slow_off*iva

print('(Slow Charging)\nPeak -',preco_slow_peak,'\nMid-peak -', preco_slow_mid, '\nOff-peak -' ,preco_slow_off)

preco_fast_peak = fixed_fast + (time_fast * tempo_fast) + (energy_fast*bateria) + (peak*bateria) + (iec*bateria)
preco_fast_peak = preco_fast_peak + preco_fast_peak*iva

preco_fast_mid = fixed_fast + (time_fast * tempo_fast) + (energy_fast*bateria) + (mid*bateria) + (iec*bateria)
preco_fast_mid = preco_slow_mid + preco_slow_mid*iva

preco_fast_off = fixed_fast + (time_fast * tempo_fast) + (energy_fast*bateria) + (off*bateria) + (iec*bateria)
preco_fast_off = preco_fast_off + preco_fast_off*iva

print('(Fast Charging)\nPeak -', preco_fast_peak,'\nMid-peak -',preco_fast_mid,'\nOff-peak -',preco_fast_off)

a = 0.75

print('(GreenCharge - Slow charging)\nPeak -',preco_slow_peak*a,'\nMid-peak -',preco_slow_mid*a,'\nOff-peak -',preco_slow_off*a,'\n')
print('(GreenCharge - Fast charging)\nPeak -',preco_fast_peak*a,'\nMid-peak -',preco_fast_mid*a,'\nOff-peak -',preco_fast_off*a)