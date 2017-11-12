# analysis.py
# -----------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

######################
# ANALYSIS QUESTIONS #
######################

# Change these default values to obtain the specified policies through
# value iteration.

# High noise go to cliff/ more random choices
# low discount ignores future rewards, high discount makes later rewards more valuable
# High living reward goes away from cliff, low living reward makes exit faster 1.0

def question2():
  answerDiscount = 0.9
  answerNoise = 0.0
  """
  No noise to ensure we follow the safe route and don't go off astray
  """
 
  return answerDiscount, answerNoise

def question3a():
  answerDiscount = 0.2 
  answerNoise = 0.0
  answerLivingReward = 0.0 

  """
  Low discount ignores future reward of value 10.0
  No noise lowers chances of falling into cliff 
  No living reward makes player risk the cliff and choose closer exit
  """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3b():
  answerDiscount = 0.2
  answerNoise = 0.1
  answerLivingReward = -0.2
  """
  Low discount ignores future reward of value 10.0
  Low noise avoids changing route
  Negative living reward chooses closer exit, avoids cliff
  """

  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3c():
  answerDiscount = 0.9
  answerNoise = 0.0
  answerLivingReward = 0.2

  """
  High discount increases value of future reward value 1.0
  No noise lowers chances of falling into cliff
  Low living reward makes player prefer cliff route
  """

  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3d():
  answerDiscount = 0.9
  answerNoise = 0.2
  answerLivingReward = 0.0
  
  """
  High discount increases value of future reward value 1.0
  Low noise avoids changing route
  No living reward makes player not worry about the cliff and choose closer exit
  """

  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3e():
  answerDiscount = 0.9
  answerNoise = 0.2
  answerLivingReward = 0.0

  """
  Slow exit option, avoids cliff, prefers distant exit, 
  but has no reward and has noise
  """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question6():
  answerEpsilon = None
  answerLearningRate = None
  """
  Changed to NOT POSSIBLE since there is no tuple
  for learning the optimal policy after 50 iterations.
  """
  return 'NOT POSSIBLE'
  # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
  print 'Answers to analysis questions:'
  import analysis
  for q in [q for q in dir(analysis) if q.startswith('question')]:
    response = getattr(analysis, q)()
    print '  Question %s:\t%s' % (q, str(response))
