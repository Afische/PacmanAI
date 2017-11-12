# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discountRate = 0.9, iters = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.

      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discountRate = discountRate
    self.iters = iters
    self.values = util.Counter() # A Counter is a dict with default 0

    # values are numbers in squares | getValue(state) returns the value of a state
    # q-values are numbers in square quarters | getQValue(state, action) returns the q-value of the (state, action) pair
    # policies are arrows out from each square | getPolicy(state) returns the best action according to computed values

    """
    Iterates through the grid x times. Iterates through states while they are
    available. For each possible action at a state, get all possible Qvalues. 
    Set value = smallest action value. Store results in actionValues array. 
    Once it has gone through all the states for an iteration, save the 
    results in self.values. These are the final actions.
    """
    "YOUR CODE HERE"

    for x in range(self.iters):
        actionValues = self.values.copy()
        for state in self.mdp.getStates():
            possibleActions = self.mdp.getPossibleActions(state)
            value = None
            for action in possibleActions:
                currentValue = self.getQValue(state, action)
                if value < currentValue:
                    value = currentValue
            if value == None:
                value = 0
            actionValues[state] = value
        self.values = actionValues

    "END CODE"

  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]

  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes). Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    """
    Determine value for a state/action tuple. I use discount
    and reward calculations to find the qValue.
    """
    " YOUR CODE HERE "
    transitionStatesAndProbs = self.mdp.getTransitionStatesAndProbs(state, action)
    qvalue = 0
    for newState, probability in transitionStatesAndProbs:
		    discount = self.discountRate * self.values[newState]
		    reward = self.mdp.getReward(state, action, newState)
		    qvalue += probability * (reward + discount)

    return qvalue
    " END CODE "

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit. Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """

    """
    Perform a check to find the best possible action in a state. 
    For all actions in a state, return the action with the 
    greatest value.
    """
    " YOUR CODE HERE "

    possibleActions = self.mdp.getPossibleActions(state)

    if (len(possibleActions) == 0):
        return None

    value = None
    policy = None
    for action in possibleActions:
    	 check = self.getQValue(state, action)
    	 if value < check:
    		  value = check
    		  policy = action

    return policy

    "END CODE" 

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
