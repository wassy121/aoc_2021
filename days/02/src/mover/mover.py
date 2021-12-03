import itertools as it
import logging
import os


class Mover:
    file_name = 'src/resources/input.txt'
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

    def countDirection(self):
        for move in self.moves:
            if move[0] == "forward":
                self.forward_moves.append(int(move[1]))
                logging.debug("added {0} to forward_moves, total: {1}".format(int(move[1]), sum(self.forward_moves)))
            if move[0] == "backward":
                self.backward_moves.append(int(move[1]))
                logging.debug("added {0} to backward_moves, total: {1}".format(int(move[1]), sum(self.backward_moves)))
            if move[0] == "left":
                self.left_moves.append(int(move[1]))
                logging.debug("added {0} to left_moves, total: {1}".format(int(move[1]), sum(self.left_moves)))
            if move[0] == "right":
                self.right_moves.append(int(move[1]))
                logging.debug("added {0} to right_moves, total: {1}".format(int(move[1]), sum(self.right_moves)))
            if move[0] == "down":
                self.down_moves.append(int(move[1]))
                logging.debug("added {0} to down_moves, total: {1}".format(int(move[1]), sum(self.down_moves)))
            if move[0] == "up":
                self.up_moves.append(int(move[1]))
                logging.debug("added {0} to up_moves, total: {1}".format(int(move[1]), sum(self.up_moves)))

if __name__ == '__main__':
    log_level = getattr(logging, (os.getenv("LOG_LEVEL","INFO")).upper(), None)
    logging.basicConfig(level=log_level)
    main_runner = Mover()
    main_runner.parseFile()
    main_runner.countDirection()
    sum_forward = sum(main_runner.forward_moves) - sum(main_runner.backward_moves)
    sum_down = sum(main_runner.down_moves) - sum(main_runner.up_moves)
    logging.debug("sum forward: {0}, sum down: {1}".format(sum_forward,sum_down))
    print("{0}".format(int(sum_forward) * int(sum_down)))

