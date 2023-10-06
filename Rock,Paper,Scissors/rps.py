import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        print("opponent: " + computer)
        return "It's a tie"
    
    # r > s, s > p, p > r
    if is_win(user,computer):
        print("opponent: " + computer)
        return 'You Won!'
    
    #we did't put this line into if, because 
    #we'll have already returned tie or win situation
    print("opponent: " + computer)
    return 'You lost!'

def is_win(player,computer):
    # return true if player wins
    # r > s, s > p, p > r
    # '\' goes for new line
    if (player=='r' and computer == 's') \
        or (player=='s' and computer == 'p') \
        or (player=='p' and computer == 'r'):
        return True    
    
print(play())