# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:14:42 2015

@author: nfalba
"""

import Constants;

class NormalMove:
    def __init__(self, name, amount, hit_chance):
        self.name = name;
        self.amount = amount;
        self.hit_chance = hit_chance;
        
    def use(self, pokemonA, pokemonT):
        damage = Constants.calcDamage(self.hit_chance, self.amount, pokemonA, pokemonT, False, True);
        if damage < 0:
            damage = 1;
        
        print "%s used %s." % (pokemonA.name, self.name);
        pokemonT.health = pokemonT.health - damage;
    
    def __str__(self):
        s = "Name: " + self.name + "\t";
        s += "Type: Normal\t";
        s += "Base Damage: " + str(self.amount);
        return s;

class StatMove(NormalMove):    
    def __init__(self, name, amount, hit_chance, ty):
        NormalMove.__init__(self, name, amount, hit_chance);
        self.type = ty;
    
    def use(self, pokemonA, pokemonT):
        if self.type == Constants.STAT_MOVE_INC_ATTACK:
            pokemonA.attack = pokemonA.attack + self.amount;
        elif self.type == Constants.STAT_MOVE_INC_DEFENSE:
            pokemonA.defense = pokemonA.defense + self.amount;
        elif self.type ==  Constants.STAT_MOVE_DEC_ATTACK:
            pokemonT.attack = pokemonT.attack - self.amount;
            if pokemonT.attack < 0:
                pokemonT.attack = 0;
        else:
            pokemonT.defense = pokemonT.defense - self.amount;
            if pokemonT.defense < 0:
                pokemonT.defense = 0;
        print "%s used %s." % (pokemonA.name, self.name);
    
    def __str__(self):
        s = "Name: " + self.name + "\t";
        s += "Type: Status Move\t";
        stat_type_str = "";
        amount_str = "";
        if self.type == Constants.STAT_MOVE_DEC_ATTACK:
            stat_type_str = "Stat Move Type: Attack Lowering\t";
            amount_str = "Amount Decrease: " + str(self.amount);
        elif self.type ==  Constants.STAT_MOVE_INC_ATTACK:
            stat_type_str = "Stat Move Type: Attack Increasing\t";
            amount_str = "Amount Increase: " + str(self.amount);
        elif self.type == Constants.STAT_MOVE_DEC_DEFENSE:
            stat_type_str = "Stat Move Type: Defense Lowering\t";
            amount_str = "Amount Decrease: " + str(self.amount);
        else:
            stat_type_str = "Stat Move Type: Defense Increasing\t";
            amount_str = "Amount Increase: " + str(self.amount);
        s += stat_type_str + amount_str;
        return s;

class SpecMove(NormalMove):
    
    def __init__(self, name, amount, hit_chance, ty):
        NormalMove.__init__(self,name,amount,hit_chance)
        self.type = ty;
    
    def use(self, pokemonA, pokemonD):
        superEffective = False;
        
        if self.type == Constants.WATER_TY:
            if pokemonD.type == Constants.FIRE_TY:
                superEffective = True;
        elif self.type == Constants.FIRE_TY:
            if pokemonD.type == Constants.EARTH_TY:
                superEffective = True;
        elif self.type == Constants.EARTH_TY:
            if pokemonD.type == Constants.WATER_TY:
                superEffective = True;
        
        damage = Constants.calcDamage(self.hit_chance, self.amount, pokemonA, pokemonD, superEffective, False);
        if damage < 0:
            damage = 1;
        pokemonD.health = pokemonD.health - damage;
        print "%s used %s." % (pokemonA.name, self.name);
    
    def __str__(self):
        s = "Name: " + self.name + "\t";
        s += "Type: Special Move\t";
        s += "Special Move Type: "
        if self.type == Constants.FIRE_TY:
            s += "Fire\t";
        elif self.type == Constants.WATER_TY:
            s += "Water\t";
        else:
            s += "Earth\t";
        
        s+= "Base Damage: " + str(self.amount);
        return s;
        
        
all_moves = {};

#Normal Moves
        
quick_attack = NormalMove("Quick Attack", 15, 0.95);
scratch = NormalMove("Scratch", 25, 0.8);
tackle = NormalMove("Tackle", 20, 0.9);
slam = NormalMove("Slam", 30, 0.6);

all_moves[quick_attack.name] = quick_attack;
all_moves[scratch.name] = scratch;
all_moves[tackle.name] = tackle;
all_moves[slam.name] = slam;

#Spec Moves

water_gun = SpecMove("Water Gun", 15, 1.0, Constants.WATER_TY);
surf = SpecMove("Surf", 20, 0.8, Constants.WATER_TY);
hydro_pump = SpecMove("Hydropump", 30, 0.65, Constants.WATER_TY);

ember = SpecMove("Ember", 15, 1.0, Constants.FIRE_TY);
flamethrower = SpecMove("Flamethrower", 20, 0.8, Constants.FIRE_TY);
fire_blast = SpecMove("Fire Blast", 30, 0.65, Constants.FIRE_TY);

vine_whip = SpecMove("Vine Whip", 15, 1.0, Constants.EARTH_TY);
razor_leaf = SpecMove("Razor Leaf", 20, 0.8, Constants.EARTH_TY);
solar_beam = SpecMove("Solar Beam", 30, 0.65, Constants.EARTH_TY);

all_moves[water_gun.name] = water_gun;
all_moves[surf.name] = surf;
all_moves[hydro_pump.name] = hydro_pump;
all_moves[ember.name] = ember;
all_moves[flamethrower.name] = flamethrower;
all_moves[fire_blast.name] = fire_blast;
all_moves[vine_whip.name] = vine_whip;
all_moves[razor_leaf.name] = razor_leaf;
all_moves[solar_beam.name] = solar_beam;

#Stat moves

growl = StatMove("Growl", 3, 0.9, Constants.STAT_MOVE_DEC_ATTACK);
tail_whip = StatMove("Tail Whip", 3, 0.9, Constants.STAT_MOVE_DEC_DEFENSE);
focus_energy = StatMove("Focus Energy", 3, 1.0, Constants.STAT_MOVE_INC_ATTACK);
harden = StatMove("Harden", 3, 1.0, Constants.STAT_MOVE_DEC_ATTACK);

all_moves[growl.name] = growl;
all_moves[tail_whip.name] = tail_whip;
all_moves[focus_energy.name] = focus_energy;
all_moves[harden.name] = harden;

def displayAllMoves(moves):
    for k in moves:
        print moves[k];