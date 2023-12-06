class ArmedFleeingStats:
    def __init__(self, fleeing, armed, race):
        self.fleeing = fleeing
        self.armed = armed
        self.race = race
        self.white = [person for person in self.race if person["Person"]["Race"] == "White"]
        self.black = [person for person in self.race if person["Person"]["Race"] == "African American"]
        self.asian = [person for person in self.race if person["Person"]["Race"] == "Asian"]
        self.hispanic = [person for person in self.race if person["Person"]["Race"] == "Hispanic"]
        self.native = [person for person in self.race if person["Person"]["Race"] == "Native American"]
        self.unknown = [person for person in self.race if person["Person"]["Race"] == "Unknown"]
        self.a_flee = []
        self.w_a_fleeing = []
        self.b_a_fleeing = []
        self.a_a_fleeing = []
        self.h_a_fleeing = []
        self.na_a_fleeing = []
        self.u_a_fleeing = []

    def armed_fleeing_count(self):
        self.a_flee = [person for person in self.fleeing if person["Factors"]["Armed"] not in ("unarmed", "unknown")]
        # a_fleeing stands for armed fleeing

    def w_armed_fleeing_count(self):
        self.w_a_fleeing = [person for person in self.a_flee if person["Person"]["Race"] == "White"]

    def b_armed_fleeing_count(self):
        self.b_a_fleeing = [person for person in self.a_flee if person["Person"]["Race"] == "African American"]

    def a_armed_fleeing_count(self):
        self.a_a_fleeing = [person for person in self.a_flee if person["Person"]["Race"] == "Asian"]

    def h_armed_fleeing_count(self):
        self.h_a_fleeing = [person for person in self.a_flee if person["Person"]["Race"] == "Hispanic"]

    def na_armed_fleeing_count(self):
        self.na_a_fleeing = [person for person in self.a_flee if person["Person"]["Race"] == "Native American"]

    def u_armed_fleeing_count(self):
        self.u_a_fleeing = [person for person in self.a_flee if person["Person"]["Race"] == "Unknown"]
