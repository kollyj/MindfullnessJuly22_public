from flask import Flask, request, Response
import numpy as np
import json
import env

#gitchange test

app = Flask(__name__) # creates a new Flask instance


# globals
next_state = None
next_action = None
ACTIONS = env.ACTIONS
num_actions = env.num_actions

#Algorithm 1 : SARSA for estimating q = q*
#line 1: Algo parameters.
gamma = 0.9
alpha = 0.6
epsilon = 0.1
#not used for now:
epsilon_min = 0.1 #new. start high epsilon, then decay over time.
epsilon_decay = 0.9 #new. start high epsilon, then decay over time.

# line 2: initialize q(s,a) for all s, a arbitrarily.
# --> we do it differently. see in def update_Q: Q[state] = dict(zip(ACTIONS, np.zeros(num_actions)))
Q = {} # hashing states to per-action reward arrays


#line 3 : we do not loop through episodes. only one episode.
#line 4: Initialize S
state = env.STATE_3  # erster schritt stimmt deshalb nicht ganz. wird sich aber anpassen mit iterationen.
                     # STATE_3 = 'CircleRed0'
#line 5: choose A from S using e-greedy policy derived from Q.
action = env.ACTION_1 #ACTION_1  = 'CircleRed', # empty Q for now. choose random (action 1)


#line 7: Take action A, observe R, S': --> GODOT !!

#taking action A: already on GODOT Screen (CircleRed).
#observve reward R: user feedback. depends on event "buttonClick".

    #if R = positive reward:
@app.route('/positiveReward', methods=['POST'])
def positiveReward():
    print(" this is the request.json that comes from Godot, by pushing button: ", request.json) # prints it in python console
    global state
    global action
    global next_state
    global epsilon
    global ACTIONS
    global next_action
    global Q
    global num_actions
    reward = str(request.json)
    next_state = action + reward  # S' = next_state

    # line 8: choose A' from S' using e-greedy policy derived from Q
    next_action = env.choose_action(Q, next_state, epsilon, ACTIONS)

    # line 9: q-update mit sarsa.
    print("Q_old: ", Q)
    env.update_Q(Q, state, action, reward, next_state, next_action, num_actions, alpha, gamma)
    print("Q_new: ", Q)
    # line 10: S <-- S', A <-- A'
    state = next_state
    action = next_action

    return json.dumps(action) # will get printed in godot console. must be the new action.
    #return 'CircleRed'




    #if R = negative reward:
@app.route('/negativeReward', methods=['POST'])
def negativeReward():
    print(" this is the request.json that comes from Godot, by pushing button: ", request.json) # prints it in python console
    global state
    global action
    global next_state
    global epsilon
    global ACTIONS
    global next_action
    global Q
    global num_actions
    reward = str(request.json)
    next_state = action + reward  # S' = next_state

    # line 8: choose A' from S' using e-greedy policy derived from Q
    next_action = env.choose_action(Q, next_state, epsilon, ACTIONS)

    # line 9: q-update mit sarsa.
    print("Q_old: ", Q)
    env.update_Q(Q, state, action, reward, next_state, next_action, num_actions, alpha, gamma)
    print("Q_new: ", Q)
    # line 10: S <-- S', A <-- A'
    state = next_state
    action = next_action

    return json.dumps(action) # will get printed in godot console. must be the new action.




    #if R = negative reward:
@app.route('/neutralReward', methods=['POST'])
def neutralReward():
    print(" this is the request.json that comes from Godot, by pushing button: ", request.json) # prints it in python console
    global state
    global action
    global next_state
    global epsilon
    global ACTIONS
    global next_action
    global Q
    global num_actions
    reward = str(request.json)
    next_state = action + reward  # S' = next_state

    # line 8: choose A' from S' using e-greedy policy derived from Q
    next_action = env.choose_action(Q, next_state, epsilon, ACTIONS)

    # line 9: q-update mit sarsa.
    print("Q_old: ", Q)
    env.update_Q(Q, state, action, reward, next_state, next_action, num_actions, alpha, gamma)
    print("Q_new: ", Q)
    # line 10: S <-- S', A <-- A'
    state = next_state
    action = next_action

    return json.dumps(action) # will get printed in godot console. must be the new action.





if __name__ == '__main__': # checks if this is main
    app.run(debug=True) # runs the server (on a specific API, see output). with debug=True: automatically re-runs app when saving changes.