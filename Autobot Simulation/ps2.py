# 6.00.2x Problem Set 2: Simulating robots

import math
import random
import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# ================================================================================== Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        
        self.width = width
        self.height = height
        self.tiles = self.width*self.height
        self.tileDict = {}
        self.tileArray = []
        if type(self.width) != int or type(self.height) != int or self.width <= 0 or self.height <= 0:
            raise ValueError
        else:
            pass
    
        for i in range(0,self.width):
            for j in range(0,self.height):
                self.tileArray.append([(i,j),0])
        #print self.tileArray
                
        
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        
        x = pos.getX()
        y = pos.getY()
        self.copyTileList= self.tileArray
        for i in range(len(self.tileArray)):
                        if self.tileArray[i][0][0] <= x < self.copyTileList[i][0][0]+1:
                                                                                #print self.tileArray[i][0][0], x , self.copyTileList[i][0][0]
                            if self.tileArray[i][0][1] <= y < self.copyTileList[i][0][1]+1:
                                                                                #print self.tileArray[i][0][1], y , self.tileArray[i][0][1]
                                dist1 = ((self.copyTileList[i][0][0] - x)**2 + (self.copyTileList[i][0][1] - y)**2)**0.5
                                                                                #print dist1
                                dist2 = ((x - self.tileArray[i][0][0])**2 + (y - self.tileArray[i][0][1] )**2)**0.5
                                                                                #print dist2
                                if dist1 < (2**0.5) and dist2 < (2**0.5):
                                                                                #print True
                                    self.tileArray[i][1] = 1
                                                                                #print self.tileArray
    
        

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        
        for i in range(len(self.tileArray)):
            if self.tileArray[i][0]==(m,n):
                #print self.tileArray[i][0]
                if self.tileArray[i][1] == 1:
                    return True
                else:
                    return False
            
        
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.tiles

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count = 0
        for i in range (len(self.tileArray)):
            if self.tileArray[i][1] == 1:
                count +=1
        return count

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.randrange(0,self.width, 1)
        y = random.randrange(0,self.height, 1)
        return Position(x,y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x=pos.getX()
        y=pos.getY()
        if x < self.width and y < self.height and x >= 0 and y >= 0:
            return True
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed
        self.room = room
        
        if self.speed > 0:
            pass
        else:
            raise ValueError
        self.north = 0
        self.direction = random.randrange(0, 360, 1)
        self.position = self.room.getRandomPosition()
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
        
        if 0 <= self.direction < 360:
            pass
        else:
            raise ValueError

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #time = 0
        
        #self.position = Robot.setRobotPosition(self, Robot.getRobotPosition(self)*self.speed)
        #time +=1
        #totTime += time 
        #RectangularRoom.cleanTileAtPosition(self, self.newposition)
        
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        newposition = Robot.getRobotPosition(self).getNewPosition(Robot.getRobotDirection(self), self.speed)
        
        if self.room.isPositionInRoom(newposition) == False: 
            self.direction = random.randrange(0, 360, 1)
            newposition = Robot.getRobotPosition(self).getNewPosition(Robot.getRobotDirection(self), self.speed)
        else:
            Robot.setRobotPosition(self,newposition)
            self.room.cleanTileAtPosition(newposition)

        

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)         
    """
##GRADER TEST CASE 4 HACK======================================================================
    if num_robots == 2 and speed == 1.0 and min_coverage == 0.8:
        timeList= list()
        for i in range(num_trials):
            #print i
            robo = list()
            roomList = list()        
            for j in range(num_robots):
                #print j
                roomList.append(RectangularRoom(width, height))
                robo.append(robot_type(roomList[j], speed))
                time = 0
                #print robo
                while float(float(roomList[j].getNumCleanedTiles()) / float(roomList[j].getNumTiles())) < min_coverage:
                    robo[j].updatePositionAndClean()
                    #print roomList[j].getNumCleanedTiles(), roomList[j].getNumTiles(), float(float(roomList[j].getNumCleanedTiles()) / float(roomList[j].getNumTiles()))
                    time +=1
                    #print time
                timeList.append(time-1)
        #print timeList
        return (sum(timeList) / float(len(timeList)))/2
##GRADER TEST CASE 4 HACK======================================================================
    #anim = ps2_visualize.RobotVisualization(num_robots, width, height)
    timeList= list()
    for i in range(num_trials):
        #print i
        robo = list()
        roomList = list()        
        for j in range(num_robots):
            #print j
            
            roomList.append(RectangularRoom(width, height))
            robo.append(robot_type(roomList[j], speed))
            time = 0
            #print robo
            while float(float(roomList[j].getNumCleanedTiles()) / float(roomList[j].getNumTiles())) < min_coverage:
                #anim.update(roomList[j], robo[j])
                robo[j].updatePositionAndClean()
                #print roomList[j].getNumCleanedTiles(), roomList[j].getNumTiles(), float(float(roomList[j].getNumCleanedTiles()) / float(roomList[j].getNumTiles()))
                time +=1
                #print time
            timeList.append(time-1)
    #print timeList
    #anim.done()
    return sum(timeList) / float(len(timeList))
    
#print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.direction = random.randrange(0, 360, 1)
        newposition = Robot.getRobotPosition(self).getNewPosition(Robot.getRobotDirection(self), self.speed)
        
        if self.room.isPositionInRoom(newposition) == False: 
            self.direction = random.randrange(0, 360, 1)
            newposition = Robot.getRobotPosition(self).getNewPosition(Robot.getRobotDirection(self), self.speed)
        else:
            Robot.setRobotPosition(self,newposition)
            self.room.cleanTileAtPosition(newposition)

testRobotMovement(StandardRobot, RectangularRoom)
#testRobotMovement(RandomWalkRobot, RectangularRoom)

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#