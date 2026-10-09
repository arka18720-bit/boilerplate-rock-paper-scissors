# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opp_history=[],pattern={}):
    if prev_play=="":
        opp_history.clear()
        pattern.clear()
        guess = "R"
    else:

        opp_history.append(prev_play)
        cur_pattern=opp_history[-4:]
        new_pattern="".join(cur_pattern)

        if len(opp_history)>4:
            if new_pattern in pattern:
                pattern[new_pattern]+=1
            else:
                pattern[new_pattern]=1
                

        guess_paper = new_pattern[-3:] + "P"
        score_paper = pattern.get(guess_paper,0)

        guess_rock = new_pattern[-3:] + "R"
        score_rock = pattern.get(guess_rock,0)

        guess_scissor = new_pattern[-3:] + "S"
        score_scissor = pattern.get(guess_scissor,0)

        max_score = max(score_paper,score_rock,score_scissor)
        
        if score_paper == max_score :
            guess = "S"
        elif score_rock == max_score:
            guess = "P"
        else:
            guess = "R"
    

    return guess
