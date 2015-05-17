# -*- coding: utf-8 -*-
"""
Created on Sat May 16 08:50:23 2015

@author: nfalba
"""

import random;

class Player:
    def __init__(self, name):
        self.name = name;
        self.pokemon = [];
    
    def addPokemon(self, p):
        self.pokemon.append(p);
    
    def checkIfFull(self):
        if len(self.pokemon) == 3:
            return True;
        else:
            return False;
    
    def check_has_remaining_pokemon(self):
        if len(self.pokemon) > 1:
            return True;
        else:
            return False;
    
    def remove_pokemon(self, p):
        for i in range(0, len(self.pokemon)):
            if p is self.pokemon[i]:
                ind_to_rem = i;
        self.pokemon.pop(ind_to_rem);
    
    def remove_pokemon_and_add_new_current(self, p, choice):
        for i in range(0, len(self.pokemon)):
            if p is self.pokemon[i]:
                choice_to_pop = i;
            if choice == self.pokemon[i].name:
                self.currentPokemon = self.pokemon[i];
        self.pokemon.pop(choice_to_pop);
    
    def choosePokemon(self, pokemon_name):
        for i in range(0, len(self.pokemon)):
            if pokemon_name == self.pokemon[i].name:
                self.currentPokemon = self.pokemon[i];
    
    def chooseRandomFirstPokemon(self):
        choice = random.randint(0, 2);
        self.currentPokemon = self.pokemon[choice];
    
    def chooseRandomRemainingPokemon(self):
        name_list = [];
        for i in range(0, len(self.pokemon)):
            if(self.pokemon[i].name == self.currentPokemon.name):
                continue;
            else:
                name_list.append(self.pokemon[i].name);
        choice = name_list[random.randint(0, len(name_list)-1)];
        self.choosePokemon(choice);
            
        
    def chooseRandomMove(self, pokemonT):
        self.currentPokemon.useRandomMove(pokemonT);
        
    def print_pokemon(self):
        for i in range(0, len(self.pokemon)):
            print self.pokemon[i].name;
    
    def print_other_pokemon(self):
        for i in range(0, len(self.pokemon)):
            if self.pokemon[i] is self.currentPokemon:
                continue;
            else:
                print self.pokemon[i].name;
    
    def pokemon_in_list(self, pokemon_name):
        for i in range(0, len(self.pokemon)):
            if pokemon_name == self.pokemon[i].name:
                return True;
        return False;
        