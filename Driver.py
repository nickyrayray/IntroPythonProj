# -*- coding: utf-8 -*-
"""
Created on Sat May 16 08:53:16 2015

@author: nfalba
"""

import Constants;
import Pokemon;
import PMoves;
import Player;
import random;
import copy;
import socket;

moves = PMoves.all_moves;
pokemon = Pokemon.pokemon;

class Game:
    
    def __init__(self):
        self.opp = Player.Player("Computer");
        kl = list(pokemon.keys());
        for i in range(0,3):
            z = random.randint(0, len(kl)-1);
            self.opp.addPokemon(copy.deepcopy(pokemon[kl[z]]));
            kl.pop(z);
        self.opp.chooseRandomFirstPokemon();
    
    def getPlayerInfo(self):
        name = raw_input("Enter your name: ");
        print "Thanks, %s!\n" % name;
        self.player = Player.Player(name);
        
    
    def selectPokemon(self):
        while not self.player.checkIfFull():
            print("Choose Pokemon from the list by typing in the name.\n");
            Pokemon.displayAllPokemon(pokemon);
            while True:
                choice = raw_input("Type your choice for a Pokemon, or the name of a move to hear more about it: ");
                if choice in pokemon:
                    self.player.addPokemon(copy.deepcopy(pokemon[choice]));
                    break;
                elif choice in moves:
                    print moves[choice];
                else:
                    print "Invalid Choice!";
    
    def chooseFirstPokemon(self):
        while True:
            print "Choose your first Pokemon:";
            self.player.print_pokemon();
            choice = raw_input("Your Choice: ");
            if self.player.pokemon_in_list(choice):
                self.player.choosePokemon(choice);
                print;
                return;
            else:
                print "Invalid Choice!";
    
    def displayStatus(self):
        opp_string = "Opponent: " + self.opp.name + "\n";
        opp_string += "Number of remaining Pokemon: " + str(len(self.opp.pokemon)) + "\n";
        opp_string += "Current Pokemon: " + self.opp.currentPokemon.opp_display_str() + "\n";
        s = "Battle Summary: \n\n" + opp_string + "\n";
        play_string = "Player: " + self.player.name + "\n";
        play_string += "Other Pokemon: ";
        for i in range(0, len(self.player.pokemon)):
            if(self.player.pokemon[i] is self.player.currentPokemon):
                continue;
            else:
                play_string += self.player.pokemon[i].name + "\t";
        play_string += "\n";
        play_string += "Current Pokemon: " + str(self.player.currentPokemon);
        s += play_string;
        expl_string = "Choose to use your turn by attacking or switching Pokemon.\n";
        expl_string += "To use an attack, type the name of an attack of your current Pokemon.\n";
        expl_string += "To switch pokemon, type the name of one of your remaining pokemon that you would like to switch to.";
        s += expl_string;
        print s;

    def get_opp_move(self):
        
        if len(self.opp.pokemon) == 1:
            return Constants.ATTACK;

        pokeC = self.opp.currentPokemon;
        pokeP = self.player.currentPokemon;
        
        decider = random.random();
        if pokeC.isWeakAgainst(pokeP):
            if decider < 0.75:
                return Constants.SWITCH;
            else:
                return Constants.ATTACK;
        else:
            if decider < 0.9:
                return Constants.ATTACK;
            else:
                return Constants.SWITCH;
    
    def get_opp_death_move(self):
        s = "Enemy " + self.opp.currentPokemon.name + " has fainted. \n"
        self.opp.remove_pokemon(self.opp.currentPokemon);
        self.opp.chooseRandomRemainingPokemon();
        s += self.opp.name + " sends out " + self.opp.currentPokemon.name;
        print s;
    
    def evaluatePlayerChoice(self, player_choice):
        if player_choice in self.player.currentPokemon.moves:
            self.player.currentPokemon.useMove(self.opp.currentPokemon, player_choice);
        else:
            s = self.player.name + " switched " + self.player.currentPokemon.name + " for ";
            self.player.choosePokemon(player_choice);
            s += self.player.currentPokemon.name;
            print s;

    def evaluateEngagement(self, player_choice):
        if not(player_choice in self.player.currentPokemon.moves or self.player.pokemon_in_list(player_choice)):
            return False;
        choice = self.get_opp_move();
        
        print "Turn Summary: ";
        
        if choice == Constants.SWITCH:
            s_opp = self.opp.name + " switches " + self.opp.currentPokemon.name + " for ";
            self.opp.chooseRandomRemainingPokemon();
            s_opp += self.opp.currentPokemon.name + ".";
            print s_opp;
            self.evaluatePlayerChoice(player_choice);
            if(self.opp.currentPokemon.isDead()):
                return True;
        else:
            self.evaluatePlayerChoice(player_choice);
            if(self.opp.currentPokemon.isDead()):
                return True;
            self.opp.chooseRandomMove(self.player.currentPokemon);
        return True;
            
    def choose_next_pokemon(self, prev):
        while True:
            s = prev.name + " has fainted. Choose next pokemon: ";
            print s;
            self.player.print_other_pokemon;
            choice = raw_input("Your choice: ");
            if self.player.pokemon_in_list(choice):
                self.player.remove_pokemon_and_add_new_current(prev, choice);
                print "\nYou chose: %s" % choice;
                break;
            else:
                print "You don't have that Pokemon! Select again!";
    
    def deal_with_loss(self):
        s = self.player.currentPokemon.name + " has fainted. You are out of usable Pokemon. You have lost.";
        print s;
        
    def deal_with_win(self):
        s = "Enemy " + self.opp.currentPokemon.name + " has fainted. " + self.opp.name + " is out of usable Pokemon. You win!";
        print s;
    
    def run_main_loop(self):
        self.chooseFirstPokemon();
        while True:
            self.displayStatus();
            choice = raw_input("Your choice: ");
            print;
            if not self.evaluateEngagement(choice):
                print "Invalid choice! Select again!";
            else:
                if(self.player.currentPokemon.isDead() and self.player.check_has_remaining_pokemon()):
                    self.choose_next_pokemon(self.player.currentPokemon);
                elif (self.player.currentPokemon.isDead() and not self.player.check_has_remaining_pokemon()):
                    self.deal_with_loss();
                    break;
                elif (self.opp.currentPokemon.isDead() and self.opp.check_has_remaining_pokemon()):
                    self.get_opp_death_move();
                elif (self.opp.currentPokemon.isDead() and not self.opp.check_has_remaining_pokemon()):
                    self.deal_with_win();
                    break;
                    
                    
class NetworkedGame(Game):
    
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    
    def initiate_connection(self, IP, port):
        self.socket.connect((IP, port));
    
    def wait_for_connection(self, port):
        self.socket.bind(('', port));
        self.socket.listen(3);
        (self.socket, address) = self.socket.accept();
    
    def get_initial_player_info(self):
        
        s = self.my_recv();
        
        sl = s.split('\n');
        
        self.opp = Player.Player(sl[0]);
        for i in range(1, len(sl)-1):
            self.opp.addPokemon(copy.deepcopy(pokemon[sl[i]]));
        self.opp.choosePokemon(sl[len(sl)-1]);
    
    def my_recv(self):
        bufsize = 4096;
        recv_str = "";
        while True:
            s = self.socket.recv(bufsize);
            recv_str += s;
            if len(s) != bufsize:
                break;
        return recv_str;
    
    def my_send(self, msg):
        sent = 0;
        while sent < len(msg):
            num_sent = self.socket.send(msg);
            sent += num_sent;
    
    def compose_initial_message(self):
        send_str = self.player.name + "\n";
        for i in range(0, len(self.player.pokemon)):
            send_str += self.player.pokemon[i].name + "\n";
        send_str += self.player.currentPokemon.name;
        return send_str;
    
    def setup(self):
        self.getPlayerInfo();
        self.selectPokemon();
        self.chooseFirstPokemon();
        self.my_send(self.compose_initial_message());
        self.get_initial_player_info();
    
    def send_move(self, move):
        send_str = "Attack\n" + move;
        self.my_send(send_str);
    
    def send_switch(self, pokemon_switch):
        send_str = "Switch\n";
        send_str += pokemon_switch;
        self.my_send(send_str);
    
    def recv_switch(self):
        s = self.my_recv();
        sl = s.split("\n");
        string = self.opp.currentPokemon.name + " has fainted.\n";
        string += self.opp.name + " switches to " + sl[1];
        print string;
        self.opp.choosePokemon(sl[1]);
        
    def evaluatePlayerChoice(self, player_choice):
        if player_choice in self.player.currentPokemon.moves:
            self.player.currentPokemon.useMove(self.opp.currentPokemon, player_choice);
        else:
            s = self.player.name + " switched " + self.player.currentPokemon.name + " for ";
            self.player.choosePokemon(player_choice);
            s += self.player.currentPokemon.name;
            print s;
    
    def evaluateEngagement(self, player_choice):
        if player_choice in self.player.currentPokemon.moves:
            self.send_move(player_choice);
        elif self.player.pokemon_in_list(player_choice):
            self.send_switch(player_choice);
        else:
            return False;
        
        s = self.my_recv();
        sl = s.split('\n');

        choice = sl[0];        
        
        print "Turn Summary: ";
        
        if choice == "Switch":
            s_opp = self.opp.name + " switches " + self.opp.currentPokemon.name + " for ";
            self.opp.choosePokemon(sl[1]);
            s_opp += self.opp.currentPokemon.name + ".";
            print s_opp;
            self.evaluatePlayerChoice(player_choice);
            if(self.opp.currentPokemon.isDead()):
                return True;
        elif choice == "Attack" and player_choice in self.player.currentPokemon.moves:
            if (self.opp.currentPokemon.health < self.player.currentPokemon.health):
                self.opp.currentPokemon.useMove(self.player.currentPokemon, sl[1]);
                if self.player.currentPokemon.isDead():
                    return True;
                self.player.currentPokemon.useMove(self.opp.currentPokemon, player_choice);
            elif self.opp.currentPokemon.health > self.player.currentPokemon.health:
                self.player.currentPokemon.useMove(self.opp.currentPokemon, player_choice);
                if self.opp.currentPokemon.isDead():
                    return True;
                self.opp.currentPokemon.useMove(self.player.currentPokemon, sl[1]);
            else:
                if(self.player.name < self.opp.name):
                    self.player.currentPokemon.useMove(self.opp.currentPokemon, player_choice);
                    if self.opp.currentPokemon.isDead():
                        return True;
                    self.opp.currentPokemon.useMove(self.player.currentPokemon, sl[1]);
                elif self.player.name > self.opp.name:
                    self.opp.currentPokemon.useMove(self.player.currentPokemon, sl[1]);
                    if self.player.currentPokemon.isDead():
                        return True;
                    self.player.currentPokemon.useMove(self.opp.currentPokemon, player_choice);
                else:
                    raise Exception("Players indistinguishable");
        else:
            self.player.choosePokemon(player_choice);
            self.opp.currentPokemon.useMove(self.player.currentPokemon, sl[1]);
                
        return True;
        
    def deal_with_loss(self):
        s = self.player.currentPokemon.name + " has fainted. You are out of usable Pokemon. You have lost.";
        self.socket.close();
        print s;
        
    def deal_with_win(self):
        s = "Enemy " + self.opp.currentPokemon.name + " has fainted. " + self.opp.name + " is out of usable Pokemon. You win!";
        self.socket.close();
        print s;
    
    def run_main_loop(self):
        self.setup();
        while True:
            self.displayStatus();
            choice = raw_input("Your choice: ");
            print;
            if not self.evaluateEngagement(choice):
                print "Invalid choice! Select again!";
            else:
                if(self.player.currentPokemon.isDead() and self.player.check_has_remaining_pokemon()):
                    self.choose_next_pokemon(self.player.currentPokemon);
                    self.send_switch(self.player.currentPokemon);
                elif (self.player.currentPokemon.isDead() and not self.player.check_has_remaining_pokemon()):
                    self.deal_with_loss();
                    break;
                elif (self.opp.currentPokemon.isDead() and self.opp.check_has_remaining_pokemon()):
                    self.recv_switch();
                elif (self.opp.currentPokemon.isDead() and not self.opp.check_has_remaining_pokemon()):
                    self.deal_with_win();
                    break;
              
    
print "Choose an option:\n\t 1) Battle the Computer\n\t 2) Battle a friend over a network";
option = input("Your choice: ");

if option == 1:
    game = Game();
    game.getPlayerInfo();
    game.selectPokemon();
    game.run_main_loop();
elif option == 2:
    game = NetworkedGame();
    print "Choose an option:\n\t 1) Initiate Connection\n\t 2) Wait on connection from other player";
    net_opt = input("Your choice: ");
    if net_opt == 1:
        IP = raw_input("Enter opponent's IP address: ");
        port = input("Enter port opponent is listening on: ");
        game.initiate_connection(IP, port);
    elif net_opt == 2:
        port = input("Enter port to listen for opponent on: ");
        game.wait_for_connection(port);
    game.run_main_loop();
    
    
