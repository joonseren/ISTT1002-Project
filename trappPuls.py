import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import statistics as statistics
import scipy.stats as stats

# Filstier for TCX-filene
file1 = 'trappPolar.tcx'  # Polar fil
file2 = 'trappGarmin.tcx'  # Garmin fil

# Funksjon for å lese pulsdata fra en TCX-fil
def read_heart_rate_from_tcx(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = {'ns': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}
    
    heart_rates = []
    for hr in root.findall('.//ns:HeartRateBpm/ns:Value', namespaces=namespace):
        heart_rates.append(int(hr.text))
    
    return heart_rates

# Lese pulsdata fra begge filer
heart_rates_1 = read_heart_rate_from_tcx(file1)
heart_rates_2 = read_heart_rate_from_tcx(file2)

min_length = min(len(heart_rates_1), len(heart_rates_2))

print(f"lengde på heart_rates_1: {len(heart_rates_1)}")
print(f"lengde på heart_rates_2: {len(heart_rates_2)}")

heart_rates_1 = heart_rates_1[:min_length]
heart_rates_2 = heart_rates_2[:min_length]

# Statistiske kalkulasjoner


# Plotting heart rates
plt.figure(figsize=(10, 5))
plt.plot(heart_rates_1, label='Polar', color='red')
plt.plot(heart_rates_2, label='Garmin', color='blue')
plt.xlabel('Tid (s)')
plt.ylabel('Puls (bpm)')
plt.title('Måling av puls i trapp')
plt.legend()
plt.grid(True)
#plt.show()