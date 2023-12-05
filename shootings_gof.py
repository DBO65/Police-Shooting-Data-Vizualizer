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


    #calculate chi square test statistic
    #use the formula chi-squared = Sum(observed-expected)^2/expected
    chi_square = 0
    for race in prop_list:
        print(race[0])
        print(race[1])
        chi_square = chi_square + ((race[0] - race[1])**2/race[0])
    print("test statistic: ", chi_square)

    #calculate the p-value of our results
    critical_value = scipy.stats.chi2.ppf(q = .94, df = 6)
    print("critical valuea:", critical_value)
    p_value = 1 - scipy.stats.chi2.cdf(x = chi_square, df = 6)
    print("p-value:", p_value)

    

      

if __name__ == "__main__":
    main()

