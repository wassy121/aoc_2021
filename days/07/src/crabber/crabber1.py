import itertools as it
import logging
import os
from pandas import *
import numpy
import statistics


class Crabber:
    file_name = 'src/resources/test.txt'
    #file_name = 'src/resources/input.txt'
    crab_list = [] 

    def parseFile(self):
        with open(self.file_name) as input_file:
            self.crab_list = [int(x) for x in input_file.readline().strip().split(',')]


if __name__ == '__main__':
    log_level = getattr(logging, (os.getenv("LOG_LEVEL","INFO")).upper(), None)
    logging.basicConfig(level=log_level)
    main_runner = Crabber()
    main_runner.parseFile()
    logging.debug(main_runner.crab_list)
    center_of_gravity = statistics.median(main_runner.crab_list)
    fuel_used = sum([abs(x-center_of_gravity) for x in main_runner.crab_list])
    logging.info("center: {0} fuel: {1}".format(center_of_gravity, fuel_used))
