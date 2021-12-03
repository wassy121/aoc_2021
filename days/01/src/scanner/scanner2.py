import itertools as it
import logging
import os


class Scanner:
    file_name = 'src/resources/input.txt'
    file_contents = []
    found_increments = 0

    def parseFile(self):
        with open(self.file_name) as input_file:
            self.file_contents = [int(x) for x in input_file.readlines()]

    @staticmethod
    def determineSlidingWindow(set_a, set_b):
        if (len(set_a) < 3 or len(set_b) < 3):
            return False
        if (sum(set_a[:3]) < sum(set_b[:3])):
            return True
        else:
            return False

    @staticmethod
    def window(iterable, size):
        for i in range(len(iterable)):
            return iterable[i:i+3]

    def countIncrements(self):
        previous_set = []
        current_set = []
        for i in range(len(self.file_contents) - 2):
            current_set = Scanner.window(self.file_contents[i:], 3)
            logging.debug("prev_set: {0} , current_set: {1} , is_greater: {2}".format(previous_set, current_set, Scanner.determineSlidingWindow(previous_set, current_set)))
            if (Scanner.determineSlidingWindow(previous_set, current_set)):
                self.found_increments += 1
            logging.debug("found_increments: {0}".format(self.found_increments))
            previous_set = current_set

if __name__ == '__main__':
    log_level = getattr(logging, (os.getenv("LOG_LEVEL","INFO")).upper(), None)
    logging.basicConfig(level=log_level)
    main_scanner = Scanner()
    main_scanner.parseFile()
    main_scanner.countIncrements()
    print(main_scanner.found_increments)

