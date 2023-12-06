#Benjamin Stickle
#Investigate the correlation between mode of fleeing and threat level

import police_shootings
import matplotlib.pyplot as plt


# Create figure
plt.figure(figsize=[100,200])

#create sample proportions for each shooting
def get_threat_status(list):
    attack_count = 0
    for incident in list:
        if incident["Factors"]["Threat-Level"] == "attack":
            attack_count += 1
    return attack_count

def get_race_count(list, race):
    race_count = 0
    for person in list:
        if person["Person"]["Race"] == race:
            race_count += 1
    return race_count

def get_flee(list, method):
    flee_list = []

    for incident in list:
        if incident["Factors"]["Fleeing"] == method:
            flee_list.append(incident)
    return flee_list

def get_methods(list, method):
    method_list = []

    for incident in list:
        if incident["Shooting"]["Manner"] == method:
            method_list.append(incident)
    return method_list

#initializes our database of all police shootings 
#initializes global variables
shootings = police_shootings.get_shootings()
shot_list = get_methods(shootings, "shot")
tasered_list = get_methods(shootings, "shot and Tasered")

def main():
    #create arrays to be analyzed and displayed
    #create count variables
    shot_list = get_methods(shootings, "shot")
    tasered_list = get_methods(shootings, "shot and Tasered")

    white_taser_count = get_race_count(tasered_list, "White")
    black_taser_count = get_race_count(tasered_list, "African American")
    hispanic_taser_count = get_race_count(tasered_list, "Hispanic")
    asian_taser_count = get_race_count(tasered_list, "Asian")
    native_taser_count = get_race_count(tasered_list, "Native American")
    other_taser_count = get_race_count(tasered_list, "Other")
    unknown_taser_count = get_race_count(tasered_list, "Unknown")

    #Print Base-Level Data Collection
    print("This program serves to analyze the data of 6569 fatal police shootings to investigate a possible correlation with race and the use of de-escalation methods, namely tasing, before being shot.")
    print(f"{len(tasered_list)}, or {len(tasered_list)/len(shootings)*100:.2f}% were faced with less-than-lethal force (tasing) before being shot. ")
    print(f"Of {get_race_count(shootings, 'White')} white people killed by police, {white_taser_count} or {white_taser_count/get_race_count(shootings, 'White')*100:.2f}% faced deescalation methods before being shot.")
    print(f"Of {get_race_count(shootings, 'African American')} African American people killed by police, {black_taser_count} or {black_taser_count/get_race_count(shootings, 'African American')*100:.2f}% faced deescalation methods before being shot.")
    print(f"Of {get_race_count(shootings, 'Hispanic')} Hispanic people killed by police, {hispanic_taser_count} or {hispanic_taser_count/get_race_count(shootings, 'Hispanic')*100:.2f}% faced deescalation methods before being shot.")
    print(f"Of {get_race_count(shootings, 'Asian')} Asian people killed by police, {asian_taser_count} or {asian_taser_count/get_race_count(shootings, 'Asian')*100:.2f}% faced deescalation methods before being shot.")
    print(f"Of {get_race_count(shootings, 'Native American')} Native American people killed by police, {native_taser_count} or {native_taser_count/get_race_count(shootings, 'Native American')*100:.2f}% faced deescalation methods before being shot.")
    print(f"Of {get_race_count(shootings, 'Other')} people of miscellaneous racial identity killed by police, {other_taser_count} or {other_taser_count/get_race_count(shootings, 'Other')*100:.2f}% faced deescalation methods before being shot.")
    print(f"Of {get_race_count(shootings, 'Unknown')} people of unknown racial identity killed by police, {unknown_taser_count} or {unknown_taser_count/get_race_count(shootings, 'Unknown')*100:.2f}% faced deescalation methods before being shot.")

    overall_taser_prop = len(tasered_list)/ len(shootings)*100
    white_taser_prop = white_taser_count/get_race_count(shootings, "White")*100
    black_taser_prop = black_taser_count/get_race_count(shootings, "African American")*100
    hispanic_taser_prop = hispanic_taser_count/get_race_count(shootings, "Hispanic")*100
    asian_taser_prop = asian_taser_count/get_race_count(shootings, "Asian")*100
    native_taser_prop = native_taser_count/get_race_count(shootings, "Native American")*100
    other_taser_prop = other_taser_count/get_race_count(shootings, "Other")*100
    unknown_taser_prop = unknown_taser_count/get_race_count(shootings, "Unknown")*100

    #create a new bar chart
    plt.style.use('_mpl-gallery')

    # make data:
    x = ["Overall", "White", "African American", "Hispanic", "Asian", "Native American", "Other", "Unknown"]
    y = [overall_taser_prop, white_taser_prop, black_taser_prop, hispanic_taser_prop, asian_taser_prop, native_taser_prop, other_taser_prop, unknown_taser_prop]

    #create and show the bar chart
    plt.bar(x, y, width = 1, edgecolor="white", linewidth=0.7)
    plt.title("Distribution of Deescalation Methods Used in Fatal Police Encounters by Race")
    plt.xlabel("Race")
    plt.ylabel("Deescalation Method Percentage")
    plt.show()

if __name__ == "__main__":
    main()




