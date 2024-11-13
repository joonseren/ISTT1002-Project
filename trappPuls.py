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


# Regner ut differansen i pulsmålingene
diff_heartrates = []
for i in range(len(heart_rates_1)):
    diff_heartrates.append(heart_rates_1[i] - heart_rates_2[i])

# Utfører t-test
sd = statistics.stdev(diff_heartrates)
mean = statistics.mean(diff_heartrates)
sigma = sd/np.sqrt(len(diff_heartrates))

t = mean/(sigma)

df = len(diff_heartrates) - 1 
t_kritisk = stats.t.ppf(1 - 0.025, df)  

p_verdi = stats.t.sf(np.abs(t), df) * 2

# Print results
print(f"\nStatistiske resultater:")
print(f"Gjennomsnittlig differanse: {mean} bpm")
print(f"Standardavvik: {sd} bpm")
print(f"t-verdi: {t}")
print(f"t-kritisk verdi: {t_kritisk:}")
print(f"p-verdi: {p_verdi}")





# Plotting
# Differanse i pulsmåling mellom Polar og Garmin
plt.figure(figsize=(10, 5))
plt.plot(diff_heartrates, label='Difference (Polar - Garmin)', color='green')
plt.xlabel('Tid (s)')
plt.ylabel('Pulsdifferanse (bpm)')
plt.title('Differanse i pulsmåling mellom Polar og Garmin')
plt.legend()
plt.grid(True)


# Plot normalfordeling
plt.figure(figsize=(10, 5))
x = np.linspace(-40, 50, 100)
plt.plot(x, stats.norm.pdf(x, mean, sd), 'r-', label='Normalfordeling')
plt.axvline(x=mean, color='red', linestyle='--', label=f'Gjennomsnitt = {mean:.2f}')
plt.title('Normalfordeling av pulsdifferanser')
plt.xlabel('Puls (bpm)')
plt.ylabel('Tetthet')
plt.legend()
plt.grid(True)

x = np.linspace(-5, 5, 1000)
y = stats.t.pdf(x, df)  

# Plotting av t-fordelingen
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'k-', lw=2)
plt.fill_between(x, 0, y, where=(x <= -t_kritisk) | (x >= t_kritisk), color="blue", alpha=0.3)
plt.text(-t_kritisk, stats.t.pdf(-t_kritisk, df), f"-t_kritisk = {-t_kritisk:.2f}", ha='center', va='bottom')
plt.text(t_kritisk, stats.t.pdf(t_kritisk, df), f"t_kritisk = {t_kritisk:.2f}", ha='center', va='bottom')
plt.axvline(x=t, color='red', linestyle='--', label=f't-verdi = {t:.2f}')
plt.xlabel('X')
plt.ylabel('Sannsynlighetstetthet')
plt.title(f'To-sidig t-test ved alpha = {0.05})')
plt.legend()
plt.grid(True)


# Create boxplot of differences
plt.figure(figsize=(10, 5))
plt.boxplot(diff_heartrates)
plt.ylabel('Pulsdifferanse (bpm)')
plt.title('Boksplot av pulsdifferanser mellom Polar og Garmin')
plt.grid(True)

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