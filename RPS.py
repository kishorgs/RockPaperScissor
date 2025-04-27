import random

def player(prev_play, opponent_history=[]):
    if not opponent_history:
        opponent_history.clear()
    if prev_play:
        opponent_history.append(prev_play)
    
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    
    if not prev_play:
        return random.choice(["R", "P", "S"])
    
    if not hasattr(player, "own_history"):
        player.own_history = []
    if len(opponent_history) > 1:
        player.own_history.append(player.last_move)
    
    def identify_opponent():
        if len(opponent_history) < 5:
            return None
        
        quincy_sequence = ["R", "R", "P", "P", "S"]
        recent_moves = opponent_history[-5:] if len(opponent_history) >= 5 else opponent_history
        if recent_moves == quincy_sequence[:len(recent_moves)]:
            return "quincy"
        
        if len(player.own_history) >= 2:
            last_player_move = player.own_history[-2]
            opponent_response = opponent_history[-1]
            if opponent_response == counter_moves[last_player_move]:
                return "kris"
        
        if len(player.own_history) >= 10:
            last_ten = player.own_history[-10:]
            most_frequent = max(set(last_ten), key=last_ten.count)
            opponent_response = opponent_history[-1]
            if opponent_response == counter_moves[most_frequent]:
                return "mrugesh"
        
        return "abbey"
    
    def quincy_strategy():
        move_index = len(opponent_history) % 5
        quincy_moves = ["R", "R", "P", "P", "S"]
        quincy_next = quincy_moves[move_index]
        return counter_moves[quincy_next]
    
    def kris_strategy():
        last_move = player.own_history[-1] if player.own_history else "R"
        kris_counter = counter_moves[last_move]
        return counter_moves[kris_counter]
    
    def mrugesh_strategy():
        if len(player.own_history) < 10:
            return "R"  
        return "S"  
    
    def abbey_strategy():
        sequence = ["R", "P", "S"] 
        return sequence[len(opponent_history) % 3]
    
    opponent = identify_opponent()
    
    if opponent == "quincy":
        move = quincy_strategy()
    elif opponent == "kris":
        move = kris_strategy()
    elif opponent == "mrugesh":
        move = mrugesh_strategy()
    elif opponent == "abbey":
        move = abbey_strategy()
    else:
        move = random.choice(["R", "P", "S"])
    
    player.last_move = move
    return move