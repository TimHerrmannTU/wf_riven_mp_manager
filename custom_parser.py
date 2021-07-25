import math

class custom_parser:
    def __init__(self):
        self.dictionary = {}
        self.preperation()

    def new_translation(self, abriviation: str, wm_v: str, rm_v: str):
        self.dictionary[rm_v] = wm_v

    def preperation(self):
        #IPS
        self.new_translation("imp", "impact_damage", "Impact")
        self.new_translation("punc", "puncture_damage", "Puncture")
        self.new_translation("slash", "slash_damage", "Slash")
        #Elements
        self.new_translation("tox", "toxin_damage", "Toxin")
        self.new_translation("elec", "electric_damage", "Electric")
        self.new_translation("heat", "heat_damage", "Heat")
        self.new_translation("cold", "cold_damage", "Cold")
        #Bane
        self.new_translation("corp", "damage_vs_corpus", "Corpus")
        self.new_translation("grin", "damage_vs_grineer", "Grineer")
        self.new_translation("inf", "damage_vs_infested", "Infested")
        #Crit
        self.new_translation("cc", "critical_chance", "CritChance")
        self.new_translation("cd", "critical_damage", "CritDmg")
        #Status
        self.new_translation("sc", "status_chance", "StatusC")
        self.new_translation("sd", "status_duration", "StatusD")
        #DPS
        self.new_translation("fr/as", "fire_rate_/_attack_speed", "Speed")
        self.new_translation("dmg", "base_damage_/_melee_damage", "Damage")
        #Guns only
        self.new_translation("ms", "multishot", "Multi")
        self.new_translation("pt", "punch_through", "Punch")
        self.new_translation("pfs", "projectile_speed", "Flight")
        self.new_translation("rls", "reload_speed", "Reload")
        self.new_translation("mag", "magazine_capacity", "Magazine")
        self.new_translation("ammo", "ammo_maximum", "Ammo")
        self.new_translation("rec", "recoil", "Recoil")
        self.new_translation("zoom", "zoom", "Zoom")
        #Melee only
        self.new_translation("range", "range", "Range")
        self.new_translation("slide", "critical_chance_on_slide_attack", "Slide")
        self.new_translation("fin", "finisher_damage", "Finisher")
        self.new_translation("c_eff", "channeling_efficiency", "ComboEfficiency")
        self.new_translation("c_init", "channeling_damage", "InitC")
        self.new_translation("c_gain", "chance_to_gain_extra_combo_count", "ComboGainExtra")
        self.new_translation("c_dur", "combo_duration", "Combo")