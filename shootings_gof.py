#Benjamin Stickle
'''
    Applies a Chi Square goodness of fit test to the distribution of individuals shot by police who were faced with deescalation methods
prior.
    We present the null hypothesis:
        that there is no difference in the proportion of those who face deescalation methods by the police
before being shot as divided by race 

and the alternative:
        that there is a statistically significant difference in the proportion of those who face deescalation methods by the police 
        before being shot as divided by race

    We will test this using a Chi-Square Goodness of Fit Model, using the assumption that each race has an equal proportion
of those who are faced with less-than-lethal force. In this case, referring to tasers. 
'''
import police_incidents
import scipy.stats

#Initialize values used for the Chi Square analysis
def main():
    
    
    #because the null hypothesis is that all races are tasered equally, we expect that the proportion of
    #each race taseredis 5% of each race shot by police
    white_expected = police_incidents.get_race_count(police_incidents.shootings, "White")*(.05)
    black_expected = police_incidents.get_race_count(police_incidents.shootings, "African American")*(.05)
    hispanic_expected = police_incidents.get_race_count(police_incidents.shootings, "Hispanic")*(.05)
    asian_expected = police_incidents.get_race_count(police_incidents.shootings, "Asian")*(.05)
    native_expected =  police_incidents.get_race_count(police_incidents.shootings, "Native American")*(.05)
    misc_expected = police_incidents.get_race_count(police_incidents.shootings, "Other")*(.05)
    unknown_expected = police_incidents.get_race_count(police_incidents.shootings, "Unknown")*(.05)

    white_observed = police_incidents.get_race_count(police_incidents.tasered_list, "White")
    black_observed = police_incidents.get_race_count(police_incidents.tasered_list, "African American")
    hispanic_observed = police_incidents.get_race_count(police_incidents.tasered_list, "Hispanic")
    asian_observed = police_incidents.get_race_count(police_incidents.tasered_list, "Asian")
    native_observed = police_incidents.get_race_count(police_incidents.tasered_list, "Native American")
    misc_observed = police_incidents.get_race_count(police_incidents.tasered_list, "Other")
    unknown_observed = police_incidents.get_race_count(police_incidents.tasered_list, "Unknown")

    #list of tuples for each races observed and expected rates of less than lethal force
    #(observed, expected)
    prop_list = [(white_observed, white_expected),
                 (black_observed, black_expected),
                 (hispanic_observed, hispanic_expected),
                 (asian_observed, asian_expected),
                 (native_observed, native_expected),
                 (misc_observed, misc_expected),
                 (unknown_observed, unknown_expected)]

    #Introduce the purpose of the program, methodology, and investigative techniques
    print("This program serves to investigate the extent to which race influences an police officer's tendency to use less than")
    print("lethal force, operationalized as the use of tasers for this investigation")
    print("We found a Chi-Square Goodness of Fit test to be the best reflection of the liklihood that each racial group has the same")
    print("likelihood of being tased by the police before the decision was made to shoot. ")
    print("In this instance, we are testing the following Hypotheses:")
    print("\t Ho: The proportion of each race which faces deescalation methods before being shot compared to the total count of shootings in")
    print("\t each race is equal to .05, that being the overall proportion of those who were tased by police before being shot")
    print("\t Ha: The proportion of each race tased before being shot by police compared to all shootings of each race is not equal to .05\n")

    #calculate chi square test statistic
    #use the formula chi-squared = Sum(observed-expected)^2/expected

    print("The following test statistic is the X^2 value, which is measured by the following formula:")
    print("\t Sum((observed - expected)^2/observed)")

    chi_square = 0
    for race in prop_list:
        chi_square = chi_square + ((race[0] - race[1])**2/race[0])
    print("test statistic: ", chi_square)
    print()

    #calculate the p-value of our results
    critical_value = scipy.stats.chi2.ppf(q = .95, df = 6)

    print("The following critical value is the minimum X^2 value required to reject the null hypothesis, Ho")
    print("critical value:", critical_value)
    print()

    p_value = 1 - scipy.stats.chi2.cdf(x = chi_square, df = 6)
    print("p-value:", p_value)
    print(f"Because our P-value of {p_value} is greater than our alpha level of .05, we fail to reject the null hypothesis, that")
    print("the proportion of each racial group which face deescalation methods before being shot is equal to .05 for each group ")
    print("There is no convincing evidence that any one racial group faces deescalation methods before being shot by police at a different")
    print("rate than another racial group. ")

    

      

if __name__ == "__main__":
    main()

