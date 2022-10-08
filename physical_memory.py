from tokenize import String
from pprint import pprint


class PhysicalMemory:
    def __init__(self, size):
        self.size = size
        self.space = dict()
        for i in range(self.size):
            self.space[i] = ""

    def read_sector(self, sector):
        data = self.space[sector]
        self.space[sector] = ""
        return data

    def write_sector(self, sector, data):
        self.space[sector] = data
    
    def read_segment(self, segment_start, offset):
        data = []
        for i in range(offset):
            sector = segment_start + i
            data.append(self.space[sector])
        return data

    def write_segment(self, segment_start, offset, data):
        if len(data) > offset + 1:
            return False
        else:
            for i, d in enumerate(data):
                sector = segment_start + i
                self.space[sector] = data[i]
            return True

    def print_memory(self):
        pprint(self.space)