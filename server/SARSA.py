import re, random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={'figure.figsize':(8,6)}, style="whitegrid")

###################################################################################
# file not used in app.py, but contains SARSA-logic, with a "for-loop", instead of Godot-connections (to get actions and rewards)
# contains also plotting stats. they are not yet in app.py

import env
# test change

# Rewards: when user is pushing buttons
REWARD_NEGATIVE = '-10'
REWARD_POSITIVE = '10'
REWARD_NEUTRAL = '0'


# actions: list of all possible actions.
# Mapping to screen-happens for now on godot side.
ACTION_1  = 'CircleRed'
ACTION_2 = 'CircleBlue'
ACTION_3  = 'CircleGreen'
ACTION_4  = 'SquareRed'
ACTION_5  = 'SquareBlue'
ACTION_6  = 'SquareGreen'


ACTIONS = (ACTION_1, ACTION_2, ACTION_3, ACTION_4, ACTION_5, ACTION_6 )


# collection of all possible states:
# state with k-order history, k=1: S_t= (R_t, A_t-1)
STATE_1   = ACTION_1+REWARD_NEGATIVE
STATE_2   = ACTION_1+REWARD_POSITIVE
STATE_3   = ACTION_1+REWARD_NEUTRAL

STATE_4   = ACTION_2+REWARD_NEGATIVE
STATE_5   = ACTION_2+REWARD_POSITIVE
STATE_6   = ACTION_2+REWARD_NEUTRAL

STATE_7   = ACTION_3+REWARD_NEGATIVE
STATE_8   = ACTION_3+REWARD_POSITIVE
STATE_9   = ACTION_3+REWARD_NEUTRAL

STATE_10   = ACTION_4+REWARD_NEGATIVE
STATE_11  = ACTION_4+REWARD_POSITIVE
STATE_12   = ACTION_4+REWARD_NEUTRAL

STATE_13   = ACTION_5+REWARD_NEGATIVE
STATE_14   = ACTION_5+REWARD_POSITIVE
STATE_15  = ACTION_5+REWARD_NEUTRAL

STATE_16   = ACTION_6+REWARD_NEGATIVE
STATE_17   = ACTION_6+REWARD_POSITIVE
STATE_18   = ACTION_6+REWARD_NEUTRAL

STATES = (STATE_1, STATE_2, STATE_3, STATE_4, STATE_5, STATE_6,
          STATE_7, STATE_8, STATE_9, STATE_10, STATE_11, STATE_12,
          STATE_13, STATE_14, STATE_15, STATE_16, STATE_17, STATE_18)



num_states = len(STATES)
num_actions = len(ACTIONS)

print("all states: ", STATES)
print("all actions: ", ACTIONS)

print("num_states: ", num_states)
print("num_actions: ", num_actions)


#definitions, used in algo SARSA

# def choose action:
def choose_action(Q, state, epsilon, ACTIONS):
    q_vals = Q.get(state)  # returns 'None' if missing (new state)
    unexplored_state = q_vals is None
    epsilon_chance = np.random.uniform(0.0, 1.0) < epsilon
    #print("ACTIONS: ", ACTIONS)
    if unexplored_state or epsilon_chance:
        #print("ACTIONS: ", ACTIONS)
        random_action = random.sample(ACTIONS, 1) # random policy.  #type(random_action): list
        for i in random_action:
            action = i # list to string
            print("action selection with epsilon-chance or unexplored state")
    else:
        # suche ACTION mit höchstem q_vals für gegebenen state
        action = max(q_vals, key=lambda key: q_vals[key])  # acting greedy
        print("action selection with greedy to q")
    return action

# def update q:
def update_Q(Q, state, action, reward, next_state, next_action, num_actions, alpha, gamma):
    if Q.get(state) is None:
        # Innitialzing per-action Q-values array for current (unexplored) state
        Q[state] = dict(zip(ACTIONS, np.zeros(num_actions)))  # we create a nested dictionary. initialize values to zero.

    # Compute expected future reward Q(S', A')
    if Q.get(next_state) is None:
        Q[next_state] = dict(zip(ACTIONS, np.zeros(num_actions)))
        next_q = 0  # Q(S',A')= 0 if not existant
    else:
        next_q = Q[next_state][next_action] # Q(S',A')

    # Update Q-value
    q_update = int(reward) + gamma * next_q
    print("state: ,", state, ", action: ", action ,", Q[state][action] before update: ", Q[state][action])
    Q[state][action] = (1 - alpha) * Q[state][action] + alpha * q_update
    print("Q[state][action] after update: ", Q[state][action])
##################################################################################################################

# plotting statistics
stats = {
        'rewards'      : [],
        'cumulativ_reward' : []
}

total_reward = 0

##################################################################################################################



#Algorithm 1 : SARSA for estimating q = q*
#with the help of assignment 12, Machine LEarning lecture.
#line 1: Algo parameters.
gamma = 0.9
alpha = 0.6
epsilon = 0.1
#not used for the moment:
epsilon_min = 0.1 #new. start high epsilon, then decay over time.
epsilon_decay = 0.9 #new. start high epsilon, then decay over time.

# line 2: initialize q(s,a) for all s, a arbitrarily.
# --> we do it differently. see in def update_Q: Q[state] = dict(zip(ACTIONS, np.zeros(num_actions)))
Q = {} # hashing states to per-action reward arrays


#line 3 : we do not loop through episodes. only one episode.
#line 4: Initialize S
state = STATE_3  # erster schritt stimmt deshalb nicht ganz. wird sich aber anpassen mit iterationen.
                # STATE_3 = 'CircleRed0'
#line 5: choose A from S using e-greedy policy derived from Q.
action = ACTION_1 #ACTION_1  = 'CircleRed', # empty Q for now. choose random (action 1)
print("first action: ", action)

#line 6: loop for each step of episode:
max_nsteps = 100 #maximum of steps. end-version: high number.
for t in range(max_nsteps):
    #for epsilon decay:
    #epsilon *= epsilon_decay
    #epsilon = max(epsilon_min, epsilon)
    #print("time step t: ", t, ", epsilon: ", epsilon)

    #line 7: Take action A, observe R, S': --> GODOT !!
    #   send "action" to godot. --> action defines next screen. godot displays screen. python waits for reward R
    #   wait for user feedback R.
    reward = REWARD_POSITIVE # zum testen hier  fixer reward
    print("time step t: ", t, " reward for action t: ", reward)

    # Accumulate reward.
    total_reward += int(reward)

    next_state = action+reward # S' = next_state
    print("time step t: ", t, " next_state: ", next_state)

    #line 8: choose A' from S' using e-greedy policy derived from Q
    next_action = choose_action(Q, next_state, epsilon, ACTIONS)
    print("time step t: ", t, " next_action: ", action)

    #line 9: q-update mit sarsa.
    update_Q(Q, state, action, reward, next_state, next_action, num_actions, alpha, gamma)
    print("Q after update: ", Q)


    #line 10: S <-- S', A <-- A'
    state = next_state
    action = next_action

    #record epsiode statistics
    stats['rewards'].append(reward)
    stats['cumulativ_reward'].append(total_reward)



# Plottings
#plt.title("rewards per time step")
#sns.lineplot(x=range(len(stats['rewards'])), y=stats['rewards'])
#plt.figure()
#plt.show()

#plt.title("cumulativ reward")
#sns.lineplot(x=range(len(stats['cumulativ_reward'])), y=stats['cumulativ_reward'])
#plt.figure()
#plt.show()

#fig, (ax1, ax2) = plt.subplots(1, 2)
#fig.suptitle('Horizontally stacked subplots')
#ax1.plot(x=range(len(stats['rewards'])), y=stats['rewards'])
#ax2.plot(x=range(len(stats['cumulativ_reward'])), y=stats['cumulativ_reward'])
