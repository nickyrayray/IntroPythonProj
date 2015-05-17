# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:41:10 2015

@author: nfalba
"""

import random;

STAT_MOVE_INC_ATTACK = 1;
STAT_MOVE_INC_DEFENSE = 2;
STAT_MOVE_DEC_ATTACK = 3;
STAT_MOVE_DEC_DEFENSE = 4;

EARTH_TY = 1;
FIRE_TY = 2;
WATER_TY = 3;

SWITCH = 1;
ATTACK = 2;

def calcDamage(hit_chance, amount, pokemonA, pokemonD, isSuperEffective, isNormal):
    
    chance = random.random();
    if chance > hit_chance:
        return 0;
    
    damage = 0;
    if isNormal:
        damage = amount + pokemonA.attack - pokemonD.defense;
    elif isSuperEffective:
        damage = (amount + pokemonA.attack - pokemonD.defense) * 2;
    else:
        damage = (amount + pokemonA.attack - pokemonD.defense) / 2;
    return damage;
 