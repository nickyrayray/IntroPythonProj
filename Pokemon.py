# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:45:24 2015

@author: nfalba
"""
import Constants
import PMoves;
import random;

class Pokemon:
    
    def __init__(self, name, ty, attack, defense):
        self.name = name;
        self.type = ty;
        self.attack = attack;
        self.defense = defense;
        self.health = 100;
    
    def addMoves(self, moves):
        self.moves = moves;
        
    def useMove(self, pokemonT, move_name):
        move = PMoves.all_moves[move_name];
        move.use(self, pokemonT);
    
    def useRandomMove(self, pokemonT):
        choice = random.randint(0,3);
        move = PMoves.all_moves[self.moves[choice]];
        move.use(self, pokemonT);
    
    def isDead(self):
        if self.health <= 0:
            return True;
        else:
            return False;
    
    def __str__(self):
        if self.type == Constants.FIRE_TY:
            str_ty = "Type: Fire";
        elif self.type == Constants.WATER_TY:
            str_ty = "Type: Water";
        else:
            str_ty = "Type: Earth";
        s = "Name: " + self.name + "\n";
        s += str_ty + "\n";
        s += "Health: " + str(self.health) + "\n";
        s += "Attack: " + str(self.attack) + "\n"
        s += "Defense: " + str(self.defense) + "\n"
        moves_str = "";
        for i in range(0, len(self.moves)):
            moves_str += self.moves[i] + "\t";
        moves_str += "\n";
        s += "Moves: " + moves_str + "\n";
        return s;
    
    def opp_display_str(self):
        s = "Name: " + self.name + "\n";
        s += "Health: " +  str(self.health) + "\n";
        if self.type == Constants.FIRE_TY:
            str_ty = "Type: Fire";
        elif self.type == Constants.WATER_TY:
            str_ty = "Type: Water";
        else:
            str_ty = "Type: Earth";
        s += str_ty + "\n";
        return s;
    
    def isWeakAgainst(self, other):
        if self.type == Constants.WATER_TY and other.type == Constants.EARTH_TY:
            return True;
        elif self.type == Constants.FIRE_TY and other.type == Constants.WATER_TY:
            return True;
        elif self.type == Constants.EARTH_TY and other.type == Constants.FIRE_TY:
            return True;
        else:
            return False;
    

pokemon = {};

venasaur = Pokemon("Venasaur", Constants.EARTH_TY, 30, 30);
venasaur_moves = ["Slam", "Tail Whip", "Solar Beam", "Razor Leaf"];
venasaur.addMoves(venasaur_moves);
pokemon[venasaur.name] = venasaur;

oddish = Pokemon("Oddish", Constants.EARTH_TY, 20, 20);
oddish_moves = ["Quick Attack", "Harden", "Vine Whip", "Razor Leaf"];
oddish.addMoves(oddish_moves);
pokemon[oddish.name] = oddish;

exeggutor = Pokemon("Exeggutor", Constants.EARTH_TY, 25, 25);
exeggutor_moves = ["Tackle", "Growl", "Focus Energy", "Razor Leaf"];
exeggutor.addMoves(exeggutor_moves);
pokemon[exeggutor.name] = exeggutor;

charizard = Pokemon("Charizard", Constants.FIRE_TY, 30, 30);
charizard_moves = ["Scratch", "Focus Energy", "Flamethrower", "Fire Blast"];
charizard.addMoves(charizard_moves);
pokemon[charizard.name] = charizard;

flareon = Pokemon("Flareon", Constants.FIRE_TY, 25, 25);
flareon_moves = ["Quick Attack", "Growl", "Focus Energy", "Flamethrower"];
flareon.addMoves(flareon_moves);
pokemon[flareon.name] = flareon;

growlithe = Pokemon("Growlithe", Constants.FIRE_TY, 20, 20);
growlithe_moves = ["Tackle", "Growl", "Ember", "Flamethrower"];
growlithe.addMoves(growlithe_moves);
pokemon[growlithe.name] = growlithe;

blastoise = Pokemon("Blastoise", Constants.WATER_TY, 30, 30);
blastoise_moves = ["Slam", "Harden", "Hydropump", "Surf"];
blastoise.addMoves(blastoise_moves);
pokemon[blastoise.name] = blastoise;

vaporeon = Pokemon("Vaporeon", Constants.WATER_TY, 25, 25);
vaporeon_moves = ["Quick Attack", "Tail Whip", "Growl", "Surf"];
vaporeon.addMoves(vaporeon_moves);
pokemon[vaporeon.name] = vaporeon;

staryu = Pokemon("Staryu", Constants.WATER_TY, 20, 20);
staryu_moves = ["Tackle", "Focus Energy", "Water Gun", "Surf"];
staryu.addMoves(staryu_moves);
pokemon[staryu.name] = staryu;

def displayAllPokemon(pokemon):
    for k in pokemon:
        print pokemon[k];
        