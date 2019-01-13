import unittest
from repose_records import Record, read_records, total_sleep_per_guard

class TestRecord(unittest.TestCase):
    def test_total_sleep_single_sleeping_time(self):
        record = Record(1, [(1,4)])
        self.assertEqual(record.total_sleep(), 3)

        record = Record(2, [(0,34)])
        self.assertEqual(record.total_sleep(), 34)

        record = Record(3, [(5,14)])
        self.assertEqual(record.total_sleep(), 9)

class TestReadRecords(unittest.TestCase):
    def setUp(self):
        self.lines = ["[1518-11-01 00:00] Guard #10 begins shift",
"[1518-11-01 00:05] falls asleep",
"[1518-11-01 00:25] wakes up",
"[1518-11-01 00:30] falls asleep",
"[1518-11-01 00:55] wakes up",
"[1518-11-01 23:58] Guard #99 begins shift",
"[1518-11-02 00:40] falls asleep",
"[1518-11-02 00:50] wakes up",
"[1518-11-03 00:05] Guard #10 begins shift",
"[1518-11-03 00:24] falls asleep",
"[1518-11-03 00:29] wakes up",
"[1518-11-04 00:02] Guard #99 begins shift",
"[1518-11-04 00:36] falls asleep",
"[1518-11-04 00:46] wakes up",
"[1518-11-05 00:03] Guard #99 begins shift",
"[1518-11-05 00:45] falls asleep",
"[1518-11-05 00:55] wakes up"]
        record1 = Record(10, [(5, 25)])
        record2 = Record(10, [(30, 55)])
        record3 = Record(99, [(40, 50)])
        record4 = Record(10, [(24, 29)])
        record5 = Record(99, [(36, 46)])
        record6 = Record(99, [(45, 55)])
        self.expectedRecords = [record1, record2, record3, record4,  record5, record6]

    def test_correct_result_read_records(self):
        self.records = read_records(self.lines)
        self.assertEqual(self.records, self.expectedRecords)

    def test_correct_total_sleep_per_guard(self):
        sleep = total_sleep_per_guard(self.expectedRecords)
        self.assertEqual(sleep, {10: 50, 99: 30})

if __name__ == "__main__":
    unittest.main()
