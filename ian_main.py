import matplotlib.pyplot as plt
import scipy.stats
import statistics
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
    other_unarmed = [person for person in unarmed if not (person in white_unarmed or person in black_unarmed or person in hispanic_unarmed or person in asian_unarmed)]
    other_unarmed_threat = [i for i in other_unarmed if i['Factors']['Threat-Level'] == 'attack']
    other_sample = len(other_unarmed)
    other_percentage = 100 * len(other_unarmed_threat) / other_sample

    # Round percentages
    overall, white_percentage, black_percentage, hispanic_percentage, asian_percentage, other_percentage = round(overall, 2), round(white_percentage, 2), round(black_percentage, 2), round(hispanic_percentage, 2), round(asian_percentage, 2), round(other_percentage, 2)
    # Calculate standard deviation of percentages
    standard_dev = statistics.stdev([white_percentage, black_percentage, hispanic_percentage, asian_percentage, other_percentage])

    # Print results
    print(f'The results indicate that, of 6569 fatal shootings recorded since 2015:\n'
          f'Of {total_unarmed_sample} total unarmed, {overall}% were perceived as an attack threat by police.\n'
          f'Of {white_sample} unarmed Whites, {white_percentage}% were perceived as an attack threat by police.\n'
          f'Of {black_sample} unarmed African-Americans, {black_percentage}% were perceived as an attack threat by police.\n'
          f'Of {hispanic_sample} unarmed Hispanics, {hispanic_percentage}% were perceived as an attack threat by police.\n'
          f'Of {asian_sample} unarmed Asians, {asian_percentage}% were perceived as an attack threat by police.\n'
          f'Of {other_sample} other unarmed, {other_percentage}% were perceived as an attack threat by police.\n'
          f'Standard deviation of these percentages is {round(standard_dev, 2)}%')
    # Display bar chart
    x = ['Overall', 'White', 'Black', 'Hispanic', 'Asian', 'Other']
    y = [overall, white_percentage, black_percentage, hispanic_percentage, asian_percentage, other_percentage]
    plt.bar(x, y, width=1, edgecolor='white', linewidth=0.7)
    plt.title('Perceived Unarmed Threat Level vs. Race in Fatal Police Shootings')
    plt.xlabel('Races')
    plt.ylabel('% of unarmed perceived as "attacking"')
    plt.show()

    # Compute "expected" numbers for 0 standard deviation
    white_expected = white_sample * overall / 100
    black_expected = black_sample * overall / 100
    hispanic_expected = hispanic_sample * overall / 100
    asian_expected = asian_sample * overall / 100
    other_expected = other_sample * overall / 100

    prop_list = [(len(white_unarmed_threat), white_expected),
                 (len(black_unarmed_threat), black_expected),
                 (len(hispanic_unarmed_threat), hispanic_expected),
                 (len(asian_unarmed_threat), asian_expected),
                 (len(other_unarmed_threat), other_expected)]

    print("\nThe following test statistic is the X^2 value, which is measured by the following formula:\n")
    print("\t Sum((observed - expected)^2/observed)\n")
    chi_square = 0
    for race in prop_list:
        chi_square += ((race[0] - race[1])**2/race[0])
    print(f'Test Statistic: {chi_square:.4f}\n')

    # p-value calculation
    critical_value = scipy.stats.chi2.ppf(q=.95, df = 6)

    print("The following critical value is the minimum X^2 value required to reject the null hypothesis, H0")
    print(f'Critical Value: {critical_value:.4f}\n')

    p_value = 1 - scipy.stats.chi2.cdf(x=chi_square, df = 6)
    print(f'p-value: {p_value:.4f}')


if __name__ == '__main__':
    main()
