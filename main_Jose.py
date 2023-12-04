import matplotlib.pyplot as plt
from RaceThreatLevel import RaceThreatLevelStats
import police_shootings
shootings = police_shootings.get_shootings()

extracted_threat = [person['Factors']['Threat-Level'] for person in shootings if 'Factors' in person and 'Threat-Level' in person['Factors']]           #Extract threat from factors
extracted_race = [person['Person']['Race'] for person in shootings if 'Person' in person and 'Race' in person['Person']]            #Extract race from person



if __name__ == '__main__':
    stats = RaceThreatLevelStats(extracted_race, extracted_threat)
    stats.count_occurrences()
    stats.calculate_threat_rates()
    race_counts = stats.get_race_counts()
    threat_level_counts = stats.get_threat_level_counts()
    race_threat_rates = stats.get_race_threat_rates()


    print(race_counts)
    print(threat_level_counts)            #Prints all data
    print(race_threat_rates)
    lists = sorted(race_threat_rates.items())
    x, y = zip(*lists)
    plt.figure(figsize=(12, 5))
    plt.plot(x, y)
    plt.xlabel("Race")            #Plots data to line graph with proper spacing and labeling
    plt.ylabel("\"Threat\" Rate")
    plt.show()







