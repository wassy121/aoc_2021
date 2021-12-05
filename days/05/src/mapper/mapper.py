import itertools as it
import logging
import os
from pandas import *


class Mapper:
    file_name = 'src/resources/input.txt'
    vent_lines = []
    vent_map = [[0 for col in range(1000)] for row in range(1000)]

    @staticmethod
    def parseVentLine(line):
        command_set = line.split()
        assert len(command_set) == 3
        return [command_set[0],command_set[2]]

    def parseFile(self):
        with open(self.file_name) as input_file:
            self.vent_lines = [Mapper.parseVentLine(line) for line in input_file.readlines()]

    def fillVentMap(self):
        for vent_line in self.vent_lines:
            # point a = index 0, point b = index 1
            # a.x = 0,0 b.x = 1,0 a.y = 0,1 b.y = 1,1
            a_x = int(vent_line[0].split(',')[0])
            a_y = int(vent_line[0].split(',')[1])
            b_x = int(vent_line[1].split(',')[0])
            b_y = int(vent_line[1].split(',')[1])
            logging.debug("added line from {0},{1} to {2},{3}".format(a_x,a_y,b_x,b_y))
            if a_x == b_x:
                # loop over y
                orientation= -1 if a_y > b_y else 1
                for horiz_place in range(a_y,b_y+orientation,orientation):
                    #logging.debug("y loop added 1 to {0},{1}".format(a_x,horiz_place))
                    self.vent_map[a_x][horiz_place] += 1
            if a_y == b_y:
                # loop over x
                orientation= -1 if a_x > b_x else 1
                for vertical_place in range(a_x,b_x+orientation,orientation):
                    #logging.debug("x loop added 1 to {0},{1}".format(vertical_place,a_y))
                    self.vent_map[vertical_place][a_y] += 1
            if (abs(a_x-b_x) == abs(a_y-b_y)):
                y_orientation= -1 if a_y > b_y else 1
                x_orientation= -1 if a_x > b_x else 1
                for item in zip(range(a_x,b_x+x_orientation,x_orientation),range(a_y,b_y+y_orientation,y_orientation)):
                   #logging.debug("angle loop added 1 to {0}".format(item)) 
                   self.vent_map[item[0]][item[1]] += 1
            #logging.debug("Map now looks like:\n{0}".format(DataFrame(self.vent_map)))

    def countExtraVentLocations(self):
        extra_vents = 0
        for line in self.vent_map:
            for point in line:
                if point > 1:
                    extra_vents += 1
        return extra_vents

if __name__ == '__main__':
    log_level = getattr(logging, (os.getenv("LOG_LEVEL","INFO")).upper(), None)
    logging.basicConfig(level=log_level)
    main_runner = Mapper()
    main_runner.parseFile()
    main_runner.fillVentMap()
    print(main_runner.countExtraVentLocations())
