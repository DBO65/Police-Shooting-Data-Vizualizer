import matplotlib.pyplot as plt
from RaceThreatLevel import RaceThreatLevelStats
import police_shootings         # imported all libs for visualization and calculations
from scipy.stats import chi2_contingency



shootings = police_shootings.get_shootings()

extracted_threat = [person['Factors']['Threat-Level'] for person in shootings if            #extracts threat and race data
                    'Factors' in person and 'Threat-Level' in person['Factors']]
extracted_race = [person['Person']['Race'] for person in shootings if 'Person' in person and 'Race' in person['Person']]

if __name__ == '__main__':
    stats = RaceThreatLevelStats(extracted_race, extracted_threat)
    stats.count_occurrences()
    stats.calculate_threat_rates()
    race_counts = stats.get_race_counts()
    threat_level_counts = stats.get_threat_level_counts()
    race_threat_rates = stats.get_race_threat_rates()

    print(race_counts)
    print(threat_level_counts)
    print(race_threat_rates)

    contingency_table = []          #data for chi square test
    for threat_level in stats.threat_level_counts:
        row = []
        for race in race_counts:
            count = 0
            for i, threat in enumerate(stats.threat_levels_list):
                if threat == threat_level and stats.races_list[i] == race:
                    count += 1
            row.append(count)
        contingency_table.append(row)


    chi2, p, dof, _ = chi2_contingency(contingency_table) #perform chi square test

    #print results of chi square test
    print(f"Chi-square test result: chi2 = {chi2}, p-value = {p}, degrees of freedom = {dof}")
    if p < 0.05:
        print("Reject the null hypothesis: Significant difference in threat perception across races.")
    else:
        print("Fail to reject the null hypothesis: No significant difference in threat perception across races.")

    #adjusting graph title, labels, and values
    lists = sorted(race_threat_rates.items())
    x, y = zip(*lists)
    plt.figure(figsize=(10, 5))
    plt.bar(x, y)            
    plt.title("Effects of Race on Perception of Threat in Police Shootings")
    plt.xlabel("Race")
    plt.ylabel("% Of Suspects Perceived as Threatening")
    plt.ylim(50, 70)
    plt.show()
