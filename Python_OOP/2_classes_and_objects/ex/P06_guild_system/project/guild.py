class Player:
    def __init__(self, name:str, hp:int, mp:int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = set("Unaffiliated")

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost

    def player_info(self):
        output = f"Name: {self.name}\n"
        output += f"Guild: {self.guild}"
        output += f"HP: {self.hp}"
        output += f"MP: {self.mp}"