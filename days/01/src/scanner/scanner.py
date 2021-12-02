import logging
import os

class Scanner:
    file_name = 'src/resources/input.txt'
    file_contents = []
    found_increments = 0

    def parseFile(self):
        with open(self.file_name) as input_file:
            self.file_contents = input_file.readlines()

    def countIncrements(self):
        previous_line = None
        for line in self.file_contents:
            logging.debug("prev_line: {0} , this_line: {1} , is_greater: {2}".format(previous_line, int(line), (previous_line and int(line) > int(previous_line))))
            if (previous_line and int(line) > int(previous_line)):
                self.found_increments += 1
            logging.debug("found_increments: {0}".format(self.found_increments))
            previous_line = int(line)

if __name__ == '__main__':
    log_level = getattr(logging, (os.getenv("LOG_LEVEL","INFO")).upper(), None)
    logging.basicConfig(level=log_level)
    main_scanner = Scanner()
    main_scanner.parseFile()
    main_scanner.countIncrements()
    print(main_scanner.found_increments)
