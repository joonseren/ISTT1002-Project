import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import statistics
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
x = heart_rates_1
y = heart_rates_2

n1 = len(x)
n2 = len(y)

mean_x = statistics.mean(x)
mean_y = statistics.mean(y)

sd_x = statistics.stdev(x)
sd_y = statistics.stdev(y)

# antall frihetsgrader:
ny = (sd_x**2/n1+sd_y**2/n2)**2/((sd_x**2/n1)**2/(n1-1)+(sd_y**2/n2)**2/(n2-1))
print("Antall frihetsgrader (ny) = ", ny)

t_kritisk = stats.t.ppf(1-0.05,ny)
print("t_kritisk = ", t_kritisk)

stats.ttest_ind_from_stats(mean_x, sd_x, n1, mean_y, sd_y, n2, equal_var=True, alternative = 'greater')

# Plot normal distributions
x_range = np.linspace(min(min(x), min(y)), max(max(x), max(y))+10, 100)
plt.figure(figsize=(10, 5))
plt.plot(x_range, stats.norm.pdf(x_range, mean_x, sd_x), label='Polar Distribution', color='red')
plt.plot(x_range, stats.norm.pdf(x_range, mean_y, sd_y), label='Garmin Distribution', color='blue')
plt.xlabel('Heart Rate (bpm)')
plt.ylabel('Probability Density')
plt.title('Normal Distributions of Heart Rate Measurements')
plt.legend()
plt.grid(True)
plt.show()

# Plotting heart rates
plt.figure(figsize=(10, 5))
plt.plot(heart_rates_1, label='Polar', color='red')
plt.plot(heart_rates_2, label='Garmin', color='blue')
plt.xlabel('Tid (s)')
plt.ylabel('Puls (bpm)')
plt.title('Måling av puls i trapp')
plt.legend()
plt.grid(True)
plt.show()