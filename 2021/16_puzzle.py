from abc import ABC
from enum import IntEnum
from dataclasses import dataclass, field
from io import FileIO
import io
from types import FunctionType, WrapperDescriptorType
from typing import List


def read_bit(bits, number):
    return bits[:number], bits[number:]

BASE = 2
class TYPE(IntEnum):
    LITERAL_VALUE = 4

@dataclass
class Packet:
    version: int
@dataclass
class Literal(Packet):
    value: int

import functools
def reduce(function, default):
    def wrapper(list):
        acc = default
        for val in list:
            acc = function(acc, val)
        return acc
    return wrapper

def conditional(function):
    def wrapper(list_):
        list_ = list(list_)
        for elt in list_[1:]:
            if not function(list_[0], elt):
                return 0
        return 1
    return wrapper
OPERATOR_FUNCTION = {
    0: sum,
    1: reduce(lambda a, b: a * b, 1),
    2: min,
    3: max,
    5: conditional(lambda a, b: a > b),
    6: conditional(lambda a, b: a < b),
    7: conditional(lambda a, b: a == b)
}

@dataclass
class Operator(Packet):
    operator: FunctionType 
    packets: List[Packet] = field(default_factory=list)

def read_version_type(input: FileIO):
    version = input.read(3)
    type_id = input.read(3)
    return int(version, BASE), int(type_id, BASE), 6

def read_literal(input: FileIO, version: int):
    read = 0
    bit_of_literal = ''
    while True:
        read += 5
        five_bits = input.read(5)
        if five_bits[0] == '1':
            bit_of_literal += five_bits[1:]
        else:
            bit_of_literal += five_bits[1:]
            return Literal(version, int(bit_of_literal, BASE)), read

def read_operator(input: FileIO, version: int, type_id: int):
    read = 1
    length_type_id = input.read(1)
    op = Operator(version, OPERATOR_FUNCTION[type_id])
    if length_type_id == '1':
        read += 11
        length = int(input.read(11), BASE)
        for _ in range(length):
            packet, packet_read_new = read_packet(input)
            read += packet_read_new
            op.packets.append(packet)
    if length_type_id == '0':
        read += 15
        length = int(input.read(15), BASE)
        packet_read = 0
        while packet_read < length:
            packet, packet_read_new = read_packet(input)
            packet_read += packet_read_new
            op.packets.append(packet)
        assert packet_read == length
        read += packet_read
    return op, read
    
def read_packet(input):
    version, type_id, read = read_version_type(input)
    if type_id == TYPE.LITERAL_VALUE:
        ans, packet_read = read_literal(input, version)
    else:
        ans, packet_read = read_operator(input, version, type_id)
    read += packet_read
    return ans, read

CHAR_TO_BIT = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
class Visitor(ABC):
    def visit_literal(self, packet: Literal):
        ...
    def visit_operator(self, packet: Operator):
        ...
    def visit_packet(self, packet: Packet):
        if isinstance(packet, Literal):
            return self.visit_literal(packet)
        if isinstance(packet, Operator):
            return self.visit_operator(packet)
class SumVisitor(Visitor):
    def visit_literal(self, packet: Literal):
        return packet.version
    def visit_operator(self, packet: Operator):
        return sum(map(lambda pac: self.visit_packet(pac), packet.packets)) + packet.version
class ExecuteVisitor(Visitor):
    def visit_literal(self, packet: Literal):
        return packet.value
    def visit_operator(self, packet: Operator):
        return packet.operator(map(lambda pac: self.visit_packet(pac), packet.packets))



if __name__ == "__main__":
    input = open("16_easy_input.txt")
    input = open("16_input.txt")
    string = ""
    for char in input.readline():
        string += CHAR_TO_BIT[char]
    input = io.StringIO(string)

    packet, size = read_packet(input)
    print(packet)
    print(SumVisitor().visit_packet(packet))
    print(ExecuteVisitor().visit_packet(packet))
