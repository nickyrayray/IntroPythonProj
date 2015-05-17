Nicholas Falba
nrf2118
Python Final Project

For my porject, I created a text-based game based on the old Poke'mon gameboy games. 

The rules are simple. You are prompted at the beginning to play against the computer or against
another player over a network. If you choose the latter, the player waiting on the connection has to
be waiting before the other player can connect. There is a big problem with the networking part but I
will explain in a second.

Once you've chosen your opponent. You are prompted to choose three Pokemon from a list. 
Each pokemon has an attack, defense, and moves stat. You can learn more about the moves
by just typing them. Pokemon with lower attack/defense stats have moves with a higer hit
percentage.

There are three types of moves. Normal is just a standard attack.
Status moves lower opponents attack/defense or increase your own
Special moves have an attribute, either fire, water, earth, which are
more effective or less effective against other types:

Water beats Fire
Fire beats Earth
Earth beats Water

Pokemon also have types which dictate the type of moves they can have.

Once you choose 3, you choose the one you want to send out into battle first.

The goal is to use attacks to destroy your opponent's pokemon first. At most, you
can only have one pokemon out at a time, but you can switch between your living 
pokemon at any time. However, this will cost you your turn, and you risk being 
damaged without retribution on the turn.

After each turn (both players select moves/pokemon to switch to), a summary of the turn and the 
status of your opponent/pokemon is displayed. You can't see everything about your oponent so 
you must pay attention.

If you use a move, but nothing seems to have happened to the other player's poke'mon, it means
the attack missed. Attacks have a higher chance of missing the more powerful they are.


Architecture:

I used several classes to build this project. Constats stored things like types and choice constants.
It also housed the formula for damage calculation from a move use.

PMoves stored the moves classes, each of which stored the hit percentage of the move, the base amount of
damage, and the name of the move. The NormalMove was subclassed into StatMoves and SpecMoves, which
also held the types of attacks (Attack_decrease, Def_increase, etc) and (Fire, Water, Earth), respectively.
This file also held a database of available moves.

Pokemon held data on poke'mon's health, it's type, and current moves.
This file also holds a database of pokemon.

Player class holds the player's and the opponent's Poke'mon, the current poke'mon and several methods for the game class.

The game class holds the player data of both the player and the opponent. It performs all the display stuff for
the text of the game. It handles all input/output of the game. And its subclass, NetworkedGame, handles all
the socket api stuff. 

Running my program:

You can run my program by running the Driver.py file in the console of Spyder. Or using "python Driver.py" from
the console. Keep the directory structure.

Packages used:

I used the copy package to create copies of the pokemon from the database for each player.
I used the random package to generate pseudo-random moves for the computer.
I used the sockets package for networking.

I also looked up online how to use the sockets API. Specifically, I looked here:
https://docs.python.org/2/howto/sockets.html
and here:
https://docs.python.org/2/library/socket.html

I cite these two because I based my methods for my_send and my_recv on the methods and discussion shown on these
pages.

Problems:

The networking part has a probelm. The way it works is that the computers send each other only the
intended moves and switches. Each computer individually does a damage calculation based on the moves.
Because of the pseudo-random nature of this calculation (e.g., some moves hit, others don't, randomly), 
the damage calculation could be different on each end. In order to fix this, I would have to redo the whole structure
of damage calculation, which is at the lowest level of my program. But I didn't have time.
Since the networking part was presented as just an extra part in my proposal anyway, I don't think it's a huge deal.
The networking aspect of the program works though (connections are formed and data exchanged as expected, taking
into account the randomness causing each end system's state to diverge). 

I wanted to make it more robust, but ran out of time.
Also, I wanted to make the program more than just text-based but I didn't have time to do this.

I genuinely enjoyed this project, though.

For parts where it asks you to choose from a numbered list, just type in the number!