from typing import List, Tuple, Dict
import parse
import sys

class RecordParser:
    def __init__(self) -> None:
        self.guard_id_parser = parse.compile("[{year}-{month}-{day} {hour}:{minute}] Guard #{guard_id} begins shift")
        self.falls_asleep_parser = parse.compile("[{year}-{month}-{day} {hour}:{minute}] falls asleep")
        self.wakes_up_parser =     parse.compile("[{year}-{month}-{day} {hour}:{minute}] wakes up")

    def parse_shift_begin(self, string: str) -> Dict:
        return self.guard_id_parser.parse(string)

    def parse_falls_asleep(self, string:str) -> Dict:
        return self.falls_asleep_parser.parse(string)

    def parse_wakes_up(self, string: str) -> Dict:
        return self.wakes_up_parser.parse(string)

class Record:
    def __init__(self, guard_id: int, sleeping_times: List[Tuple[int, int]]) -> None:
        self.guard_id = guard_id
        self.sleeping_times = sleeping_times

    def __repr__(self):
        return "Guard id: " + repr(self.guard_id) + " " + repr(self.sleeping_times)

    def __eq__(self, other):
        if isinstance(other, Record) and self.guard_id == other.guard_id and self.sleeping_times == other.sleeping_times:
            return True
        else:
            return False

    def total_sleep(self) -> int:
        total = 0
        for start, end in self.sleeping_times:
            total += int(end) - int(start)
        return total

def read_records(lines) -> List[Record]:
    parser = RecordParser()
    lines.sort()
    records = []
    guard_id = -1
    sleeping_times: List[Tuple[int, int]] = []
    sleeping = False
    for line in lines:
        result = parser.parse_shift_begin(line)
        if result:
            guard_id = int(result["guard_id"])
        elif not sleeping:
            result = parser.parse_falls_asleep(line)
            falls_asleep = int(result["minute"])
            sleeping = True
        else:
            result = parser.parse_wakes_up(line)
            sleeping_times = [(falls_asleep, int(result["minute"]))]
            sleeping = False
            records.append(Record(guard_id, sleeping_times))
    return records

def total_sleep_per_guard(records: List[Record]) -> Dict[int, int]:
    records.sort(key = lambda r: r.guard_id)
    guards = dict([])
    for record in records:
        if record.guard_id in guards:
            guards[record.guard_id] += record.total_sleep()
        else:
            guards[record.guard_id] = record.total_sleep()
    return guards

def minute_most_asleep(records: List[Record]) -> int:
    sleeping_times = []
    minutes = [0] * 60
    for record in records:
        for interval in record.sleeping_times:
            for minute in range(interval[0], interval[1]):
                minutes[minute] += 1
    return max(enumerate(minutes), key= lambda m: m[1])


if __name__ == "__main__":
    lines = [x.strip() for x in sys.stdin.readlines()]
    records = read_records(lines)
    guards = total_sleep_per_guard(records)
    sleeping_guard_id = max(guards, key = (lambda key: guards[key]))
    print(sleeping_guard_id)
    most_sleeping_records = filter(lambda r: r.guard_id == sleeping_guard_id, records)
    minute = minute_most_asleep(most_sleeping_records)
    print(minute)
    print(sleeping_guard_id * minute[0]) #correct answer: 72925
