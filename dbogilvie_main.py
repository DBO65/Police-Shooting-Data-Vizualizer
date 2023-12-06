import police_shootings
from armedfleeingstats import ArmedFleeingStats
import matplotlib
import scipy.stats
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
shootings = police_shootings.get_shootings()

extract_person = [person for person in shootings]
# extract_person creates a list of all the fatal police shootings in the data set "shootings"
extract_fleeing = [person for person in shootings if person["Factors"]["Fleeing"] not in ("Not Fleeing", "unknown")]
# extract_fleeing creates a list of all the fatal police shooting suspects where they were fleeing
extract_armed = [person for person in shootings if person["Factors"]["Armed"] not in ("unarmed", "unknown")]
# extract_armed creates a list of all the fatal police shooting suspects where they were armed

# Initializing the functions in the class

AF_stats = ArmedFleeingStats(extract_fleeing, extract_armed, extract_person)  # AF in AF_stats stand for Armed Fleeing
AF_stats.armed_fleeing_count()
AF_stats.w_armed_fleeing_count()    # The w in w_armed_fleeing_count() stands for white
AF_stats.b_armed_fleeing_count()    # The b in b_armed_fleeing_count() stands for black
AF_stats.a_armed_fleeing_count()    # The a in a_armed_fleeing_count() stands for asian
AF_stats.h_armed_fleeing_count()    # The h in h_armed_fleeing_count() stands for hispanic
AF_stats.na_armed_fleeing_count()   # The na in na_armed_fleeing_count() stands for native american
AF_stats.o_armed_fleeing_count()   # The o in o_armed_fleeing_count() stands for other
AF_stats.u_armed_fleeing_count()   # The u in u_armed_fleeing_count() stands for unknown

""" Calculations to find the % of police fatal shooting victims who were fleeing, % of police fatal shootings
victims who were fleeing while armed, % of fleeing police fatal shootings victims who were fleeing while armed and 
% of fleeing police fatal shootings victims who were fleeing while armed based of each race"""

c_f_data = len(extract_fleeing)/len(extract_person)         # c_f_data stands for Control Fleeing Data
c_af_data = len(AF_stats.a_flee)/len(extract_person)       # af in c_af_data stands for Armed Fleeing
af_data = len(AF_stats.a_flee)/len(extract_fleeing)       # af in af_data stands for Armed Fleeing
w_af_data = len(AF_stats.w_a_fleeing)/len(AF_stats.white)   # w in w_af_data stands for White
b_af_data = len(AF_stats.b_a_fleeing)/len(AF_stats.black)   # b in b_af_data stands for Black
a_af_data = len(AF_stats.a_a_fleeing)/len(AF_stats.asian)   # a in a_af_data stands for Asian
h_af_data = len(AF_stats.h_a_fleeing)/len(AF_stats.hispanic)    # h in h_af_data stands for Hispanic
na_af_data = len(AF_stats.na_a_fleeing)/len(AF_stats.native)    # na in na_af_data stands for Native American
o_af_data = len(AF_stats.o_a_fleeing)/len(AF_stats.other)       # o in o_af_data stands for Other
u_af_data = len(AF_stats.u_a_fleeing)/len(AF_stats.unknown)     # u in u_af_data stands for Unknown

"""Calculations to find the % of fleeing fatal police victims, based of of race, who were fleeing while armed"""

waf_data = (len(AF_stats.w_a_fleeing)/len(extract_fleeing))     # waf_data stands for white armed fleeing data
baf_data = len(AF_stats.b_a_fleeing)/len(extract_fleeing)       # baf_data stands for black armed fleeing data
aaf_data = len(AF_stats.a_a_fleeing)/len(extract_fleeing)       # aaf_data stands for asian armed fleeing data
haf_data = len(AF_stats.h_a_fleeing)/len(extract_fleeing)       # haf_data stands for hispanic armed fleeing data
_na_af_data = len(AF_stats.na_a_fleeing)/len(extract_fleeing)
# _na_af_data stands for native american armed fleeing data
oaf_data = len(AF_stats.o_a_fleeing)/len(extract_fleeing)       # oaf_data stands for other armed fleeing data
uaf_data = len(AF_stats.u_a_fleeing)/len(extract_fleeing)       # uaf_data stands for unknown armed fleeing data

"""Calculations to find the % of fatal police victims, based of of race, who were fleeing while armed"""

c_waf_data = len(AF_stats.w_a_fleeing)/len(extract_person)   # c_waf_data stands for control white armed fleeing data
c_baf_data = len(AF_stats.b_a_fleeing)/len(extract_person)   # Similar logic to c_waf_data
c_aaf_data = len(AF_stats.a_a_fleeing)/len(extract_person)   # Similar logic to c_waf_data
c_haf_data = len(AF_stats.h_a_fleeing)/len(extract_person)   # Similar logic to c_waf_data
c_naf_data = len(AF_stats.na_a_fleeing)/len(extract_person)  # Similar logic to c_waf_data
c_oaf_data = len(AF_stats.o_a_fleeing)/len(extract_person)   # Similar logic to c_waf_data
c_uaf_data = len(AF_stats.u_a_fleeing)/len(extract_person)   # Similar logic to c_waf_data

# Printing the stats found using the armedfleeingstats class and calculations above

print(f"\nFor police shootings in 2015 the {c_f_data*100:.2f}% of those involved in fatal police shootings were "
      f"fleeing")
print(f"Of those fleeing {af_data*100:.2f}% were armed, so out of all the fatal police shootings since 2015 "
      f"{c_af_data*100:.2f}% of those killed in a fatal police shooting were fleeing and armed")
print(f"When taking into account the race of those fleeing the police while armed during a fatal shooting the")
print("following rates of individuals being shot by police while fleeing while armed was found")
print(f"\nOf all the White individuals involved in a fatal police shooting {w_af_data*100:.2f}% were fleeing while "
      f"armed")
print(f"Of all the African American individuals involved in a fatal police shooting {b_af_data*100:.2f}% were fleeing "
      f"while armed")
print(f"Of all the Asian individuals involved in a fatal police shooting {a_af_data*100:.2f}% were fleeing while armed")
print(f"Of all the Hispanic individuals involved in a fatal police shooting {h_af_data*100:.2f}% were fleeing "
      f"while armed")
print(f"Of all the Native American individuals involved in a fatal police shooting {na_af_data*100:.2f}% were fleeing "
      f"while armed")
print(f"Of all the Other individuals involved in a fatal police shooting {o_af_data*100:.2f}% were fleeing "
      f"while armed")
print(f"Of all the Unknown individuals involved in a fatal police shooting {u_af_data*100:.2f}% were fleeing "
      f"while armed")

print(f"\nOut of the population of individuals fleeing a fatal police shooting while armed {waf_data*100:.2f}%\n"
      f"were White, {baf_data*100:.2f}% were African American, {aaf_data*100:.2f}% were Asian,\n"
      f"{haf_data*100:.2f}% were Hispanic, {_na_af_data*100:.2f}% where Native American, "
      f"{oaf_data*100:.2f}% were Other, and {oaf_data*100:.2f}% were Unknown,")

print(f"\nIn contrast out of all the fatal police shootings that occurred in 2015, {c_waf_data*100:.2f}%\n"
      f"were White, {c_baf_data*100:.2f}% were African American, {c_aaf_data*100:.2f}% were Asian,\n"
      f"{c_haf_data*100:.2f}% were Hispanic, {c_naf_data*100:.2f}% were Native American, "
      f"{c_oaf_data*100:.2f}% were Other, and {c_uaf_data*100:.2f}% were Unknown")

# Create and Display bar chart
x = ['White', 'African-American', 'Asian', 'Hispanic', 'Native American', 'Other', 'Unknown']
y = [w_af_data*100, b_af_data*100, a_af_data*100, h_af_data*100, na_af_data*100, o_af_data*100, u_af_data*100]
plt.bar(x, y, width=1, edgecolor='white', linewidth=0.7)
plt.title('Bar Graph Showing Percentage of each Race Involved in Fatal Police Shooting'
          '\nWhile Fleeing And Armed')
plt.xlabel('\nRaces')
plt.ylabel('Percentage (%)')
plt.show()

# Create and Display pie chart
labels = ['White', 'African-American', 'Asian', 'Hispanic', 'Native American', 'Other', 'Unknown']
sizes = [waf_data*100, baf_data*100, aaf_data*100, haf_data*100, _na_af_data*100, oaf_data*100, uaf_data*100]
colors = ['blue', 'orange', 'green', 'red', 'purple', 'gray', 'lightgray']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Pie Chart Showing the Percentage of Individuals Fleeing While Armed in Fatal Police Shootings'
          '\nDistribution Across Different Races')
plt.show()

# Create and Display pie chart
labels = ['White', 'African-American', 'Asian', 'Hispanic', 'Native American', 'Other', 'Unknown']
sizes = [c_waf_data*100, c_baf_data*100, c_aaf_data*100, c_haf_data*100, c_naf_data*100, c_oaf_data*100, c_uaf_data*100]
colors = ['blue', 'orange', 'green', 'red', 'purple', 'gray', 'lightgray']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Pie Chart Showing the Percentage of Individuals Fleeing While Armed for Each Race'
          '\nAs a Proportion of Total Fatal Police Shooting Incidents')
plt.show()


# Compute "expected" numbers for 0 standard deviation
print("\n\n")
import scipy.stats

# Expected numbers calculation
white_expected = len(AF_stats.white) * c_af_data
black_expected = len(AF_stats.black) * c_af_data
hispanic_expected = len(AF_stats.hispanic) * c_af_data
asian_expected = len(AF_stats.asian) * c_af_data
native_expected = len(AF_stats.native) * c_af_data
other_expected = len(AF_stats.other) * c_af_data
unknown_expected = len(AF_stats.unknown) * c_af_data

# List of observed and expected values
prop_list = [
    (len(AF_stats.w_a_fleeing), white_expected),
    (len(AF_stats.b_a_fleeing), black_expected),
    (len(AF_stats.h_a_fleeing), hispanic_expected),
    (len(AF_stats.a_a_fleeing), asian_expected),
    (len(AF_stats.na_a_fleeing), native_expected),
    (len(AF_stats.o_a_fleeing), other_expected),
    (len(AF_stats.u_a_fleeing), unknown_expected)
]

# Chi-squared test statistic calculation
print("\nThe following test statistic is the X^2 value, which is measured by the following formula:\n")
print("\t Sum((observed - expected)^2/expected)\n")
chi_square = 0
for race in prop_list:
    chi_square += (((race[0] - race[1])**2) / race[1])
print(f'Test Statistic: {chi_square:.4f}\n')

# Critical value calculation
critical_value = scipy.stats.chi2.ppf(q=0.95, df=6)
print("The following critical value is the minimum X^2 value required to reject the null hypothesis, H0")
print(f'Critical Value: {critical_value:.4f}\n')

# P-value calculation
p_value = 1 - scipy.stats.chi2.cdf(x=chi_square, df=6)
print(f'p-value: {p_value:.7f}')

# Interpret the results
print("\nInterpretation of Chi-squared Test Results:")
print(f'Test Statistic: {chi_square:.4f}')
print(f'Critical Value: {critical_value:.4f}')
print(f'p-value: {p_value:.7f}\n')

# Compare the test statistic to the critical value
if chi_square > critical_value:
    print("The test statistic exceeds the critical value.")
    print("Reject the null hypothesis (H0) that there is no significant association between race and the "
          "treatment of armed individuals fleeing during police shooting incidents")
else:
    print("The test statistic does not exceed the critical value.")
    print("Fail to reject the null hypothesis (H0) that there is no significant association between race and the "
          "treatment of armed individuals fleeing during police shooting incidents")

# Compare the p-value to the significance level (commonly 0.05)
alpha = 0.05
print(f"\nComparison with Significance Level (α = {alpha}):")
if p_value < alpha:
    print("The p-value is less than the significance level.")
    print("Reject the null hypothesis (H0) that there is no significant association between race and the "
          "treatment of armed individuals fleeing during police shooting incidents")
else:
    print("The p-value is greater than the significance level.")
    print("Fail to reject the null hypothesis (H0) that there is no significant association between race and the "
          "treatment of armed individuals fleeing during police shooting incidents")
