import itertools as it
import logging
import os


class Mover:
    file_name = 'src/resources/input.txt'
    aim = 0
    depth = 0
    file_contents = []
    forward_moves = []
    backward_moves = []
    left_moves = []
    right_moves = []
    down_moves = []
    up_moves = []

    @staticmethod
    def parseMove(line):
        command_set = line.split()
        assert len(command_set) == 2
        return command_set

    def parseFile(self):
        with open(self.file_name) as input_file:
            self.moves = [Mover.parseMove(line) for line in input_file.readlines()]

    def moveDirection(self, aim, scale):
        self.forward_moves.append(scale)
        self.depth = self.depth + (scale * aim)
        logging.debug("added {0} forward moves, new sum: {1}, new depth: {2}".format(scale, sum(self.forward_moves), self.depth))



    def executeMove(self):
        for move in self.moves:
            if move[0] == "forward":
                self.moveDirection(self.aim, int(move[1]))
            if move[0] == "down":
                self.aim += int(move[1])
                logging.debug("added {0} to aim, total: {1}, depth: {2}".format(int(move[1]), self.aim, self.depth))
            if move[0] == "up":
                self.aim -= int(move[1])
                logging.debug("added {0} to aim, total: {1}, depth: {2}".format(-int(move[1]), self.aim, self.depth))

if __name__ == '__main__':
    log_level = getattr(logging, (os.getenv("LOG_LEVEL","INFO")).upper(), None)
    logging.basicConfig(level=log_level)
    main_runner = Mover()
    main_runner.parseFile()
    main_runner.aim = 0
    main_runner.executeMove()
    sum_forward = sum(main_runner.forward_moves)
    logging.debug("sum forward: {0}, depth: {1}".format(sum_forward,main_runner.depth))
    print("{0}".format(int(sum_forward) * int(main_runner.depth)))


