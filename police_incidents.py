#Benjamin Stickle
#Investigate the correlation between mode of fleeing and threat level

import police_shootings
import matplotlib.pyplot as plt

#initializes our database of all police shootings 
shootings = police_shootings.get_shootings()

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

#create arrays to be analyzed and displayed

fleeing_car = get_flee(shootings, "Car")
fleeing_foot = get_flee(shootings, "Foot")
other_list = get_flee(shootings, "Other")
not_fleeing = get_flee(shootings, "Not fleeing")
unknown_list = get_flee(shootings, "unknown")
shot_list = get_methods(shootings, "shot")
tasered_list = get_methods(shootings, "shot and Tasered")


car_attack = get_threat_status(fleeing_car)
print("Cars:", car_attack)

#print counts of those in each list
print(f"Car: {len(fleeing_car)}")
print(f"Foot: {len(fleeing_foot)}")
print(f"Other: {len(other_list)}")
print(f"Unknown: {len(unknown_list)}")
print(f"Not fleeing: {len(not_fleeing)}")
print(f"Shot: {len(shot_list)}")
print(f"Tasered and shot: {len(tasered_list)}")


print("This program serves to analyze the data of 6569 fatal police shootings to investigate a possible correlation with race and the use of de-escalation methods, namely tasing, before being shot.")
print(f"{len(tasered_list)}, or {len(tasered_list)/len(shootings)*100:.2f}% were faced with less-than-lethal force (tasing) before being shot. ")
print(f"Of {get_race_count(shootings, 'White')} white people killed by police, {get_race_count(tasered_list, 'White')} or {get_race_count(tasered_list, 'White')/get_race_count(shootings, 'White')*100:.2f}% faced deescalation methods before being shot.")
print(f"Of {get_race_count(shootings, 'African American')} African American people killed by police, {get_race_count(tasered_list, 'African American')} or {get_race_count(tasered_list, 'African American')/get_race_count(shootings, 'African American')*100:.2f}% faced deescalation methods before being shot.")
print(f"Of {get_race_count(shootings, 'Hispanic')} Hispanic people killed by police, {get_race_count(tasered_list, 'Hispanic')} or {get_race_count(tasered_list, 'Hispanic')/get_race_count(shootings, 'Hispanic')*100:.2f}% faced deescalation methods before being shot.")
print(f"Of {get_race_count(shootings, 'Asian')} Asian people killed by police, {get_race_count(tasered_list, 'Asian')} or {get_race_count(tasered_list, 'Asian')/get_race_count(shootings, 'Asian')*100:.2f}% faced deescalation methods before being shot.")
print(f"Of {get_race_count(shootings, 'Native American')} Native American people killed by police, {get_race_count(tasered_list, 'Native American')} or {get_race_count(tasered_list, 'Native American')/get_race_count(shootings, 'Native American')*100:.2f}% faced deescalation methods before being shot.")
print(f"Of {get_race_count(shootings, 'Other')} people of miscellaneous racial identity killed by police, {get_race_count(tasered_list, 'Other')} or {get_race_count(tasered_list, 'Other')/get_race_count(shootings, 'Other')*100:.2f}% faced deescalation methods before being shot.")
print(f"Of {get_race_count(shootings, 'Unknown')} people of unknown racial identity killed by police, {get_race_count(tasered_list, 'Unknown')} or {get_race_count(tasered_list, 'Unknown')/get_race_count(shootings, 'Unknown')*100:.2f}% faced deescalation methods before being shot.")



#create a new bar chart
plt.style.use('_mpl-gallery')

# make data:
x = ["White", "African American", "Hispanic", "Asian", "Native American", "Other", "Unknown"]
y = [get_race_count(tasered_list, "White"), get_race_count(tasered_list, "African American"), get_race_count(tasered_list, "Hispanic"), get_race_count(tasered_list, "Asian"), get_race_count(tasered_list, "Native American"), get_race_count(tasered_list, "Other"), get_race_count(tasered_list, "Unknown")]


#create and show the bar chart
plt.bar(x, y, width = 1, edgecolor="white", linewidth=0.7)
plt.title("Distribution of Deescalation Methods Used in Fatal Police Encounters by Race")
plt.xlabel("Race")
plt.ylabel("Deescalation Method Count")
plt.show()




