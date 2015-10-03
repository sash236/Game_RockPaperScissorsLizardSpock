import simplegui
import random

message1 = "  Rock Paper Scissors Lizard Spock"

scorePlayer = 0
scoreCPU = 0
message_choiceU = ""
message_choiceC = ""
win_statement = ""

def number_to_name(number):
    
    name = 'Error' # assign a string that is not one of the name
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'    
    elif number ==  3:
        name = 'lizard'
    elif number ==  4:
        name = 'scissors'
    else:
        print "%s: 'number' is not in the correct range. Valid range is from 0 to 4" %name			
    
    return name
    
def name_to_number(name):

    number = -1  # assign a value outside the range
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number =  2   
    elif name ==  'lizard':
        number = 3
    elif name ==  'scissors':
        number = 4
    else:
        print ("Error: 'name' does not match any of the five correct input strings")
    
    return number

def rpsls(player_number): 
    global message_choiceU, message_choiceC, scorePlayer, scoreCPU, win_statement  
    comp_name = '' # the name chosen by computer random # generator

    if scorePlayer >= 10 or scoreCPU >= 10:
        restart()    
    
    diff = 0
    
    player_name = number_to_name(player_number)
    comp_number = random.randrange(0,5)
    comp_name = number_to_name(comp_number)
    
    message_choiceU = "Player chooses " + player_name + "."
    message_choiceC = "Computer chooses " + comp_name + "."	
    
    diff = (player_number - comp_number) % 5

    if player_number == -1:
        win_statement = 'Player chose a name that is not one of the five correct input strings'        
    elif diff <= 2 and diff > 0:
        win_statement = 'Player wins!'
        scorePlayer+=1
    elif diff > 2 and diff < 5:
        win_statement = 'Computer wins!'
        scoreCPU+=1
    elif diff == 0:
        win_statement = 'Player and computer tie!'

    comp_name = number_to_name(comp_number)


def rock():
    choice_player = 0
    rpsls(choice_player)
    
def paper():
    choice_player = 2
    rpsls(choice_player)
    
def scissors():
    choice_player = 4
    rpsls(choice_player)

def lizard():
    choice_player = 3
    rpsls(choice_player)
    
def spock():
    choice_player = 1
    rpsls(choice_player)

def restart():
    global message1, scorePlayer, scoreCPU, message_choiceU, message_choiceC, win_statement
    message1 = "  Rock Paper Scissors Lizard Spock"
    
    scorePlayer = 0
    scoreCPU = 0
    message_choiceC = ""
    message_choiceU = ""
    win_statement = ""

def draw(canvas):
    canvas.draw_text(message1, [5,30], 20, "White")
    canvas.draw_text("Your score: " + str(scorePlayer), [5,295], 20, "Red")
    canvas.draw_text("Computer's score: " + str(scoreCPU), [175,295], 20, "Blue")
    canvas.draw_text(message_choiceU, [50,100], 20, "White")
    canvas.draw_text(message_choiceC, [50,125], 20, "White")
    canvas.draw_text(win_statement, [50,150], 20, "White")
    
    if scorePlayer >= 10:
        canvas.draw_text("You Won ! ", [90,250], 30, "Red")
    elif scoreCPU >= 10:
        canvas.draw_text("Computer Won ! ", [90,250], 30, "Blue")
                
    
f = simplegui.create_frame("Rock Paper Scissors Lizard Spock", 350, 300)

f.add_button("Rock", rock, 80)
f.add_button("Paper", paper, 80)
f.add_button("Scissors", scissors, 80)
f.add_button("Lizard", lizard, 80)
f.add_button("Spock", spock, 80)

f.add_label('')
f.add_button("Restart", restart, 80)


f.set_draw_handler(draw)

f.start()
    




