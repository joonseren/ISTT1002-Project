import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import statistics as statistics
import scipy.stats as stats



# Filstier for TCX-filene
file1 = 'stillePolar.tcx'  # Polar fil
file2 = 'stilleGarmin.tcx'  # Garmin fil

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

#print(f"lengde på heart_rates_1: {len(heart_rates_1)}")
#print(f"lengde på heart_rates_2: {len(heart_rates_2)}")

# Opprett en felles tidsakse basert på den lengste listen


min_length = 3
min_length = min(len(heart_rates_1), len(heart_rates_2))

# Fjerner overflødige elementer i listene
heart_rates_1 = heart_rates_1[:min_length]
heart_rates_2 = heart_rates_2[:min_length]

# Statistiske kalkulasjoner
def calculate_statistics(x, y):
    n1 = len(x)
    n2 = len(y)

    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)

    sd_x = statistics.stdev(x)
    sd_y = statistics.stdev(y)

    T = (mean_x - mean_y)/np.sqrt(sd_x**2/n1 + sd_y**2/n2)

    # antall frihetsgrader
    ny = (sd_x**2/n1+sd_y**2/n2)**2/((sd_x**2/n1)**2/(n1-1)+(sd_y**2/n2)**2/(n2-1))
    print("Antall frihetsgrader (ny) = ", ny)

    # P-verdi
    p_verdi = stats.t.sf(np.abs(T), ny) * 2
    print("P-verdi = ", p_verdi)
    print("T-verdi = ", T)


    # Signifikansnivå og kritisk t-verdi
    
    t_critical = stats.t.ppf(1 - 0.05/2, ny)
    print("T-kritisk = ±", t_critical)
    return T, p_verdi


calculate_statistics(heart_rates_1, heart_rates_2)





# Plotting heart rates
plt.figure(figsize=(10, 5))
plt.plot(heart_rates_1, label='Polar', color='red')
plt.plot(heart_rates_2, label='Garmin', color='blue')
plt.xlabel('Tid (s)')
plt.ylabel('Puls (bpm)')
plt.title('Måling av puls i stillesittende tilstand')
plt.legend()
plt.grid(True)
plt.show()