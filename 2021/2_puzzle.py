from dataclasses import dataclass, field
from typing import List


@dataclass
class Command:
    amount: int

    def run(self):
        ...

class Forward(Command):
    def run(self):
        return {"position": self.amount}

class Down(Command):
    def run(self):
        return {"depth": self.amount}

class Up(Command):
    def run(self):
        return {"depth": -self.amount}


@dataclass
class Submarine:
    command_list: List[Command] = field(default_factory=list)
    current_state: int = 0
    def compute_commands(self):
        aim = 0
        commands_result = {"depth": 0, "position":0}
        for command in self.command_list[:self.current_state]:
            command_result = command.run()
            depth = command_result.get('depth', 0)
            position = command_result.get('position', 0)
            if depth:
                aim += depth
            if position:
                commands_result["depth"] += position * aim
                commands_result["position"] += position
        return commands_result

    def __str__(self):
        result = self.compute_commands()
        return f"depth: {result['depth']}, position: {result['position']}, multiplyied: {result['depth'] * result['position']}"

    def add_command(self, command: Command):
        self.command_list = self.command_list[:self.current_state]
        self.command_list.append(command)
        self.current_state += 1
    def undo(self):
        self.current_state -= 1
    def redo(self):
        if self.current_state >= len(self.command_list):
            raise AssertionError("can't redo if it wasn't undo")
        self.current_state += 1


WORD_TO_COMMAND = {
    "forward": Forward,
    "down": Down,
    "up": Up,
}

if __name__ == "__main__":
    submarine = Submarine()
    with open("2_input.txt") as input:
        lines = input.readlines()
        for line in lines:
            try:
                line = line.split()
            except Exception as e:
                raise e
            if len(line) != 2:
                raise AssertionError(f"the command isn't valid (need command and argument): {' '.join(line)}.")
            try:
                command = WORD_TO_COMMAND[line[0]]
            except KeyError:
                raise AssertionError(f"{line[0]} isn't a valid command. (choose between : {list(WORD_TO_COMMAND.keys())})")
            try:
               argument = int(line[1])
            except ValueError:
                raise AssertionError(f"{line[1]} must be a number.")
            submarine.add_command(command(argument))
    print(submarine)