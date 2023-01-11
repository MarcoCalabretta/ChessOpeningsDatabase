moves = []
player_color = ""
in_database = True
out_of_database_message = "\nYou have reached the end of the database. We don't know what to play here. Hopefully we'll add commentary after we analyse your current game."
def addmove(current_color,num_move):
    if(current_color == "white"):
        moves.append([input(str(num_move) + ".   : ")])
    elif(current_color == "black"):
        moves[num_move-1].append(input(str(num_move) + "... : "))

print("REMEMBER TO USE PROPER CHESS NOTATION OR ELSE THINGS BREAK\n")
#Prompts the user whether they're playing black or white. It will only recommend moves during the player's move
while(player_color != "white" and player_color != "black"):
    player_color = input("Are you playing as white or black? ")
    if(player_color == "white"):
        white = True
        #I use two variables here instead of one so that it's really easy to set both of them to true and look at all the database's recommendations
        black = False
    elif(player_color == "black"):
        white = False
        black = True
    else:
        print("Error. Please input either white or black: ")
"""
temptlate to add an extra move of depth(copy paste it)
#Move 1
if(in_database):
    if(white):
        if(moves == []):
            print("I recommend")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",1)
    if(black):
        if(moves == []):
            print("I recommend")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",1)
"""
#Pay close attention to the following block of code for move 1. All other moves have basically the same structure, so if you need to understand what's going on, look at move 1
#Move 1
#Recommends a move for white if the player is playing white
if(in_database):
    if(white):
        print("I recommend 1. e4, but play whatever you want. Just be aware that there will likely be less depth in the database if you play something else, because the database consists mostly of games I have played.")
    #Input white's move
    addmove("white",1)
    #Recommends a move for black if the player is playing black
    if(black):
        #Here, the program checks what the position is then reccomends a move based on that. It will do this for every single following half move until the database is out of depth
        if(moves == [["e4"]]):
            print("I recommend 1... c6, known as the caro-kann defense. The caro-kann is an opening that allows for really solid pawn structures for black, leading into a good endgame position. It is, in most variations, a lot less sharp and aggressive then other openings, which is why I prefer it.")
        elif(moves == [["d4"]]):
            print("I recommend 1... d5. Generally leads to solid play by black, although there are some fantastic alternatives that I don't know how to play, such as the dutch or indian games")
        elif(moves == [["c4"]]):
            print("I recommend 1... c6, hoping it transposes into a caro-kann or slav defense")
        elif(moves == [["Nf3"]]):
            print("I recommend 1... d5, hoping it transposes into a Queen's pawn opening")
        elif(moves == [["Nc3"]]):
            print("I recommend 1... d5, hoping it transposes into a Queen's pawn opening")
        elif(moves == [["e3"]]):
            print("I recommend 1... d5, taking space in the center")
        else:
            print(out_of_database_message)
            in_database = False
    #Inputs black's move
    addmove("black",1)
    #Sidenote, the program recommends a move FOR white, receives a move FROM white, recommends a move FOR black, THEN receives a move FROM black. The order is important here, because the program checks for the specific set of moves in the "moves" list

#Move 2
if(in_database):
    if(white):
        #e5 lines
        if(moves == [["e4","e5"]]):
            print("I recommend 2. Nf3, attacking black's e-pawn")
        #Sicilian lines
        elif(moves == [["e4","c5"]]):
            print("I recommend 2. c3. This is called the Alapin Variation of the Sicilian Defense(The Sicilian Defense is 1. e4 c5) and the idea behind it is that white plays c3 to prepare for d4, bringing two central pawns. I'm also adding lines for Nc3 followed by f4 for the grand prix attack")
        #French lines
        elif(moves == [["e4","e6"]]):
            print("I recommend 2. d4. e4 e6 is the French Defense, and 2. d4 is the main line, taking lots of center control with white's two central pawns")
        #Alekhine's defense lines
        elif(moves == [["e4","Nf6"]]):
            print("I recommend 2. e5. e4 Nf3 is Alekhine's Defense, and 2. e5 is a great line, giving white lots of central space, pawns, and tempo")
        #caro-kann lines
        elif(moves == [["e4","c6"]]):
            print("I recommend 2. d4. This is main-line caro-kann.")
        #Scandanavian lines
        elif(moves == [["e4","d5"]]):
            print("I recommend 2. exd5. This is main-line scandanavian.")
        #Owen lines
        elif(moves == [["e4","b6"]]):
            print("I recommend 2. d4. This is main-line Owen defense, where white gets early control of the center.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",2)
    if(black):
        #caro-kann lines
        if(moves == [["e4","c6"],["d4"]]):
            print("I recommend 2... d5. This is the main caro-kann line, and the whole point of putting the pawn on c6 is so that you can push d5 the next turn and keep your pawns solid and central")
        elif(moves == [["e4","c6"],["Bc4"]]):
            print("I recommend 2.. d5. The hillbilly attack(1.e4 c6 2.Bc4) is pretty bad for white, it essentially lets black force the pawn exchange, which is generally good for black in the caro-kann as it gives black extra central pawns. d5 forks white's e-pawn and bishop, forcing white to do something to address the threat instead of continuing development")
        elif(moves == [["e4","c6"],["c3"]]):
            print("I recommend 2.. d5. c3 does nothing to stop black's pawn push")
        elif(moves == [["e4","c6"],["c4"]]):
            print("I recommend 2.. d5. This is the accelerated panov attack")
        elif(moves == [["e4","c6"],["Be2"]]):
            print("I recommend 2... d5. Be2 is an odd line against the caro-kann, highly solid to just play d5 and force the exchange")
        elif(moves == [["e4","c6"],["Nf3"]]):
            print("I recommend 2... d5, taking control on the center")
        elif(moves == [["e4","c6"],["e5"]]):
            print("I recommend 2... d6, ready to trade pawns.")
        elif(moves == [["e4","c6"],["f4"]]):
            print("I recommend 2... d5, establishing a pawn center.")
        #queen's pawn opening lines
        elif(moves == [["d4","d5"],["c4"]]):
            print("I recommend 2... c6. Accepting the Queen's gambit is usually really bad for black, especially if you're inexperienced in that particular opening. I much prefer the slav defense, which is very similar to the caro-kann")
        elif(moves == [["d4","d5"],["Nc3"]]):
            print("I recommend 2... Bf5. Called the Alburt Defense, it's a nice, offbeat, active way to play agianst the Chigorin Queen's pawn opening")
        elif(moves == [["d4","d5"],["Nf3"]]):
            print("I recommend 2... Nf6. Very natural move, reinforces the d-pawn")
        elif(moves == [["d4","d5"],["e4"]]):
            print("I recommend 2... c6. Not the best move, the best move is dxe4, but that's likely what white wants you to do. playing c6 transposes into a caro-kann, which your authour is very familiar with, but white is likely to be extremely unfamiliar with. dxe4 could lead to mistakes if black isn't careful or familiar with the blackmar gambit. If you play c6, please restart the program and input e4, c6, d4, d5 to get in-depth opening analysis of the main line caro-kann.")
        #Accelerated London lines
        elif(moves == [["d4","d5"],["Bf4"]]):
            print("I recommend 2... Nf6, strengthening the d-pawn.")
        elif(moves == [["d4","d5"],["f4"]]):
            print("I recommend 2... g6. c5 is also very strong, but I prefer fianchettoing the black bishop with g6 then Bg7 followed by Bf5 O-O ideas to attack the queenside.")
        #English lines
        elif(moves == [["c4","c6"],["Nc3"]]):
            print("I recommend 2... d5, hoping it transposes into a slav defense")
        #Reti lines
        elif(moves == [["Nf3","d5"],["d4"]]):
            print("I recommend 2... c6, kinda like a slav, perfectly good move, likely to throw off the Reti players because it's not so common")
        #Van Geet Lines
        elif(moves == [["Nc3","d5"],["d4"]]):
            print("I recommend 2... Bf5. Called the Alburt Defense, it's a nice, offbeat, active way to play agianst the Chigorin Queen's pawn opening")
        #Vant krujis lines
        elif(moves == [["e3","d5"],["g3"]]):
            print("I recommend 2... e5, taking more space in the center")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",2)

#Move 3
if(in_database):
    if(white):
        #Spanish lines
        if(moves == [["e4","e5"],["Nf3","Nc6"]]):
            print("I recommend 3. Bb5, the Ruy Lopez/Spanish Game, although Bc4(the Italian) is a very strong and well-known move here, and 3. d4(the Scotch) has lines in this database")
        #Philidor lines
        elif(moves == [["e4","e5"],["Nf3","d6"]]):
            print("I recommend 3. d4, aiming to aggressively take control of the center is a great way to deal with the philidor defense")
        #Petrov defense lines
        elif(moves == [["e4","e5"],["Nf3","Nf6"]]):
            print("I recommend 3. Nc3, this is the three knights line of the Petrov defense. Other, slightly less strong alternatives are Nxe5 or d4")
        #Butch-Gauss Gambit lines
        elif(moves == [["e4","e5"],["Nf3","Bc5"]]):
            print("I recommend 3. Nxe5. Take the free pawn. Calculate a lot in positions like this, The Butch-Gauss Gambit isn't great if white plays carefully and actively")
        #Sicilian lines
        #Alapin lines
        elif(moves == [["e4","c5"],["c3","d6"]]):
            print("I recommend 3. d4. This is the point of the Alapin Sicilian, giving white center control")
        elif(moves == [["e4","c5"],["c3","d5"]]):
            print("I recommend 3. exd5, forcing black to bring out an early queen, which can be dangerous for black")
        elif(moves == [["e4","c5"],["c3","Nf6"]]):
            print("I recommend 3. e5, forcing black to move his knight and then following up with d5, giving a nice pawn chained center")
        elif(moves == [["e4","c5"],["c3","Nc6"]]):
            print("I recommend 3. d4, taking control of the center")
        elif(moves == [["e4","c5"],["c3","a6"]]):
            print("I recommend 3. d4, taking control of the center")
        elif(moves == [["e4","c5"],["c3","g6"]]):
            print("I recommend 3. d4, taking control of the center")
        #Grand Prix Lines
        elif(moves == [["e4","c5"],["Nc3","Nc6"]]):
            print("I recommend 3. f4. This is the grand prix attack. The idea is an early f4 to play Nf3 behind your pawn in order to have a nice attack on the black kingside.")
        elif(moves == [["e4","c5"],["Nc3","d6"]]):
            print("I recommend 3. f4. This is the grand prix attack. The idea is an early f4 to play Nf3 behind your pawn in order to have a nice attack on the black kingside.")
        #French lines
        elif(moves == [["e4","e6"],["d4","d5"]]):
            print("I recommend 3. e5(French Defense Advance Variation), although other strong and common responses are Nc3(Classical or Paulsen Variation) or Nd2(Tarrasch). e5 is meant to lock down on the center, and stop black's light squared bishop from ever developing. The game will likely continue with black putting enormous pressure on d4, with white defending d4 and keeping black in a closed, spaceless position")
        elif(moves == [["e4","e6"],["d4","a6"]]):
            print("I recommend 3. Bd3, solidifying white's center")
        #Alekhine's defense lines
        elif(moves == [["e4","Nf6"],["e5","Nd5"]]):
            print("I recommend 3. c4(two pawns attack), attacking black's knight again and giving white lots of space")
        #caro-kann lines
        elif(moves == [["e4","c6"],["d4","d5"]]):
            print("I recommend 3. e5. This is the advance caro-kann, which is generally the modern way of playing against the caro-kann.")
        #Scandanavian lines
        elif(moves == [["e4","d5"],["exd5","c6"]]):
            print("I recommend 3. dxc6. Free pawn, you can take it. This is the Blackburne Kloosterboer gambit, and it's better for white and not really tricky.")
        #Owen lines
        elif(moves == [["e4","b6"],["d4","Bb7"]]):
            print("I recommend 3. Nd2. This is a cool sideline, point is that it's like Nc3 except you don't block your c-pawn so you're more flexible.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",3)
    if(black):
        #caro-kann lines
        if(moves == [["e4","c6"],["d4","d5"],["e5"]]):
            print("I recommend 3... Bf5. The caro-kann advanced is pretty scary for me, but Bf5 aiming for e6 and an eventual c5 keep the oh-so important solid pawn center.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3"]]):
            print("I recommend 3... dxe4. Generally, black wants to exchange his d-pawn in the caro-kann.")
        elif(moves == [["e4","c6"],["d4","d5"],["exd5"]]):
            print("I recommend 3... cxd5, taking back the pawn and giving black 2 central pawns to white's 1")
        elif(moves == [["e4","c6"],["d4","d5"],["Nf3"]]):
            print("I recommend 3... dxe4, winning a pawn")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5"]]):
            print("I recommend 3... cxd5, giving black two central pawns to white's one, and forcing white to move his bishop, giving black even more tempo.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["Bb3"]]):
            print("I recommend 3... dxe4, we take free pawns, this gambit isn't very good, you can just take the pawn.")
        elif(moves == [["e4","c6"],["c3","d5"],["e5"]]):
            print("I recommend 3.. Bf5, hoping for an eventual e6 and turning the position into a normal caro-kann advance")
        elif(moves == [["e4","c6"],["c4","d5"],["cxd5"]]):
            print("I recommend 3.. cxd5, taking back the pawn")
        elif(moves == [["e4","c6"],["Be2","d5"],["exd5"]]):
            print("I recommend 3... cxd5, taking back the pawn and giving black 2 central pawns to white's 1")
        elif(moves == [["e4","c6"],["Nf3","d5"],["e5"]]):
            print("I recommend 3... Bf5, preparing to solidify in the center with a following e6")
        elif(moves == [["e4","c6"],["Nf3","d5"],["Nc3"]]):
            print("I recommend 3... Bg4, meaning to exchange the bishop for knight and rebuild on the dark squares")
        elif(moves == [["e4","c6"],["Nf3","d5"],["exd5"]]):
            print("I recommend 3... cxd5, retaking the pawn")
        elif(moves == [["e4","c6"],["f4","d5"],["e5"]]):
            print("I recommend 3... Bf5, developing the light squared bishop.")
        #queen's pawn opening lines
        elif(moves == [["d4","d5"],["c4","c6"],["a4"]]):
            print("I recommend 3... a5. Protects against white's queenside advances, and paves the way for black to attack on the queenside after developing and strengthening the kingside")
        elif(moves == [["d4","d5"],["c4","c6"],["Nf3"]]):
            print("I recommend 3... dxc4. Free pawns for the win. This pawn is easier to defend than the queen's gambit accepted because black already has a pawn on c6 to protect b5.")
        elif(moves == [["d4","d5"],["c4","c6"],["Nc3"]]):
            print("I recommend 3... dxc4. Free pawns for the win. This pawn is easier to defend than the queen's gambit accepted because black already has a pawn on c6 to protect b5.")
        elif(moves == [["d4","d5"],["c4","c6"],["e3"]]):
            print("I recommend 3... Bf5, preparing for e6.")
        elif(moves == [["d4","d5"],["Nc3","Bf5"],["Nf3"]]):
            print("I recommend 3... e6. Protects the d-pawn, and allows for g6, Bg7, and Ne7 at some point, getting a dragon-looking fianchetto setup")
        elif(moves == [["d4","d5"],["Nf3","Nf6"],["c4"]]):
            print("I recommend 3... c6. Transposing into the slav defense. The c-pawn is there to reinforce the d-pawn so that you can retake and keep two central pawns")
        elif(moves == [["d4","d5"],["Nf3","Nf6"],["Nc3"]]):
            print("I recommend 3... e6, preparing c5 and b6 to bring in the light squared bishop.")
        elif(moves == [["d4","d5"],["f4","g6"],["Nc3"]]):
            print("I recommend 3... Bg7. Fianchettoing the bishop is the way to go, putting pressure on d5.")
        #Accelerated London lines
        elif(moves == [["d4","d5"],["Bf4","Nf6"],["Nd2"]]):
            print("I recommend 3... g6, preparing to fianchetto the dark squared bishop.")
        elif(moves == [["d4","d5"],["Bf4","Nf6"],["e3"]]):
            print("I recommend 3... Bf5, developing the light squared bishop.")
        #Reti lines
        elif(moves == [["Nf3","d5"],["d4","c6"],["g3"]]):
            print("I recommend 3... Bf5, aiming to give black a solid center with Nf6 followed by e6 and the light squared bishop out of the pawn chain")
        #Van Geet Lines
        elif(moves == [["Nc3","d5"],["d4","Bf5"],["Bf4"]]):
            print("I recommend 3... e6, locking in the center")
        #Vant krujis lines
        elif(moves == [["e3","d5"],["g3","e5"],["Bg2"]]):
            print("I recommend 3... Nf6, developing and reinforcing the center")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",3)

#Move 4
if(in_database):
    if(white):
        #Spanish lines
        if(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","d6"]]):
            print("I recommend 4. O-O. It makes the rest of the position easier to play.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Bc5"]]):
            print("I recommend 4. O-O. It makes the rest of the position easier to play.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"]]):
            print("I recommend 4. Ba4, saving the bishop while keeping the pressure on the knight.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","f6"]]):
            print("I recommend 4. O-O, continuing development and protecting white's king.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nf6"]]):
            print("I recommend 4. O-O, continuing development and protecting white's king. After Nxe4 you can play Re1 and win back the pawn")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nd4"]]):
            print("I recommend 5. Nxd4, getting an even larger developement lead on black by taking the knight with tempo and doubling their pawns")
        #Scotch lines
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"]]):
            print("I recommend 4. Nxd4, taking back the pawn. There are some gambiting lines, but the main Scotch line is retaking the pawn, giving white central knight and central pawn")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","f6"]]):
            print("I recommend 4. Bc4, getting a large developmental lead over black.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","d5"]]):
            print("I recommend 4. Nxe5. Calculate it. If Nxe5 then dxe5 dxe4 Qxd8 now black can't castle. If dxe4 then Nxc6 and you double and isolate his pawns and his e-pawn is weak.")
        #Philidor lines
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"]]):
            print("I recommend 4. Nxd4, obviously you gotta take back the pawn, unless... 4. c3, Bird Gambit, absolute banger of a move. The idea is after dxc3 you play Nxc3 and have a big development lead and an openable e-file. The REAL idea is that no one plays this and philidor players are little babies who can't understand dynamic positions, so you can catch a lot of people off guard, even though it's not actually a good move according to the computer")
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","Qe7"]]):
            print("I recommend 4. Nc3, keeping the tension in the center and developing")
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","f6"]]):
            print("I recommend 4. Bc4, capitalizing on black's lack of development")
        #Butch-Gauss Gambit lines
        elif(moves == [["e4","e5"],["Nf3","Bc5"],["Nxe5","Qh4"]]):
            print("I recommend 4. d4. Qh4 is a mistake, and d4 gains tempo and puts pressure in the center, giving white a great position")
        #Petrov defense lines
        elif(moves == [["e4","e5"],["Nf3","Nf6"],["Nc3","Bc5"]]):
            print("I recommend 4. Nxe5, don't worry about any fried-liver type attacks with Ng4 because white can play d4 and black doesn't have an e-pawn to capture.")
        elif(moves == [["e4","e5"],["Nf3","Nf6"],["Nc3","Nc6"]]):
            print("I recommend 4. d4, taking center space.")
        #French lines
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"]]):
            print("I recommend 4. c3, supporting the d-pawn and making sure that, in the event on cxd4, white can capture back with the c-pawn to keep white's central structure. I should mention here that attacking the d-pawn is black's biggest plan in the advance french, so it is critical for white to protect its d-pawn")
        #Sicilian lines
        #Alapin Lines
        elif(moves == [["e4","c5"],["c3","d6"],["d4","cxd4"]]):
            print("I recommend 4. cxd4, giving white two central pawns and a fantastic opening position")
        elif(moves == [["e4","c5"],["c3","d5"],["exd5","Qxd5"]]):
            print("I recommend 4. d4, taking control of the center")
        elif(moves == [["e4","c5"],["c3","Nf6"],["e5","Nd5"]]):
            print("I recommend 4. d4, controlling the center")
        elif(moves == [["e4","c5"],["c3","Nc6"],["d4","e6"]]):
            print("I recommend 4. Nf3, developing towards the center.")
        elif(moves == [["e4","c5"],["c3","a6"],["d4","cxd4"]]):
            print("I recommend 4. cxd4, taking control of the center and having an ideal center")
        elif(moves == [["e4","c5"],["c3","g6"],["d4","cxd4"]]):
            print("I recommend 4. cxd4, the whole point of the alapin")
        #Grand Prix Lines
        elif(moves == [["e4","c5"],["Nc3","Nc6"],["f4","a6"]]):
            print("I recommend 4. Bc4, developing the bishop immediatelly to respond to b5 with Bd5 and trading it off. The only alternative is to develop the bishop with g6 Bg7, which I think is too clunky and forces white to change their main idea in the opening.")
        elif(moves == [["e4","c5"],["Nc3","Nc6"],["f4","g6"]]):
            print("I recommend 4. Nf3, developping the knight behind the f-pawn, which is the whole point of f4.")
        elif(moves == [["e4","c5"],["Nc3","d6"],["f4","e6"]]):
            print("I recommend 4. Nf3. Developping your knight behind your f-pawn.")
        #Alekhine's defense lines
        elif(moves == [["e4","Nf6"],["e5","Nd5"],["c4","Nb6"]]):
            print("I recommend 4. d4, taking control of the center. Be careful now, white has a great position and now just needs to solidify")
        #caro-kann lines
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"]]):
            print("I recommend 4. h4. This is the Tal Variation of the advance caro-kann, named after world champion Mikhail Tal. The point of this move is that the best move here is 4... h5. if black plays h6 instead, you play g4, forcing the black bishop to h7, then play e6, gambiting your e-pawn to severely weaken the light squares around the black king. You then trade light squared bishops with Bd3, then attack the black king with everything and the kitchen sink. ALTERNATE MOVE is 4. Nc3, the Van der Wiel attack. The idea is that after e6, white plays g4, attacking the bishop and then starts to go nuts with a kingside pawn storm designed to decimate the light squares around the black king. There are lines for both these variations in the database")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","c5"]]):
            print("I recommend 4. Nf3. After cxd4 Nxd4 you can just defend the e-pawn with f4 and your knight is now well placed.")
        #Scandanavian lines
        elif(moves == [["e4","d5"],["exd5","c6"],["dxc6","Nxc6"]]):
            print("I recommend 4. Bb5. There's a few moves you can make here, but I like Bb5 because it pins the black knight and puts pressure on the black position.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",4)
    if(black):
        #caro-kann lines
        if(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["c3"]]):
            print("I recommend 4... e6. This stops all of white's future e6 pawn sacrifice dreams and solidifies black's center")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4"]]):
            print("I recommend 4... h5. Best move. Look it up later. The idea is that h6 fails after g4 Bh7 then 6. e6, an absolute banger of a pawn sacrifice which is really bad for black. h5 avoids this problem and also avoids having to retreat the light-squared bishop.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Bd3"]]):
            print("I recommend 4... Bxd3. getting rid of white's good bishop with black's bad bishop, judging by the central pawn structure")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3"]]):
            print("I recommend 4... e6, solidifying the center")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h3"]]):
            print("I recommend 4... e6, solidifying the center")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nf3"]]):
            print("I recommend 4... e6, solidifying the center")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["f4"]]):
            print("I recommend 4... e6, solidifying the center")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4"]]):
            print("I recommend 4... Bf5, attacking white's knight.")
        elif(moves == [["e4","c6"],["d4","d5"],["exd5","cxd5"],["Nf3"]]):
            print("I recommend 4... Nc6, pressuring the d4 pawn. knights before bishops, you know how it is.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nf3","dxe4"],["Ng5"]]):
            print("I recommend 4... Nf6, protecting the pawn and developing a knight")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3"]]):
            print("I recommend 4... e5, giving black a perfect pawn center.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["Bb3","dxe4"],["Qh5"]]):
            print("I recommend 4... g6, winning tempo on the queen while getting ready to fianchetto your bishop. e6 is also good, I just think it makes developing black's light squared bishop difficult.")
        elif(moves == [["e4","c6"],["c4","d5"],["cxd5","cxd5"],["exd5"]]):
            print("I recommend 4.. Qxd5, taking back the pawn. Interesting line is Nf6, which initially gambits the pawn to gain back some activity and development")
        elif(moves == [["e4","c6"],["c3","d5"],["e5","Bf5"],["d4"]]):
            print("I recommend 4... e6, transposing into a normal caro-kann advance")
        elif(moves == [["e4","c6"],["Be2","d5"],["exd5","cxd5"],["Bf3"]]):
            print("I recommend 4... e5, giving black an ideal pawn center")
        elif(moves == [["e4","c6"],["Nf3","d5"],["e5","Bf5"],["d4"]]):
            print("I recommend 4... e6, solidifying the center")
        elif(moves == [["e4","c6"],["Nf3","d5"],["exd5","cxd5"],["d4"]]):
            print("I recommend 4... g6, readying a bishop fianchetto. Bf5 isnt necessary because you can play b6 and double fianchetto without a c6 pawn in the way of the light squared bishop")
        elif(moves == [["e4","c6"],["f4","d5"],["e5","Bf5"],["Nf3"]]):
            print("I recommend 4... e6, locking in the pawn center.")
        #queen's pawn opening lines
        elif(moves == [["d4","d5"],["c4","c6"],["a4","a5"],["Nc3"]]):
            print("I recommend 4... Nf6. DO NOT PLAY Bf5!!!!. It can lead to 5. Qb3, where you cannot protect both your b-pawn and d-pawn and you lose a pawn on move 5. That would suck. Reinforce your d-pawn instead with Nf6")
        elif(moves == [["d4","d5"],["c4","c6"],["Nc3","dxc4"],["a4"]]):
            print("I recommend 4... e5. Give back the pawn momentarily in exchange for a queen trade with tempo, and the pawn is quite difficult to defend after Nd7, so black will probably win it back.")
        elif(moves == [["d4","d5"],["c4","c6"],["Nc3","dxc4"],["e3"]]):
            print("I recommend 4... b5, protecting the c-pawn.")
        elif(moves == [["d4","d5"],["c4","c6"],["Nf3","dxc4"],["e4"]]):
            print("I recommend 4... b5, protecting the c-pawn.")
        elif(moves == [["d4","d5"],["c4","c6"],["e3","Bf5"],["cxd4"]]):
            print("I recommend 4... cxd4, retaking the pawn.")
        elif(moves == [["d4","d5"],["c4","c6"],["e3","Bf5"],["Nc3"]]):
            print("I recommend 4... e6, solidifying the center.")
        elif(moves == [["d4","d5"],["Nf3","Nf6"],["c4","c6"],["Bg5"]]):
            print("I recommend 4... dxc4. We take free pawns over here")
        elif(moves == [["d4","d5"],["f4","g6"],["Nc3","Bg7"],["Nf3"]]):
            print("I recommend 4... Bf5. Feel free to play what you want here though. I prefer Bf5 because it allows an e6 and frees up all the space for the knights to develop to their best squares. The bishops are basically in their optimal squares at this point, and black now needs space to develop the knights to their best squares, c4 and e4.")
        #Accelerated London lines
        elif(moves == [["d4","d5"],["Bf4","Nf6"],["e3","Bf5"],["c4"]]):
            print("I recommend 4... c6, reinforcing the center.")
        #Reti lines
        elif(moves == [["Nf3","d5"],["d4","c6"],["g3"]]):
            print("I recommend 4... Nf6, black wants to avoid trading knight for bishop as it ruins pawn structure, and e6 blocks out the light squared bishop so that white can play Nh4 at some point and force the trade")
        #Vant krujis lines
        elif(moves == [["e3","d5"],["g3","e5"],["Bg2","Nf6"],["c3"]]):
            print("I recommend 4... Nc6, developing and reinforcing the center")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",4)

#Move 5
if(in_database):
    if(white):
        #Spanish lines
        if(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","d6"],["O-O","a6"]]):
            print("I recommend 5. Ba4, keeping the pressure on the knight.")
        if(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","d6"],["O-O","Bg4"]]):
            print("I recommend 5. h3, pressuring the bishop.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Bc5"],["O-O","Nf6"]]):
            print("I recommend 5. d3, defending the e-pawn.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Bc5"],["O-O","a6"]]):
            print("I recommend 5. Bxc6. a6 is a mistake and lets you win a pawn after removing the c-knight from the defence of the e-pawn.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","b5"]]):
            print("I recommend 5. Bb3, saving the bishop.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","Nf6"]]):
            print("I recommend 5. O-O, ready to play Re1 if Nxe4 winning back the pawn.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","f6"],["O-O","a6"]]):
            print("I recommend 5. Bc4, stopping black from castling.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nf6"],["O-O","d6"]]):
            print("I recommend 5. Re1, protecting the pawn")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nd4"],["Nxd4","exd4"]]):
            print("I recommend 5. O-O, getting the king safe and preparing to develop")
        #Scotch lines
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Nf6"]]):
            print("I recommend 5. Nxc6, potentially leading to some nice lines attacking black's f6 knight")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Nxd4"]]):
            print("I recommend 5. Qxd4, obviously")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Bc5"]]):
            print("I recommend 5. Be3, developing and protecting the knight, as well as potentially leading to a nice tactic if black isn't careful with Nxc6 bxc6 Bxc5")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Qh4"]]):
            print("I recommend 5. Nc3, developing and protecting the pawn")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","d6"]]):
            print("I recommend 5. Nc3, developing and protecting the pawn")
        #Philidor lines
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"],["c3","dxc3"]]):
            print("I recommend 5. Nxc3, also Bc4 is good hoping for cxb2 Bxb2 with like a Danish Gambit type thing")
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"],["Nxd4","Be7"]]):
            print("I recommend 5. Nc3, bringing your knight into the center and protecting your e-pawn")
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"],["Nxd4","a6"]]):
            print("I recommend 5. Nc3, bringing your knight into the center and protecting your e-pawn")
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"],["Nxd4","Nf6"]]):
            print("I recommend 5. Nc3, bringing your knight into the center and protecting your e-pawn")
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","f6"],["Bc4","Qe7"]]):
            print("I recommend 5. O-O, nice low elo trap, if 5... exd4 6. Nxd4 Qxe4, you win the game instantly after Re1")
        #Petrov defense lines
        elif(moves == [["e4","e5"],["Nf3","Nf6"],["Nc3","Nc6"],["d4","exd4"]]):
            print("I recommend 5. Nxe4, recapturing in the center.")
        #French lines
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","Nc6"]]):
            print("I recommend 5. Nf3, strengthening the d-pawn")
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","a6"]]):
            print("I recommend 5. Nf3, strengthening the d-pawn")
        #Sicilian lines
        #Alapin Lines
        elif(moves == [["e4","c5"],["c3","d6"],["d4","cxd4"],["cxd4","a6"]]):
            print("I recommend 5. Nf3. Nc3 is also great, the idea at this point is to keep developing")
        elif(moves == [["e4","c5"],["c3","d5"],["exd5","Qxd5"],["d4","Bf5"]]):
            print("I recommend 5. Nf3, the idea behind this is just to defend the d-pawn, and I think it's the best move because you're going to move the knight there anyway, while there's maybe a bit of ambiguity as to where the dark squared bishop is going")
        elif(moves == [["e4","c5"],["c3","d5"],["exd5","Qxd5"],["d4","cxd4"]]):
            print("I recommend 5. cxd4, keeping a powerful Isolated Queen's Pawn in the center")
        elif(moves == [["e4","c5"],["c3","Nf6"],["e5","Nd5"],["d4","cxd4"]]):
            print("I recommend 5. Nf3, controlling the center. Black can't take the c-pawn because of QxN, so white just develops instead of immediately recapturing")
        elif(moves == [["e4","c5"],["c3","Nc6"],["d4","e6"],["Nf3","Nf6"]]):
            print("I recommend 5. e5, chasing black's knight to a bad square.")
        elif(moves == [["e4","c5"],["c3","a6"],["d4","cxd4"],["cxd4","e6"]]):
            print("I recommend 5. Nc3, developing the knight to its best square and controlling the center")
        elif(moves == [["e4","c5"],["c3","g6"],["d4","cxd4"],["cxd4","d5"]]):
            print("I recommend 5. Bb5+, a nice in between move that either forces a pin with Nc6 or forces Bd7 leading to a bad-for-good bishop trade")
        #Grand Prix Lines
        elif(moves == [["e4","c5"],["Nc3","Nc6"],["f4","a6"],["Bc4","e6"]]):
            print("I recommend 5. a3, ready to retreat the bishop to a2 after b5 because Bd5 is no longer possible.")
        elif(moves == [["e4","c5"],["Nc3","Nc6"],["f4","g6"],["Nf3","Bg7"]]):
            print("I recommend 5. Bb5, Bc4 is also very good, I think better, but at the time of writing, I am quite inexperienced at the Grand Prix, so I think Bb5 planning to trade off white's probem bishop is a good idea. I often have lots of trouble with Bc4 ideas because of an a6-b5 expansion on the black queenside that wins a lot of time on me.")
        elif(moves == [["e4","c5"],["Nc3","d6"],["f4","e6"],["Nf3","d5"]]):
            print("I recommend 5. Bb5+, developping your bishop with tempo.")
        #Alekhine's defense lines
        elif(moves == [["e4","Nf6"],["e5","Nd5"],["c4","Nb6"],["d4","d6"]]):
            print("I recommend 5. Nf3. DO NOT PLAY f4, which would cause lots of weaknesses around the white king.")
        #caro-kann lines
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4","Qd7"]]):
            print("I recommend 5. c3. Forget about all your attacking dreams and just play solid chess.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"]]):
            print("I recommend 5. g4. This is the whole point, gaining big space on the kingside with tempo.")
        #Scandanavian lines
        elif(moves == [["e4","d5"],["exd5","c6"],["dxc6","Nxc6"],["Bb5","Bd7"]]):
            print("I recommend 5. Nf3, developping.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",5)
    if(black):
        #caro-kann lines
        if(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["c3","e6"],["h3"]]):
            print("I recommend 5... Ne7. This does look ugly because it blocks out the dark squared bishop, but it's to build into Ng6, where you leave it in a nice kingside position along with your bishop and then move Be7 afterwards. Otherwise, you'll either be playing c5 at some point to bring out your dark squared bishop(bad because he has a c3 pawn).")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4","h5"],["Nf3"]]):
            print("I recommend 5... e6, closing up the center and opening up the dark-squared bishop.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4","h5"],["Bg5"]]):
            print("I recommend 5... Qb6, winning a tempo by threatening b2 and unpinning to play e6.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4","h5"],["Bd3"]]):
            print("I recommend 5... Bxd3, trading off black's problem bishop.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Bd3","Bxd3"],["Qxd3"]]):
            print("I recommend 5... e6, solidifying the center for black")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nf3","e6"],["Bd3"]]):
            print("I recommend 5... Ne7, ready to take the bishop back")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"],["Nf3"]]):
            print("I recommend 5... c5, trading a wing pawn for white's crucial d-pawn")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["f4","e6"],["Nf3"]]):
            print("I recommend 5... c5, opening the center.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h3","e6"],["a3"]]):
            print("I recommend 5... Nd7, developing and preparing for a c5 push.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Bd3"]]):
            print("I recommend 5... Qxd4, taking a free pawn.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Qf3"]]):
            print("I recommend 5... e6, protecting the bishop, opening for the dark-squared bishop, and targeting white's d-pawn.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["f3"]]):
            print("I recommend 5... e6, solidifying the center. Taking with Bxe4 is bad because it gives white two central pawns.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Ng3"]]):
            print("I recommend 5... Bg6, protecting the bishop.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Nc5"]]):
            print("I recommend 5... Qb6. e5 is also great, but your authour dislikes it because it isolates black's a-pawn after Nxb7. Black gets a center pawn in compensation for a side pawn, but at the cost of solid pawn structure. Qb6, by contrast, allows black to retain pawn structure and push for e5 or e6 later and attack the d-pawn and open the dark-squared bishop.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nf3","dxe4"],["Ng5","Nf6"],["Nc3"]]):
            print("I recommend 5... Bf5, protecting the pawn and developing another piece.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3","Bf5"],["d3"]]):
            print("I recommend 5... Nf6, furthering development and reinforcing your d-pawn.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3","e5"],["Nc3"]]):
            print("I recommend 5... Nf6, furthering development and reinforcing your d-pawn.")
        elif(moves == [["e4","c6"],["c3","d5"],["e5","Bf5"],["d4","e6"],["Nf3"]]):
            print("I recommend 5... Ne7. This does look ugly because it blocks out the dark squared bishop, but it's to build into Ng6, where you leave it in a nice kingside position along with your bishop and then move Be7 afterwards. Otherwise, you'll either be playing c5 at some point to bring out your dark squared bishop(bad because he has a c3 pawn)")
        elif(moves == [["e4","c6"],["Be2","d5"],["exd5","cxd5"],["Bf3","e5"],["d3"]]):
            print("I recommend 5... Nf6, threatening a potential e4 push, although try not to do e4 right away as it could lead to a queen trade leaving black unable to castle")
        elif(moves == [["e4","c6"],["Nf3","d5"],["e5","Bf5"],["d4","e6"],["Bg5"]]):
            print("I recommend 5... Ne7, blocking the queen attack and preparing for a potential Qb6")
        elif(moves == [["e4","c6"],["Nf3","d5"],["e5","Bf5"],["d4","e6"],["Bd3"]]):
            print("I recommend 5... Bxd3, exchanging black's potentially bad bishop for white's potentially good bishop, based on the central pawn structure")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3","e5"],["Nf3"]]):
            print("I recommend 5... e4, making the white knight jump around the board while black gains tempo.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["Bb3","dxe4"],["Qh5","g6"],["Qe5"]]):
            print("I recommend 5... Nf6, then laugh at your opponent because they let you develop.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["f4","e6"],["Nc3"]]):
            print("I recommend 5... c5, destabilising white's center. It's important to play c5 now while white's knight is in the way of him playing c3")
        elif(moves == [["e4","c6"],["f4","d5"],["e5","Bf5"],["Nf3","e6"],["d5"]]):
            print("I recommend 5... c5, attacking white's center.")
        #queen's pawn opening lines
        elif(moves == [["d4","d5"],["Nf3","Nf6"],["c4","c6"],["Bg5","dxc4"],["Bxf6"]]):
            print("I recommend 5... exf6, keeping your kingside pawn structure intact")
        elif(moves == [["d4","d5"],["c4","c6"],["Nf3","dxc4"],["e4","b5"],["Nc3"]]):
            print("I recommend 5... Nf6, pressuring the center. If e5 you shmoove the knight over to the outpost on d5 and have yourself a swell time.")
        elif(moves == [["d4","d5"],["c4","c6"],["Nc3","dxc4"],["e3","b5"],["Qf3"]]):
            print("I recommend 5... Nf6. Nxb5 doesn't need to be protected against because after Bg4, forcing the queen off of the long diagonal, black wins the knight.")
        elif(moves == [["d4","d5"],["c4","c6"],["e3","Bf5"],["cxd4","cxd4"],["Bd3"]]):
            print("I recommend 5... Bxd3, exchanging black's bad bishop for white's good bishop. Congratulations! Black now has equality if not a slightly better position.")
        elif(moves == [["d4","d5"],["c4","c6"],["e3","Bf5"],["Nc3","e6"],["cxd5"]]):
            print("I recommend 5... exd5, retaking and keeping your king's diagonal safe and your light-squared bishop useful.")
        elif(moves == [["d4","d5"],["f4","g6"],["Nc3","Bg7"],["Nf3","Bf5"],["e3"]]):
            print("I recommend 5... e6. The reason is because it brings flexibility, allowing black to develop the knight to d7 or f6, depending on the ensuing position.")
        #Accelerated London lines
        elif(moves == [["d4","d5"],["Bf4","Nf6"],["e3","Bf5"],["c4","c6"],["Qb3"]]):
            print("I recommend 5... Nbd7, setting a trap. Qxb7 is actually a blunder for white now, because after e5, blocking white's dark squared bishop, then Rb8, forcing the queen away, black starts a devastating attack against the white king. Moves like Qa5, Bb4, Rxb2, and black is sure to win at least white's b1 knight.")
        elif(moves == [["d4","d5"],["Bf4","Nf6"],["e3","Bf5"],["c4","c6"],["Nc3"]]):
            print("I recommend 5... e6, reinforcing the center.")
        #Vant krujis lines
        elif(moves == [["e3","d5"],["g3","e5"],["Bg2","Nf6"],["c3","Nc6"],["b3"]]):
            print("I recommend 5... Bd6, developing and reinforcing the center")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",5)

#Move 6
if(in_database):
    if(white):
        #Spanish lines
        if(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","d6"],["O-O","a6"],["Ba4","b5"]]):
            print("I recommend 6. Bb3, stopping the bishop from being taken.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Bc5"],["O-O","a6"],["Bxc6","dxc6"]]):
            print("I recommend 6. Nxe5, free pawn.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","b5"],["Bb3","Be7"]]):
            print("I recommend 6. O-O, Preparing Re1 and keeping the king safe.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","Nf6"],["O-O","b5"]]):
            print("I recommend 6. Bb3, saving the bishop.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nf6"],["O-O","d6"],["Re1","Be7"]]):
            print("I recommend 6. c3, preparing for d4")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nd4"],["Nxd4","exd4"],["O-O","c6"]]):
            print("I recommend 6. Bc4, moving the bishop to a better diagonal")
        #Scotch lines
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Nf6"],["Nxc6","bxc6"]]):
            print("I recommend 6. Bd3, strengthening the e-pawn. I don't recommend Nc3 because Bb4 leads to a pin that is only escapeable by 7. Bd2 Bxc3 8. Bxc3 Nxe4 9. Bxg7, trading a center pawn for a flank pawn, it is in my opinion, quite awkward, so just play Bd3 instead")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Nxd4"],["Qxd4","Qf6"]]):
            print("I recommend 6. Qc4, trying not to trade queens so early because white has better attacking chances here")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Bc5"],["Be3","d6"]]):
            print("I recommend 6. Nxc6. Only good move here. You take his knight, then bishop, then queen, tripling black pawns and stopping black from castling")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Bc5"],["Be3","Bxd4"]]):
            print("I recommend 6. Bxd4, obviously.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Qh4"],["Nc3","Bb4"]]):
            print("I recommend 6. Be2, gambiting the pawn. After Qxe4 you play Nb5 and watch the madness ensue as black tries to stop the fork on c7(this gambit is supported by computer evaluations as being up for white)")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","d6"],["Nc3","Nf6"]]):
            print("I recommend 6. Bb5, attacking the knight. Bonus for lower rated players because the only good move is Bd7(or maybe Qd7) or else you play Nxc6 bxc6 Bxc6+ and win the game")
        #Philidor lines
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"],["c3","dxc3"],["Nxc3","g6"]]):
            print("I recommend 6. Bb5+, gaining time then playing Bc4")
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"],["Nxd4","Be7"],["Nc3","Nf6"]]):
            print("I recommend 6. Bc4. It's a great attacking diagonal, and there's a chance he might mess up and play Be6, in which case you go 6... Bxe6 7. fxe6 Nxe6, queen moves followed by Nxg7 which is mad nice for white")
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"],["Nxd4","Nf6"],["Nc3","Be7"]]):
            print("I recommend 6. Bf4, developping your dark-squared bishop. The reason I prefer this over Bc4 is that you might play Bb5 if black plays Nc6 at some point.")
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","f6"],["Bc4","Qe7"],["O-O","Bg4"]]):
            print("I recommend 6. c3, reinforcing the d-pawn so you can retake and have two central pawns")
        #Petrov defense lines
        elif(moves == [["e4","e5"],["Nf3","Nf6"],["Nc3","Nc6"],["d4","exd4"],["Nxe4","Bb4"]]):
            print("I recommend 6. Nxc6, letting black double white's c-pawns in exchange for a doubling of their own c-pawns.")
        #French lines
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","Nc6"],["Nf3","Qb6"]]):
            print("I recommend 6. a3, preparing for b4 to stop the queen's attack. DO NOT PLAY b3! It leads to cxd4 cxd4 Bb4+ and white loses the d-pawn")
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","Nc6"],["Nf3","Bd7"]]):
            print("I recommend 6. Be2, developing to castle and leaving the dark-squared bishop to protect b2 for now")
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","Nc6"],["Nf3","Nge7"]]):
            print("I recommend 6. Bd3, putting the light-squared bishop in its best place. Respond to Qb6 with Bc2, leaving the bishop on the long diagonal necessary to counteract black's e7 knight from moving to f5 or maybe g6.")
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","a6"],["Nf3","Nc6"]]):
            print("I recommend 6. Bd3, getting ready to castle")
        #Sicilian lines
        #Alapin Lines
        elif(moves == [["e4","c5"],["c3","d6"],["d4","cxd4"],["cxd4","a6"],["Nc3","g6"]]):
            print("I recommend 6. Bc4. This can lead to some great attacking lines if black isn't careful")
        elif(moves == [["e4","c5"],["c3","d5"],["exd5","Qxd5"],["d4","Bf5"],["Nf3","Nc6"]]):
            print("I recommend 6. Be3, defending the d-pawn")
        elif(moves == [["e4","c5"],["c3","d5"],["exd5","Qxd5"],["d4","cxd4"],["cxd4","Nc6"]]):
            print("I recommend 6. Nf3, protecting the pawn")
        elif(moves == [["e4","c5"],["c3","Nc6"],["d4","e6"],["Nf3","Nf6"],["e5","Nd5"]]):
            print("I recommend 6. c4, chasing black's knight to a bad square.")
        elif(moves == [["e4","c5"],["c3","d5"],["exd5","Qxd5"],["d4","e6"]]):
            print("I recommend 6. Be3, reinforcing the d-pawn, although you will still retake with the c-pawn if cxd4.")
        elif(moves == [["e4","c5"],["c3","a6"],["d4","cxd4"],["cxd4","e6"],["Nc3","Nc6"]]):
            print("I recommend 6. d5, if black takes you can retake and both have isolated pawns, while also gaining time on black's knight. the pawn is very safe on d5, guarded by the knight, and so white will have no problems developing and ending up with an open position with more space.")
        elif(moves == [["e4","c5"],["c3","Nf6"],["e5","Nd5"],["d4","cxd4"],["Nf3","e6"]]):
            print("I recommend 6. cxd4, retaking the pawn and opening c3 for the white knight.")
        elif(moves == [["e4","c5"],["c3","g6"],["d4","cxd4"],["cxd4","d5"],["Bb5+","Nc6"]]):
            print("I recommend 6. Nc3, threatening exd5, if black takes play d5 anyway because the knight is pinned")
        #Grand Prix Lines
        elif(moves == [["e4","c5"],["Nc3","Nc6"],["f4","a6"],["Bc4","e6"],["a3","b5"]]):
            print("I recommend 6. Ba2, keeping the bishop on a strong diagonal.")
        elif(moves == [["e4","c5"],["Nc3","Nc6"],["f4","g6"],["Nf3","Bg7"],["Bc4","e6"]]):
            print("I recommend 6. e5, blocking out the black bishop before black can play d6.")
        #Caro-Kann lines
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"],["g4","Bg6"]]):
            print("I recommend 6. Nge2. preparing Nf4 hitting the bishop and h5 square. important to remember move order here. Knight first, then pawn, then knight again. h4 first leads to h5 and your knight is to slow. Moving the knight twice gives him enoug time for counterplay with c5 Nc6. Remember the order.")
        #Scandanavian lines
        elif(moves == [["e4","d5"],["exd5","c6"],["dxc6","Nxc6"],["Bb5","Bd7"],["Nf3, e6"]]):
            print("I recommend 6. c3, giving escape room for your bishop.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",6)
    if(black):
        #Caro-Kann lines
        if(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Bd3","Bxd3"],["Qxd3","e6"],["Nf3"]]):
            print("I recommend 6... Ne7. This does look ugly because it blocks out the dark squared bishop, but it's to build into Ng6, where you leave it in a nice kingside position along with your bishop and then move Be7 afterwards, looking for O-O and c5 eventually")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4","h5"],["Nf3","e6"],["Nbd2"]]):
            print("I recommend 6... c5, attacking white's center before playing Nc6.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"],["Nf3","Bd3"]]):
            print("I recommend 6... Bxd3, trading black's somewhat weak light squared bishop and allowing cxd4 without having a white pawn on d4 for a long time")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nf3","e6"],["Bd3","Ne7"],["O-O"]]):
            print("I recommend 6... Nd7, developing the knight. Other alternatives such as c5 right away, gambiting a pawn, or Bxd3 Qxd3 Nf5/Ng6 aren't quite as strong")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nf3","e6"],["Bf5","Qb6"],["Nbd2"]]):
            print("I recommend 6... Qxb2, taking the free pawn")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["f4","e6"],["Nf3","c5"],["c3"]]):
            print("I recommend 6... Nc6, developing the knight to its best square.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h3","e6"],["a3","Nd7"],["Bd3"]]):
            print("I recommend 6... Ne7, preparing to recapture the bishop.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4","h5"],["Bd3","Bxd3"],["Qxd3"]]):
            print("I recommend 6... e6, solidifying the center.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Bd3","Qxd4"],["Nf3"]]):
            print("I recommend 6... Qd1, retreating the queen.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Ng3","Bg6"],["Nf3"]]):
            print("I recommend 6... e6, preparing for Ne7 to protect the bishop in the case of Ne5.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Ng3","Bg6"],["N1e2"]]):
            print("I recommend 6... e6, preparing for Ne7 to protect the bishop in the case of Nf4.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3","Bf5"],["d3","Nf6"],["Bg5"]]):
            print("I recommend 6... e6, reinforcing your d-pawn and opening up for your dark-squared bishop.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["Bb3","dxe4"],["Qh5","g6"],["Qe5","Nf6"],["Nc3"]]):
            print("I recommend 6... Qd6, trying to force a queen trade that removes your weaknesses by undoubling your e-pawns and letting your play d5 and protect everything after Qxd6 exd6.")
        elif(moves == [["e4","c6"],["c3","d5"],["e5","Bf5"],["d4","e6"],["Nf3","Ne7"],["Be2"]]):
            print("I recommend 6... Ng6, completing the plan from last move")
        elif(moves == [["e4","c6"],["Be2","d5"],["exd5","cxd5"],["Bf3","e5"],["d3","Nf6"],["Bg5"]]):
            print("I recommend 6... Nbd7, protecting your knight with another knight so that you can simultaneously give the a-rook some space and keep the pressure on e4. If 7. Bxd5 you have 7... Qa5+ 8. Nc3 Nxd5")
        elif(moves == [["e4","c6"],["Nf3","d5"],["e5","Bf5"],["d4","e6"],["Bd3","Bxd3"],["Qxd3"]]):
            print("I recommend 6... Ne7. This does look ugly because it blocks out the dark squared bishop temporarily, but it's to build into Ng6, where you leave it in a nice kingside position along with your bishop and then move Be7 afterwards.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3","e5"],["Nf3","e4"],["Nd4"]]):
            print("I recommend 6... Nc6, making white trade knights and giving black a solid central pawn structure. If white doesn't trade knights, black can continue chasing it around the board gaining tempo.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["f4","e6"],["Nc3","c5"],["Bb5+"]]):
            print("I recommend 6... Nc6, stopping the check and developing your knight")
        elif(moves == [["e4","c6"],["f4","d5"],["e5","Bf5"],["Nf3","e6"],["d5","c5"],["c3"]]):
            print("I recommend 6... Nc6, developing the knight to its ideal square.")
        #queen's pawn opening lines
        elif(moves == [["d4","d5"],["Nf3","Nf6"],["c4","c6"],["Bg5","dxc4"],["Bxf6","exf6"],["e4"]]):
            print("I recommend 6... b5, protecting the pawn. Note how this is different than normal queen's gambit accepted because the c-pawn is already supporting the d-pawn.")
        elif(moves == [["d4","d5"],["c4","c6"],["e3","Bf5"],["cxd4","cxd4"],["Bd3","Bxd3"],["Qxd3"]]):
            print("I recommend 6... Nf6, controlling the e4 square.")
        elif(moves == [["d4","d5"],["c4","c6"],["e3","Bf5"],["Nc3","e6"],["cxd5","exd5"],["Qb3"]]):
            print("I recommend 6... Qb6, inviting a tade of queens to open your a-rook.")
        elif(moves == [["d4","d5"],["f4","g6"],["Nc3","Bg7"],["Nf3","Bf5"],["e3","e6"],["Bd3"]]):
            print("I recommend 6... Nd7, ready to recapture the bishop on f5 if needed.")
        #Accelerated London lines
        elif(moves == [["d4","d5"],["Bf4","Nf6"],["e3","Bf5"],["c4","c6"],["Nc3","e6"],["Qb3"]]):
            print("I recommend 6... Qc8, protecting the pawn on b7. The reason I don't like Qb6 is because after c5 you're forced into Qxb3 giving white an active rook and more space for no reason.")
        #Vant krujis lines
        elif(moves == [["e3","d5"],["g3","e5"],["Bg2","Nf6"],["c3","Nc6"],["b3","Bd6"],["Bb2"]]):
            print("I recommend 6... Bf5, developing and reinforcing the center")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",6)

#Move 7
if(in_database):
    if(white):
        #Spanish lines
        if(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","d6"],["O-O","a6"],["Ba4","b5"],["Bb3","Bb7"]]):
            print("I recommend 7. c3, preparing d4.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Bc5"],["O-O","a6"],["Bxc6","dxc6"],["Nxe5","Qf6"]]):
            print("I recommend 7. d4, winning tempo, taking space, and protecting the knight at the same time.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","b5"],["Bb3","Be7"],["O-O","Nf6"]]):
            print("I recommend 7. Re1, protecting the e-pawn.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","Nf6"],["O-O","b5"],["Bb3","d6"]]):
            print("I recommend 7. Re1, protecting the e-pawn. Na5 isn't that good for black here because after d4 breaking open the center, white gains a lot of time.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nf6"],["O-O","d6"],["Re1","Be7"],["c3","O-O"]]):
            print("I recommend 7. d4, controlling the center")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nd4"],["Nxd4","exd4"],["O-O","c6"],["Bc4","Nf6"]]):
            print("I recommend 7. Re1, supporting the e-pawn and planning e5 while also giving a nice f1 escape square for your bishop")
        #Scotch lines
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Bc5"],["Be3","d6"],["Nxc6","bxc6"]]):
            print("I recommend 7. Bxc5. tripling the black pawns and preparing to trade queens")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","d6"],["Nc3","Nf6"],["Bb5","Bd7"]]):
            print("I recommend 7. Nxc6 doubling black's pawns")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Bc5"],["Be3","Bxd4"],["Bxd4","Nf6"]]):
            print("I recommend 7. Nc3, protecting the e-pawn.")
        #Philidor Lines
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"],["Nxd4","Nf6"],["Nc3","Be7"],["Bf4","O-O"]]):
            print("I recommend 7. Bc4, developping your bishop to likely its best square and preparing to castle.")
        #French lines
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","Nc6"],["Nf3","Qb6"],["a3","a5"]]):
            print("I recommend 7. a4, massive brain creating an outpost on b5.")
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","Nc6"],["Nf3","Qb6"],["a3","Nh6"]]):
            print("I recommend 7. b4, taking space and relieving the pressure on white's d-pawn.")
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","Nc6"],["Nf3","Nge7"],["Bd3","cxd4"]]):
            print("I recommend 7. cxd4, keeping the center intact.")
        #Sicilian lines
        #Alapin Lines
        elif(moves == [["e4","c5"],["c3","d5"],["exd5","Qxd5"],["d4","cxd4"],["cxd4","Nc6"],["Nf3","Bg4"]]):
            print("I recommend 7. Nc3, attacking the black queen with danger levels and being ready to take Nxd5 if Bxf3 and forking the king")
        elif(moves == [["e4","c5"],["c3","d6"],["d4","cxd4"],["cxd4","a6"],["Nc3","g6"],["Bc4","Bg7"]]):
            print("I recommend 7. O-O. Ng5 is defendable. I write this after having failed an attack from this position based on a Ng5 Qf3 attack. Just castle.")
        elif(moves == [["e4","c5"],["c3","Nc6"],["d4","e6"],["Nf3","Nf6"],["e5","Nd5"],["c4","Ndb4"]]):
            print("I recommend 7. dxc5, that pawn is poisoned. If black takes with Bxc5, white plays a3, forcing Na6 then b4 and white wins a piece for two pawns. Be very careful in that position, because white is heavily underdeveloped and exposed, and black can wreak havoc on the queenside if white isn't careful.")
        elif(moves == [["e4","c5"],["c3","Nf6"],["e5","Nd5"],["d4","cxd4"],["Nf3","e6"],["cxd4","d6"]]):
            print("I recommend 7. Bc4, developing and attacking white's central knight. The idea behind this is after dxe5 dxe5, black can't defend his knight, and so you end up isolating his queen's pawn for free. Not a very good engine line, but I feel that for <2000 players isolated queen's pawns are generally a strategic weakness rather than a strength.")
        #Grand Prix Lines
        elif(moves == [["e4","c5"],["Nc3","Nc6"],["f4","a6"],["Bc4","e6"],["a3","b5"],["Ba2","Bb7"]]):
            print("I recommend 7. Nf3, developing the knight to its best square. You need not fear c4 because d3 is very strong. Taking is bad for black and defending the pawn is a tad difficult.")
        #Caro-Kann lines
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"],["g4","Bg6"],["Nge2","c5"]]):
            print("I recommend 7. h4, threatening the bishop.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",7)
    if(black):
        #Caro-Kann lines
        if(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Bd3","Qxd4"],["Nf3","Qd1"],["O-O"]]):
            print("I recommend 7... Bxe4, simplifying. Black's bishop can only be a target here")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4","h5"],["Nf3","e6"],["Nbd2","c5"],["Be2"]]):
            print("I recommend 7... Nc6, developing the knight to its ideal square.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Ng3","Bg6"],["Nf3","e6"],["Bd3"]]):
            print("I recommend 7... Nf3. Trading bishops is bad for white here because it opens up a file for the h-rook, and black can still castle long.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nf3","e6"],["Bd3","Ne7"],["O-O","Ne7"],["Bg5"]]):
            print("I recommend 7... Qb6, gaining a tempo on the b-pawn. Remember not to take the b-pawn instead of taking back a minor piece, for example Bxf5/e7 Qxb2 sucks for black")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Ng3","Bg6"],["N1e2","e6"],["Nf4"]]):
            print("I recommend 7... Ne7, preparing to recapture the bishop.")
        elif(moves == [["e4","c6"],["c3","d5"],["e5","Bf5"],["d4","e6"],["Nf3","Ne7"],["Be2","Ng6"],["O-O"]]):
            print("I recommend 7... Be7, continuing development and preparing to castle")
        elif(moves == [["e4","c6"],["Nf3","d5"],["e5","Bf5"],["d4","e6"],["Bd3","Bxd3"],["Qxd3"]]):
            print("I recommend 7... Nd7. This puts both knights into solid positions, from where you can transition to Ng6 c5 ideas.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nf3","e6"],["Bf5","Qb6"],["Nbd2","Qxb2"],["Rb1"]]):
            print("I recommend 7... Qxc2, taking another free pawn. Qxa2 is also good, DO NOT PLAY Bxc2, I made that mistake, you just lose a bishop after Rxb2 Bxd1 Kxd1")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["f4","e6"],["Nf3","c5"],["c3","Nc6"],["Be2"]]):
            print("I recommend 7... Qb6, attacking the queenside.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Bd3","Qxd4"],["Nf3","Qd1"],["Nc5"]]):
            print("I recommend 7... Qa5+, winning an easy knight with an easy fork, and protecting the bishop too.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"],["Nf3","Bd3"],["Bxd3","cxd3"]]):
            print("I recommend 7... cxd4")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4","h5"],["Bd3","Bxd3"],["Qxd3","e6"],["Bg5"]]):
            print("I recommend 7... Qb6, gaining a tempo on the b2 pawn.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3","e5"],["Nf3","e4"],["Nd4","Nc6"],["Nb5"]]):
            print("I recommend 7... Nf6, protecting the e4 and d5 squares. This is a trap. If white does a normal, passing move, such as O-O, black pulls up with a3, forcing N5c3 to stay in the center, leading to d4 and Ne2, giving black an incredibly strong position and leaving white with a knight that was moved 5 times only to come back to a mediocre square. Enormous flex moment.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["Bb3","dxe4"],["Qh5","g6"],["Qe5","Nf6"],["Nc3","Qd6"],["Qg5"]]):
            print("I recommend 7... Bf5, the only reasonable way for your bishop to be dislodged is with h6 g5, even then you can reply with Be6 and make white waste mad timeage.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["f4","e6"],["Nc3","c5"],["Bb5+","Nc6"],["Nf3"]]):
            print("I recommend 7... a6, because some people don't realize that Ba4 is completely losing for white after b5 and c6 wins a piece for pawn for black.")
        elif(moves == [["e4","c6"],["f4","d5"],["e5","Bf5"],["Nf3","e6"],["d5","c5"],["c3","Nc6"],["Bb5"]]):
            print("I recommend 7... Qb6, attacking the bishop and the d-pawn.")
        #queen's pawn opening lines
        elif(moves == [["d4","d5"],["Nf3","Nf6"],["c4","c6"],["Bg5","dxc4"],["Bxf6","exf6"],["e4","b5"],["a4"]]):
            print("I recommend 7... Bb4+, forcing the knight to pin itself and not attack the queenside pawns.")
        elif(moves == [["d4","d5"],["c4","c6"],["e3","Bf5"],["Nc3","e6"],["cxd5","exd5"],["Qb3","Qb6"],["Qxb6"]]):
            print("I recommend 7... axb6, duh.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",7)

#Move 8
if(in_database):
    if(white):
        #Spanish lines
        if(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","d6"],["O-O","a6"],["Ba4","b5"],["Bb3","Bb7"],["c3","Na5"]]):
            print("I recommend 8. Bc2, protecting the bishop.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Bc5"],["O-O","a6"],["Bxc6","dxc6"],["Nxe5","Qf6"],["d4","Bb6"]]):
            print("I recommend 8. c3, computer move and also very safe, keeping your extra pawn afvantage.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","b5"],["Bb3","Be7"],["O-O","Nf6"],["Re1","O-O"]]):
            print("I recommend 8. c3, preparing d4.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","Nf6"],["O-O","b5"],["Bb3","d6"],["Re1","Be7"]]):
            print("I recommend 8. c3, preparing d4.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nf6"],["O-O","d6"],["Re1","Be7"],["c3","O-O"],["d4","exd4"]]):
            print("I recommend 8. cxd4, controlling the center with the ideal pawn structure")
        #Scotch lines
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Bc5"],["Be3","d6"],["Nxc6","bxc6"],["Bxc5","dxc5"]]):
            print("I recommend 8. Qxd8, stopping black from castling")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Bc5"],["Be3","Bxd4"],["Bxd4","Nf6"],["Nc3","O-O"]]):
            print("I recommend 8. Be3, protecting the bishop pair.")
        #Philidor Lines
        elif(moves == [["e4","e5"],["Nf3","d6"],["d4","exd4"],["Nxd4","Nf6"],["Nc3","Be7"],["Bf4","O-O"],["Bc4","Nxe4"]]):
            print("I recommend 8. Nxe4, you can take and play Nb5 in response to d5 which wins a rook.")
        #French lines
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","Nc6"],["Nf3","Qb6"],["a3","a5"],["a4","c4"]]):
            print("I recommend 8. Na3, THREATENING to enter the outpost. Maybe hold off on actually doing it until it's safe.")
        elif(moves == [["e4","e6"],["d4","d5"],["e5","c5"],["c3","Nc6"],["Nf3","Nge7"],["Bd3","cxd4"],["cxd4","Bd7"]]):
            print("I recommend 8. Nc3, developing the knight to its best square.")
        #Sicilian lines
        elif(moves == [["e4","c5"],["c3","d5"],["exd5","Qxd5"],["d4","cxd4"],["cxd4","Nc6"],["Nf3","Bg4"],["Nc3","Qe6+"]]):
            print("I recommend 8. Be3, protecting the e-pawn, stopping the check, and threatening a d5 fork")
        elif(moves == [["e4","c5"],["c3","Nf6"],["e5","Nd5"],["d4","cxd4"],["Nf3","e6"],["cxd4","d6"],["Bc4","Nb6"]]):
            print("I recommend 8. Bd3, bringing the bishop back to a good square and protecting the queen.")
        #Caro-Kann lines
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"],["g4","Bg6"],["Nge2","c5"],["h4","h5"]]):
            print("I recommend 8. Nf4, threatening the bishop and the pawn.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",8)
    if(black):
        #Caro-kann lines
        if(moves == [["e4","c6"],["c3","d5"],["e5","Bf5"],["d4","e6"],["Nf3","Ne7"],["Be2","Ng6"],["O-O","Be7"],["h3"]]):
            print("I recommend 8... O-O, because not much is going on in this position so you can castle pretty easy")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["f4","e6"],["Nf3","c5"],["c3","Nc6"],["Be2","Qb6"],["O-O"]]):
            print("I recommend 8... cxd4, getting ready to attack the d-pawn and open the center to get a passed pawn.")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Ng3","Bg6"],["N1e2","e6"],["Nf4","Ne7"],["Nxg6"]]):
            print("I recommend 8... Nxg6, preserving the pawn structure.")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"],["Nf3","Bd3"],["Bxd3","cxd3"],["cxd4","Nxd4"]]):
            print("I recommend 8... Ne7, preparing to bring the knight out to g6 where both knights can attack white's weak e-pawn")
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["h4","h5"],["Bd3","Bxd3"],["Qxd3","e6"],["Bg5","Qb6"],["Nd2"]]):
            print("I recommend 8... c5, because you can. Pressure the center and give the c6 square to your knight.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3","e5"],["Nf3","e4"],["Nd4","Nc6"],["Nb5","Nf6"],["N5c3"]]):
            print("I recommend 8... d4, forcing Ne2.")
        #queen's pawn opening lines
        elif(moves == [["d4","d5"],["Nf3","Nf6"],["c4","c6"],["Bg5","dxc4"],["Bxf6","exf6"],["e4","b5"],["a4","Bb4+"],["Nbd2"]]):
            print("I recommend 8... Bg4, ready to trade g-bishop for f-knight to solidify the black dark square bishop's dominance of the queenside.")
        elif(moves == [["d4","d5"],["c4","c6"],["e3","Bf5"],["Nc3","e6"],["cxd5","exd5"],["Qb3","Qb6"],["Qxb6","axb6"],["Nf3"]]):
            print("I recommend 8... Nd7, computer move.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",8)

#Move 9
if(in_database):
    if(white):
        #Spanish lines
        if(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","d6"],["O-O","a6"],["Ba4","b5"],["Bb3","Bb7"],["c3","Na5"],["Bc2","Nf6"]]):
            print("I recommend 9. Re1, although a4 is a fantastic pawn break to open the position.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","b5"],["Bb3","Be7"],["O-O","Nf6"],["Re1","O-O"],["c3","d6"]]):
            print("I recommend 9. d4, taking control of the center.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","Nf6"],["O-O","b5"],["Bb3","d6"],["Re1","Be7"],["c3","O-O"]]):
            print("I recommend 9. h3, preventing Bg4.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","Nf6"],["O-O","d6"],["Re1","Be7"],["c3","O-O"],["d4","exd4"],["cxd4","Bg4"]]):
            print("I recommend 9. Nf3, responding to Bxf3 with gxf3 not Qxf3 because that loses a pawn. Big Dawg Stockfish says white is better, even with the messed up structure.")
        #Sicilian lines
        elif(moves == [["e4","c5"],["c3","d5"],["exd5","Qxd5"],["d4","cxd4"],["cxd4","Nc6"],["Nf3","Bg4"],["Nc3","Qe6+"],["Be3","Nb4"]]):
            print("I recommend 9. Qa4+, winning, because the only way black can save his knight is by moving it back where it will be forked ")
        #Scotch lines
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["d4","exd4"],["Nxd4","Bc5"],["Be3","d6"],["Nxc6","bxc6"],["Bxc5","dxc5"],["Qxd8","Kxd8"]]):
            print("I recommend 9. Nc3, preparing to castle queenside and attack the tripled pawns")
        #Caro-Kann lines
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"],["g4","Bg6"],["Nge2","c5"],["h4","h5"],["Nf4","Nc6"]]):
            print("I recommend 9. Nxg6, weakening the black king.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",9)
    if(black):
        #Caro-kann lines
        if(moves == [["e4","c6"],["c3","d5"],["e5","Bf5"],["d4","e6"],["Nf3","Ne7"],["Be2","Ng6"],["O-O","Be7"],["h3","O-O"],["c4"]]):
            print("I recommend 9... Nd7, preparing for an eventual Nb6")
        elif(moves == [["e4","c6"],["d4","d5"],["Nc3","dxe4"],["Nxe4","Bf5"],["Ng3","Bg6"],["N1e2","e6"],["Nf4","Ne7"],["Nxg6","Nxg6"],["Be3"]]):
            print("I recommend 9... Nd7, computer move.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3","e5"],["Nf3","e4"],["Nd4","Nc6"],["Nb5","Nf6"]]):
            print("I recommend 6... Nf6, this is a trap. If white does a normal, passing move, such as O-O, black pulls up with a3, forcing N5c3 to stay in the center, leading to d4 and Ne2, giving black an incredibly strong position and leaving white with a knight that was moved 5 times only to come back to a mediocre square. Enormous flex moment.")
        elif(moves == [["e4","c6"],["Bc4","d5"],["exd5","cxd5"],["Bb3","e5"],["Nf3","e4"],["Nd4","Nc6"],["Nb5","Nf6"],["N5c3","d4"],["Ne2"]]):
            print("I recommend 9... d3, the idea is that if white exchanges pawns black plays Qe7+, forcing Kf1 and stopping white from castling. If white just plays Ng3 instead, then Bg4 f3 exf3 and Bh3, again stopping white from castling.")
        #queen's pawn opening lines
        elif(moves == [["d4","d5"],["Nf3","Nf6"],["c4","c6"],["Bg5","dxc4"],["Bxf6","exf6"],["e4","b5"],["a4","Bb4+"],["Nbd2","Bg4"],["axb5"]]):
            print("I recommend 9... Bxf3 first, then cxb5 after.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",9)

#Move 10
if(in_database):
    if(white):
        #Spanish lines
        if(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","d6"],["O-O","a6"],["Ba4","b5"],["Bb3","Bb7"],["c3","Na5"],["Bc2","Nf6"],["Re1","h6"]]):
            print("I recommend 10. d4, taking control of the center.")
        elif(moves == [["e4","e5"],["Nf3","Nc6"],["Bb5","a6"],["Ba4","b5"],["Bb3","Be7"],["O-O","Nf6"],["Re1","O-O"],["c3","d6"],["d4","Bg4"]]):
            print("I recommend 10. Be3, protecting the d-pawn. Black can't play Nxe4 because of Bd5, forking the knights.")
        #Caro-Kann lines
        elif(moves == [["e4","c6"],["d4","d5"],["e5","Bf5"],["Nc3","e6"],["g4","Bg6"],["Nge2","c5"],["h4","h5"],["Nf4","Nc6"],["Nxg6","fxg6"]]):
            print("I recommend 10. Ne2, looks like a very simple move, you protect the pawn. However, it's actually very tricky. For example black cannot play g5 because that loses a pawn after hxg5(now the black h-pawn is pinned to the rook). hxg4 destroys the black pawn structure and fails to Nf4, ripping everything apart. Best continuation for black is cxd4 Nxd4, after which the obvious Nxe5 loses to Qe2, taking advantage of black's terrible structure to attack the king.")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("white",10)
    if(black):
        if(moves == []):
            print("I recommend")
        else:
            print(out_of_database_message)
            in_database = False
    addmove("black",10)

print("\nThis is what we recorded of your game")
count = 0
while(count<len(moves)):
    if(len(moves[count]) == 2):
        print(str(count+1) + ". ",moves[count][0],moves[count][1])
    elif(len(moves[count]) == 1):
        print(str(count+1) + "... ",moves[count][0])
    count += 1