import xml.etree.ElementTree as ET
from datetime import datetime
import matplotlib.pyplot as plt

def parse_tcx(file_path):
    """Parse a .tcx file and extract timestamps and heart rate data."""
    timestamps = []
    heart_rates = []
    
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Namespace found in TCX files, usually defined as default namespace.
    namespace = {'ns': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}
    
    for trackpoint in root.findall('.//ns:Trackpoint', namespace):
        # Extract time
        time_elem = trackpoint.find('ns:Time', namespace)
        if time_elem is not None:
            timestamp = datetime.fromisoformat(time_elem.text.replace("Z", "+00:00"))
            timestamps.append(timestamp)
        
        # Extract heart rate
        hr_elem = trackpoint.find('.//ns:HeartRateBpm/ns:Value', namespace)
        if hr_elem is not None:
            heart_rate = int(hr_elem.text)
            heart_rates.append(heart_rate)
    
    return timestamps, heart_rates

# Load Garmin data
garmin_file = 'trappGarmin.tcx'
garmin_timestamps, garmin_heart_rates = parse_tcx(garmin_file)

# Load Polar data
polar_file = 'trappPolar.tcx'
polar_timestamps, polar_heart_rates = parse_tcx(polar_file)

print("First 5 Garmin timestamps:", garmin_timestamps[:5])
print("First 5 Polar timestamps:", polar_timestamps[:5])

# Plotting heart rates
plt.figure(figsize=(10, 5))
plt.plot(garmin_timestamps, garmin_heart_rates, label='Garmin', color='red')
plt.plot(polar_timestamps, polar_heart_rates, label='Polar', color='blue')
plt.xlabel('Tid')
plt.ylabel('Puls (bpm)')
plt.title('Måling av puls i ro')
plt.legend()
plt.grid(True)
plt.show()
