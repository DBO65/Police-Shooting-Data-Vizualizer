class RaceThreatLevelStats:            
    def __init__(self, races_list, threat_levels_list):
        self.races_list = races_list
        self.threat_levels_list = threat_levels_list
        self.race_counts = {}
        self.threat_level_counts = {}
        self.race_threat_rates = {}

    def count_occurrences(self):            #Counts how many people per race there are
        for race in self.races_list:
            self.race_counts[race] = self.race_counts.get(race, 0) + 1

        for threat_level in self.threat_levels_list:
            self.threat_level_counts[threat_level] = self.threat_level_counts.get(threat_level, 0) + 1

    def calculate_threat_rates(self):           #Calculates perceived threat rates rounded to 3 decimal places
        attack_threat_counts = {race: 0 for race in self.race_counts}
        for i, threat_level in enumerate(self.threat_levels_list):
            if threat_level == 'attack':
                race = self.races_list[i]  # Corresponding race
                attack_threat_counts[race] = attack_threat_counts.get(race, 0) + 1
        for race, count in self.race_counts.items():
            rate = (attack_threat_counts[race] / count) * 100 if count else 0
            self.race_threat_rates[race] = round(rate, 3)

    def get_race_counts(self):
        return self.race_counts

    def get_threat_level_counts(self):
        return self.threat_level_counts

    def get_race_threat_rates(self):
        return self.race_threat_rates
