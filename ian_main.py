import matplotlib.pyplot as plt
import police_shootings
shootings = police_shootings.get_shootings()


def main():
    # Statistics unarmed
    unarmed = [incident for incident in shootings if incident['Factors']['Armed'] == 'unarmed']
    unarmed_and_threat = [i for i in unarmed if i['Factors']['Threat-Level'] == 'attack']
    total_unarmed_sample = len(unarmed)
    overall = 100 * len(unarmed_and_threat)/total_unarmed_sample  # Around 38.48%

    # White specific
    white_unarmed = [person for person in unarmed if person['Person']['Race'] == 'White']
    white_unarmed_threat = [i for i in white_unarmed if i['Factors']['Threat-Level'] == 'attack']
    white_sample = len(white_unarmed)
    white_percentage = 100 * len(white_unarmed_threat)/white_sample

    # African-American specific
    black_unarmed = [person for person in unarmed if person['Person']['Race'] == 'African American']
    black_unarmed_threat = [i for i in black_unarmed if i['Factors']['Threat-Level'] == 'attack']
    black_sample = len(black_unarmed)
    black_percentage = 100 * len(black_unarmed_threat)/black_sample

    # Hispanic specific
    hispanic_unarmed = [person for person in unarmed if person['Person']['Race'] == 'Hispanic']
    hispanic_unarmed_threat = [i for i in hispanic_unarmed if i['Factors']['Threat-Level'] == 'attack']
    hispanic_sample = len(hispanic_unarmed)
    hispanic_percentage = 100 * len(hispanic_unarmed_threat)/hispanic_sample

    # Asian specific
    asian_unarmed = [person for person in unarmed if person['Person']['Race'] == 'Asian']
    asian_unarmed_threat = [i for i in asian_unarmed if i['Factors']['Threat-Level'] == 'attack']
    asian_sample = len(asian_unarmed)
    asian_percentage = 100 * len(asian_unarmed_threat)/asian_sample
    # Other

    overall, white_percentage, black_percentage, hispanic_percentage, asian_percentage = round(overall, 2), round(white_percentage, 2), round(black_percentage, 2), round(hispanic_percentage, 2), round(asian_percentage, 2)
    print(f'The results indicate that, of 6569 fatal shootings recorded since 2015:\n'
          f'Of {total_unarmed_sample} total unarmed, {overall}% were perceived as an attack threat by police.\n'
          f'Of {white_sample} unarmed Whites, {white_percentage}% were perceived as an attack threat by police.\n'
          f'Of {black_sample} unarmed African-Americans, {black_percentage}% were perceived as an attack threat by police.\n'
          f'Of {hispanic_sample} unarmed Hispanics, {hispanic_percentage}% were perceived as an attack threat by police.\n'
          f'Of {asian_sample} unarmed Asians, {asian_percentage}% were perceived as an attack threat by police.\n')

    x = ['Overall', 'White', 'African-American', 'Hispanic', 'Asian']
    y = [overall, white_percentage, black_percentage, hispanic_percentage, asian_percentage]
    plt.bar(x, y, width=1, edgecolor='white', linewidth=0.7)
    plt.title('Perceived Unarmed Threat Level vs. Race in Fatal Police Shootings')
    plt.xlabel('Races')
    plt.ylabel('% of unarmed perceived as "attacking"')
    plt.show()


if __name__ == '__main__':
    main()
