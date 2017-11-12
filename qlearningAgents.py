# qlearningAgents.py
# ------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
  """
    Q-Learning Agent

    Functions you should fill in:
      - getQValue
      - getAction
      - getValue
      - getPolicy
      - update

    Instance variables you have access to
      - self.epsilon (exploration prob)
      - self.alpha (learning rate)
      - self.discountRate (discount rate)

    Functions you should use
      - self.getLegalActions(state)
        which returns legal actions
        for a state
  """
  def __init__(self, **args):
    "You can initialize Q-values here..."
    ReinforcementAgent.__init__(self, **args)

    self.Qvalues = util.Counter()

  def getQValue(self, state, action):
    """
      Returns Q(state,action)
      Should return 0.0 if we never seen
      a state or (state,action) tuple
    """

    """ YOUR CODE HERE """
    return self.Qvalues[(state, action)]
    """ END CODE """



  def getValue(self, state):
    """
      Returns max_action Q(state,action)
      where the max is over legal actions.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return a value of 0.0.
    """
    """
    Get all Qvalues for a state and store into array.
    Return the max value of these values.
    """
    """ YOUR CODE HERE """

    actions = self.getLegalActions(state)

    if len(actions) == 0:
        return 0.0

    Qvalues = []
    for action in actions:
        Qvalues.append(self.getQValue(state, action))
    value = max(Qvalues)
    return value

    """ END CODE """

  def getPolicy(self, state):
    """
      Compute the best action to take in a state.  Note that if there
      are no legal actions, which is the case at the terminal state,
      you should return None.
    """
    """
    For actions in a state, find the greatest value of all the actions
    and save to possibleActions. If values are the same, then append 
    multiple values to possibleActions. Randomly choose between these
    actions.
    """
    """ YOUR CODE HERE """
    actions = self.getLegalActions(state)

    if (len(actions) == 0):
        return None

    value = None
    policy = None
    possibleActions = []
    maxVal = float("-inf")
    for action in actions:
        actionValue = self.getQValue(state, action)
        if actionValue == maxVal:
            possibleActions.append(action)
        elif actionValue > maxVal:
          maxVal = actionValue
          possibleActions = [action]
    return random.choice(possibleActions)
    """ END CODE """

  def getAction(self, state):
    """
      Compute the action to take in the current state.  With
      probability self.epsilon, we should take a random action and
      take the best policy action otherwise.  Note that if there are
      no legal actions, which is the case at the terminal state, you
      should choose None as the action.

      HINT: You might want to use util.flipCoin(prob)
      HINT: To pick randomly from a list, use random.choice(list)
    """
    # Pick Action
    actions = self.getLegalActions(state)
    action = None

    """
    If we flip a coin and get heads, randomly return an action. 
    Otherwise, determine action through getPolicy.
    """
    """ YOUR CODE HERE """
    if len(actions) == 0:
        return None

    if len(actions) > 0:
        if util.flipCoin(self.epsilon):
            action = random.choice(actions)
        else: 
            action = self.getPolicy(state)
        """ END CODE """

    return action

  def update(self, state, action, nextState, reward):
    """
      The parent class calls this to observe a
      state = action => nextState and reward transition.
      You should do your Q-Value update here

      NOTE: You should never call this function,
      it will be called on your behalf
    """
    """
    Update Qvalues by looking at nextState and implementing
    reward and update values. For reward, take nextState value combined
    with discount and added reward. Subtract frmo out QValue to see
    the difference for total reward. For update, multiply reward by alpha 
    to implement learning rate for this reward. We add this to Qvalue for 
    total update value.
    """
    """ YOUR CODE HERE """
    rewardVal = (reward + self.discountRate * self.getValue(nextState) - self.getQValue(state, action))
    updateVal = self.getQValue(state, action) + (self.alpha * rewardVal)
    self.Qvalues[(state, action)] = updateVal

    """ END CODE """

class PacmanQAgent(QLearningAgent):
  "Exactly the same as QLearningAgent, but with different default parameters"

  def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
    """
    These default parameters can be changed from the pacman.py command line.
    For example, to change the exploration rate, try:
        python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

    alpha    - learning rate
    epsilon  - exploration rate
    gamma    - discount factor
    numTraining - number of training episodes, i.e. no learning after these many episodes
    """
    args['epsilon'] = epsilon
    args['gamma'] = gamma
    args['alpha'] = alpha
    args['numTraining'] = numTraining
    self.index = 0  # This is always Pacman
    QLearningAgent.__init__(self, **args)

  def getAction(self, state):
    """
    Simply calls the getAction method of QLearningAgent and then
    informs parent of action for Pacman.  Do not change or remove this
    method.
    """
    action = QLearningAgent.getAction(self,state)
    self.doAction(state,action)
    return action


class ApproximateQAgent(PacmanQAgent):
  """
     ApproximateQLearningAgent

     You should only have to overwrite getQValue
     and update.  All other QLearningAgent functions
     should work as is.
  """
  def __init__(self, extractor='IdentityExtractor', **args):
    self.featExtractor = util.lookup(extractor, globals())()
    PacmanQAgent.__init__(self, **args)

    # You might want to initialize weights here.

  def getQValue(self, state, action):
    """
      Should return Q(state,action) = w * featureVector
      where * is the dotProduct operator
    """
    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    util.raiseNotDefined()
    """ END CODE """

  def update(self, state, action, nextState, reward):
    """
       Should update your weights based on transition
    """
    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    util.raiseNotDefined()
    """ END CODE """

  def final(self, state):
    "Called at the end of each game."
    # call the super-class final method
    PacmanQAgent.final(self, state)

    # did we finish training?
    if self.episodesSoFar == self.numTraining:
      # you might want to print your weights here for debugging
      util.raiseNotDefined()
