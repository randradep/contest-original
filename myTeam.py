# myTeam.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
#type a coment or something 

from captureAgents import CaptureAgent
import random, time, util
from game import Directions
import game

#################
# Team creation #
#################

def createTeam(firstIndex, secondIndex, isRed,
               first = 'InterceptAgent', second = 'InterceptAgent'):
  """
  This function should return a list of two agents that will form the
  team, initialized using firstIndex and secondIndex as their agent
  index numbers.  isRed is True if the red team is being created, and
  will be False if the blue team is being created.

  As a potentially helpful development aid, this function can take
  additional string-valued keyword arguments ("first" and "second" are
  such arguments in the case of this function), which will come from
  the --redOpts and --blueOpts command-line arguments to capture.py.
  For the nightly contest, however, your team will be created without
  any extra arguments, so you should make sure that the default
  behavior is what you want for the nightly contest.
  """

  # The following line is an example only; feel free to change it.
  return [eval(first)(firstIndex), eval(second)(secondIndex)]

##########
# Agents #
##########

class InterceptAgent(CaptureAgent):
  """
  A Dummy agent to serve as an example of the necessary agent structure.
  You should look at baselineTeam.py for more details about how to
  create an agent as this is the bare minimum.
  """

  def registerInitialState(self, gameState):
    """
    This method handles the initial setup of the
    agent to populate useful fields (such as what team
    we're on).

    A distanceCalculator instance caches the maze distances
    between each pair of positions, so your agents can use:
    self.distancer.getDistance(p1, p2)

    IMPORTANT: This method may run for at most 15 seconds.
    """

    '''
    Make sure you do not delete the following line. If you would like to
    use Manhattan distances instead of maze distances in order to save
    on initialization time, please take a look at
    CaptureAgent.registerInitialState in captureAgents.py.
    '''
    CaptureAgent.registerInitialState(self, gameState)

    '''
    Your initialization code goes here, if you need any.
    '''
    self.oponents = self.getOpponents(gameState)
    self.oponentsDistance = []
    self.position = None
    self.noisyDistances = None

  def getOponentsPositions(self, gameState):
    oponentsPositions = []
    for oponent in self.oponents:
      oponentPosition = gameState.getAgentState(oponent).getPosition()
      if not oponentPosition == None:
        oponentsPositions.append(oponentPosition)
      else:
        oponentsPositions.append(0)
    return oponentsPositions

  def chooseAction(self, gameState):
    """
    Picks among actions randomly.
    """
    MAX_HISTORY = 5
    actions = gameState.getLegalActions(self.index)

    '''
    You should change this in your own agent.
    '''
    #Variable declaration
    enemyDistances = []

    #Update position
    self.position = gameState.getAgentState(self.index).getPosition()

    self.noisyDistances = gameState.getAgentDistances()

    print self.noisyDistances

    for oponent in self.oponents:
      oponentPosition = self.getOponentsPositions(gameState)
      if oponentPosition != None:
        print oponentPosition
      #oponentDistance = self.distancer.getDistance(self.position, oponentPosition)
      #self.oponentsDistance.append(oponentDistance)

    #print self.oponentsDistance so far it is always blanck
    #self.distancer.getDistance(self.position, )

    return random.choice(actions)

#Trying ot write on branch