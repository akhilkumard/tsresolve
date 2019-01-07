from tsresolve.time_stamp_resolver import point_of_time, period_of_time
import unittest

# TODO DO NOT CHANGE THIS !!!
NOW = "2018-12-1T08:30:0"

# TODO DO NOT CHANGE THIS !!!


class TimestampRoutes_Point_of_time_Tests(unittest.TestCase):

    def test_point_of_time_01(self):
        result = point_of_time("Schedule a meeting with Raja at 9 p.m.", NOW)
        expected_timestamp = "2018-12-01T21:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_02(self):
        result = point_of_time("Schedule a meeting at 9 p.m. with Nava", NOW)
        expected_timestamp = "2018-12-01T21:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_03(self):
        result = point_of_time("Schedule a meeting with Sayyad on 8 a.m.", NOW)
        expected_timestamp = "2018-12-01T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_04(self):
        result = point_of_time("Schedule a meeting on 8 a.m. with Parmanand", NOW)
        expected_timestamp = "2018-12-01T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_05(self):
        result = point_of_time("Schedule a meeting with Harish for tomorrow", NOW)
        expected_timestamp = "2018-12-02T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_06(self):
        result = point_of_time("Schedule a meeting for tomorrow with Akhil", NOW)
        expected_timestamp = "2018-12-02T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_07(self):
        result = point_of_time("Schedule a meeting with Jhansi on tomorrow", NOW)
        expected_timestamp = "2018-12-02T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_08(self):
        result = point_of_time("Schedule a meeting on tomorrow with Mounika", NOW)
        expected_timestamp = "2018-12-02T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_09(self):
        result = point_of_time("Schedule a meeting with Anirudh tomorrow", NOW)
        expected_timestamp = "2018-12-02T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_10(self):
        result = point_of_time("Schedule a meeting with Sandeep for tomorrow at 5 p.m.", NOW)
        expected_timestamp = "2018-12-02T17:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_11(self):
        result = point_of_time("Schedule meeting for tomorrow at 5 p.m. with Bipasha", NOW)
        expected_timestamp = "2018-12-02T17:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_12(self):
        result = point_of_time("Schedule meeting with Priyanka for tomorrow 5 p.m.", NOW)
        expected_timestamp = "2018-12-02T17:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_13(self):
        result = point_of_time("Schedule a meeting at 5 p.m. tomorrow with Virgil", NOW)
        expected_timestamp = "2018-12-02T17:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_14(self):
        result = point_of_time("Schedule a meeting with Kiran on monday at 4 p.m.", NOW)
        expected_timestamp = "2018-12-03T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_15(self):
        result = point_of_time("Schedule meeting on monday at 4 p.m. with Vidyadhar", NOW)
        expected_timestamp = "2018-12-03T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_16(self):
        result = point_of_time("Schedule a meeting at 4 p.m. of monday with Revanth", NOW)
        expected_timestamp = "2018-12-03T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_17(self):
        result = point_of_time("Schedule a meeting on 4 p.m. of monday with Shiva", NOW)
        expected_timestamp = "2018-12-03T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_18(self):
        result = point_of_time("Schedule meeting with Radhasree on monday 4 p.m.", NOW)
        expected_timestamp = "2018-12-03T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_19(self):
        result = point_of_time("Schedule a meeting on 10 a.m. monday with Udayan", NOW)
        expected_timestamp = "2018-12-03T10:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_20(self):
        result = point_of_time("Schedule a meeting on monday with Jens at 4 p.m.", NOW)
        expected_timestamp = "2018-12-03T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

# TODO This should prompt all time slots for the entire day, until the assistant don't have facility for the timing.
    def test_point_of_time_21(self):
        result = point_of_time("Schedule a meeting with Krishna on monday", NOW)
        expected_timestamp = "2018-12-03T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

# TODO This should prompt all time slots for the entire day, until the assistant don't have facility for the timing.
    def test_point_of_time_22(self):
        result = point_of_time("Schedule meeting on tuesday with Roja", NOW)
        expected_timestamp = "2018-12-04T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_23(self):
        result = point_of_time("Schedule a meeting with Sai on tuesday at 7 p.m.", NOW)
        expected_timestamp = "2018-12-04T19:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_24(self):
        result = point_of_time("Schedule meeting on tuesday at 8 p.m. with Manikanta", NOW)
        expected_timestamp = "2018-12-04T20:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_25(self):
        result = point_of_time("Schedule a meeting at 5 a.m. of tuesday with Raja", NOW)
        expected_timestamp = "2018-12-04T05:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_26(self):
        result = point_of_time("Schedule meeting on tuesday 7 p.m. with Sayyad", NOW)
        expected_timestamp = "2018-12-04T19:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_27(self):
        result = point_of_time("Schedule meeting on tuesday with Parmanand at 7 p.m.", NOW)
        expected_timestamp = "2018-12-04T19:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_28(self):
        result = point_of_time("Schedule meeting with Akhil tuesday 7 p.m.", NOW)
        expected_timestamp = "2018-12-04T19:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_29(self):
        result = point_of_time("Schedule a meeting with Jhansi on next wednesday", NOW)
        expected_timestamp = "2018-12-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_30(self):
        result = point_of_time("Schedule meeting on next wednesday with Mounika", NOW)
        expected_timestamp = "2018-12-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_31(self):
        result = point_of_time("Schedule meeting with Nava next wednesday", NOW)
        expected_timestamp = "2018-12-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_32(self):
        result = point_of_time("Schedule a meeting next wednesday with Harish", NOW)
        expected_timestamp = "2018-12-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_33(self):
        result = point_of_time("Schedule a meeting with Krishna on next wednesday at 9 p.m.", NOW)
        expected_timestamp = "2018-12-05T21:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_34(self):
        result = point_of_time("Schedule meeting on next wednesday at 9 p.m. with Virgil", NOW)
        expected_timestamp = "2018-12-05T21:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_35(self):
        result = point_of_time("Schedule a meeting on next wednesday with Prasanna at 9 a.m.", NOW)
        expected_timestamp = "2018-12-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_36(self):
        result = point_of_time("Schedule meeting at 11 p.m. of next wednesday with Anusha", NOW)
        expected_timestamp = "2018-12-05T23:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_37(self):
        result = point_of_time("Schedule a meeting with harivikram on next wednesday 9 p.m.", NOW)
        expected_timestamp = "2018-12-05T21:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_38(self):
        result = point_of_time("Schedule a meeting with Atchuta on next week", NOW)
        expected_timestamp = "2018-12-08T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_39(self):
        result = point_of_time("Schedule meeting on next week with Ramesh", NOW)
        expected_timestamp = "2018-12-08T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_40(self):
        result = point_of_time("Schedule a meeting for next week with Anirudh", NOW)
        expected_timestamp = "2018-12-08T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_41(self):
        result = point_of_time("Schedule a meeting with Sandeep next week", NOW)
        expected_timestamp = "2018-12-08T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_42(self):
        result = point_of_time("Schedule a meeting with Bipasha on next week at 4 p.m.", NOW)
        expected_timestamp = "2018-12-08T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_43(self):
        result = point_of_time("Schedule a meeting with Priyanka on next week 4 a.m.", NOW)
        expected_timestamp = "2018-12-08T04:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_44(self):
        result = point_of_time("Schedule a meeting on next week at 4 p.m. with Udayan", NOW)
        expected_timestamp = "2018-12-08T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_45(self):
        result = point_of_time("Schedule meeting on next week with Aditya at 4 p.m.", NOW)
        expected_timestamp = "2018-12-08T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_46(self):
        result = point_of_time("Schedule meeting with Arghyadeb at 4 p.m. of next week", NOW)
        expected_timestamp = "2018-12-08T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_47(self):
        result = point_of_time("Schedule meeting at 4 p.m. of next week with raja", NOW)
        expected_timestamp = "2018-12-08T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_48(self):
        result = point_of_time("Schedule meeting at 4 p.m. with Jens on next week", NOW)
        expected_timestamp = "2018-12-08T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_49(self):
        result = point_of_time("Schedule meeting with Raja and Parmanand at 4 p.m. next week", NOW)
        expected_timestamp = "2018-12-08T16:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_50(self):
        result = point_of_time("Schedule a meeting with Raja and Akhil on next week tuesday at 6 a.m.", NOW)
        expected_timestamp = "2018-12-04T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_51(self):
        result = point_of_time("Schedule meeting on next week tuesday at 6 a.m. with Raja and Jhansi", NOW)
        expected_timestamp = "2018-12-04T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_52(self):
        result = point_of_time("Schedule meeting on next week tuesday with Sayyad and Mounika at 6 a.m.", NOW)
        expected_timestamp = "2018-12-04T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_53(self):
        result = point_of_time("Schedule meeting with Akhil, Jhasi and Raja at 6 a.m. of next week tuesday", NOW)
        expected_timestamp = "2018-12-04T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_54(self):
        result = point_of_time("Schedule a meeting at 6 a.m. of next week tuesday with Akhil, Parmanand and Raja", NOW)
        expected_timestamp = "2018-12-04T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_55(self):
        result = point_of_time("Schedule a meeting at 6 a.m. with Sandeep on next week tuesday", NOW)
        expected_timestamp = "2018-12-04T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_56(self):
        result = point_of_time("Schedule a meeting with Santhosh at 6 a.m. next week tuesday", NOW)
        expected_timestamp = "2018-12-04T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_57(self):
        result = point_of_time("Schedule a meeting at 7 a.m. next week tuesday with raja", NOW)
        expected_timestamp = "2018-12-04T07:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_58(self):
        result = point_of_time("Schedule a meeting at 8 a.m. with Prasanna for next week tuesday", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_59(self):
        result = point_of_time("Schedule a meeting with Udayan next week tuesday 7:30 a.m.", NOW)
        expected_timestamp = "2018-12-04T07:30:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_60(self):
        result = point_of_time("Schedule meeting for next week tuesday at 6 a.m. with Virgil", NOW)
        expected_timestamp = "2018-12-04T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_61(self):
        result = point_of_time("Schedule meeting for next week tuesday with Arghyadeb at 8 a.m.", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_62(self):
        result = point_of_time("Schedule a meeting with Revanth on tuesday of next week at 8:15 a.m.", NOW)
        expected_timestamp = "2018-12-04T08:15:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_63(self):
        result = point_of_time("Schedule meeting with Vidyadhar at 8 a.m. on tuesday of next week", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_64(self):
        result = point_of_time("Schedule a meeting at 8 a.m. with Atchuta on tuesday of next week", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_65(self):
        result = point_of_time("Schedule a meeting at 8 a.m. on tuesday of next week with Akhil", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_66(self):
        result = point_of_time("Schedule meeting on tuesday of next week at 8 a.m. with Manikanta", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_67(self):
        result = point_of_time("Schedule meeting on tuesday of next week with raja at 8 a.m.", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_68(self):
        result = point_of_time("Schedule a meeting with raja at 8 a.m. on tuesday of next week", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_69(self):
        result = point_of_time("Schedule a meeting at 8 a.m. with raja on tuesday of next week", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_70(self):
        result = point_of_time("Schedule a meeting at 8 a.m. on tuesday of next week with raja", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_71(self):
        result = point_of_time("Schedule a meeting with Raja on thursday next week 8 a.m.", NOW)
        expected_timestamp = "2018-12-06T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_72(self):
        result = point_of_time("Schedule meeting on tuesday next week 8 a.m. with raja", NOW)
        expected_timestamp = "2018-12-04T08:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_73(self):
        result = point_of_time("Schedule a meeting with raja on first monday of next month", NOW)
        expected_timestamp = "2019-01-07T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_74(self):
        result = point_of_time("Schedule a meeting on first monday of next month with raja", NOW)
        expected_timestamp = "2019-01-07T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_75(self):
        result = point_of_time("Schedule a meeting with raja on first monday of next month at 6 p.m.", NOW)
        expected_timestamp = "2019-01-07T18:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_76(self):
        result = point_of_time("Schedule a meeting on first monday of next february with raja", NOW)
        expected_timestamp = "2019-02-04T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_77(self):
        result = point_of_time("Schedule a meeting with raja on first monday of next february at 6 p.m.", NOW)
        expected_timestamp = "2019-02-04T18:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_78(self):
        result = point_of_time("Schedule a meeting on first monday of next month at 6 p.m. with raja", NOW)
        expected_timestamp = "2019-01-07T18:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_79(self):
        result = point_of_time("Schedule a meeting on first monday of next month with raja at 6 p.m.", NOW)
        expected_timestamp = "2019-01-07T18:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

# TODO This should prompt all time slots for the entire day, until the assistant don't have facility for the timing.
    def test_point_of_time_80(self):
        result = point_of_time("Schedule a meeting with raja on August 5th", NOW)
        expected_timestamp = "2019-08-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

# TODO This should prompt all time slots for the entire day, until the assistant don't have facility for the timing.
    def test_point_of_time_81(self):
        result = point_of_time("Schedule a meeting on August 5th with raja", NOW)
        expected_timestamp = "2019-08-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

# TODO This should prompt all time slots for the entire day, until the assistant don't have facility for the timing.
    def test_point_of_time_82(self):
        result = point_of_time("Schedule meeting with raja for August 5th", NOW)
        expected_timestamp = "2019-08-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

# TODO This should prompt all time slots for the entire day, until the assistant don't have facility for the timing.
    def test_point_of_time_83(self):
        result = point_of_time("Schedule meeting for August 5th with raja", NOW)
        expected_timestamp = "2019-08-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_84(self):
        result = point_of_time("Schedule a meeting with raja on August 5th at 5 a.m.", NOW)
        expected_timestamp = "2019-08-05T05:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_85(self):
        result = point_of_time("Schedule a meeting on August 5th at 5 a.m. with raja", NOW)
        expected_timestamp = "2019-08-05T05:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_86(self):
        result = point_of_time("Schedule a meeting on August 5th with raja at 5 a.m.", NOW)
        expected_timestamp = "2019-08-05T05:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_87(self):
        result = point_of_time("Schedule a meeting with raja at 5 a.m. on August 5th", NOW)
        expected_timestamp = "2019-08-05T05:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_88(self):
        result = point_of_time("Schedule a meeting at 5 a.m. on August 5th with raja", NOW)
        expected_timestamp = "2019-08-05T05:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_89(self):
        result = point_of_time("Schedule a meeting at 5 a.m. with raja on August 5th", NOW)
        expected_timestamp = "2019-08-05T05:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_90(self):
        result = point_of_time("Schedule a meeting with raja for August 5th 5 a.m.", NOW)
        expected_timestamp = "2019-08-05T05:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_91(self):
        result = point_of_time("Schedule a meeting for August 5th 5 p.m. with raja", NOW)
        expected_timestamp = "2019-08-05T17:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_92(self):
        result = point_of_time("Schedule a meeting for August 5th with raja at 5 a.m.", NOW)
        expected_timestamp = "2019-08-05T05:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_93(self):
        result = point_of_time("Schedule a meeting on 5th of November with raja", NOW)
        expected_timestamp = "2019-11-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_94(self):
        result = point_of_time("Schedule a meeting with raja on 5th of November", NOW)
        expected_timestamp = "2019-11-05T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_95(self):
        result = point_of_time("Schedule a meeting with raja on 5th of November at 2 p.m.", NOW)
        expected_timestamp = "2019-11-05T14:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_96(self):
        result = point_of_time("Schedule a meeting on 5th of November at 2:30 p.m. with raja", NOW)
        expected_timestamp = "2019-11-05T14:30:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_97(self):
        result = point_of_time("Schedule a meeting on 5th of November with raja at 2 p.m.", NOW)
        expected_timestamp = "2019-11-05T14:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_98(self):
        result = point_of_time("Schedule a meeting with raja on second friday of November", NOW)
        expected_timestamp = "2019-11-08T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_99(self):
        result = point_of_time("Schedule a meeting on second friday of November with raja", NOW)
        expected_timestamp = "2019-11-08T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_100(self):
        result = point_of_time("Schedule a meeting with raja on second friday of November at 2 p.m.", NOW)
        expected_timestamp = "2019-11-08T14:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_101(self):
        result = point_of_time("Schedule a meeting on second friday of November at 2 p.m. with raja", NOW)
        expected_timestamp = "2019-11-08T14:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    # TODO Too ambitious
    @unittest.skipIf(True, 'Too ambitious')
    def test_point_of_time_102(self):
        result = point_of_time("Schedule a meeting on second friday of November with raja at 2 p.m.", NOW)
        expected_timestamp = "2019-11-08T14:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_103(self):
        result = point_of_time("Schedule a meeting with raja on tuesday at 7:30 p.m.", NOW)
        expected_timestamp = "2018-12-04T19:30:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_104(self):
        result = point_of_time("Schedule a meeting with raja on tuesday morning at 7 o'clock", NOW)
        expected_timestamp = "2018-12-04T07:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_105(self):
        result = point_of_time("Schedule a meeting with raja on tuesday evening at 8 o'clock", NOW)
        expected_timestamp = "2018-12-04T20:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_108(self):
        result = point_of_time("Schedule a meeting with raja on tuesday evening at 8", NOW)
        expected_timestamp = "2018-12-04T20:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_109(self):
        result = point_of_time("Schedule a meeting with raja on tuesday evening at 9", NOW)
        expected_timestamp = "2018-12-04T21:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_110(self):
        result = point_of_time("Schedule a meeting with raja on thursday morning at 11", NOW)
        expected_timestamp = "2018-12-06T11:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_111(self):
        result = point_of_time("Schedule a meeting with raja on tomorrow morning at 11", NOW)
        expected_timestamp = "2018-12-02T11:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_112(self):
        result = point_of_time("Schedule a meeting with raja on tomorrow morning at 11 o'clock", NOW)
        expected_timestamp = "2018-12-02T11:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_113(self):
        result = point_of_time("Schedule a meeting with raja on tomorrow evening at 8", NOW)
        expected_timestamp = "2018-12-02T20:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_114(self):
        result = point_of_time("Schedule a meeting with raja on tomorrow evening at 8 o'clock", NOW)
        expected_timestamp = "2018-12-02T20:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_115(self):
        NOW = "2018-12-3T08:30:0"
        result = point_of_time("schedule a meeting with Krishna and Virgil on this weekend", NOW)
        expected_timestamp = "2018-12-08T09:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], False)

    def test_point_of_time_116(self):
        NOW = "2018-12-3T08:30:0"
        result = point_of_time("schedule a meeting with Krishna and Virgil on this weekend morning at 6", NOW)
        expected_timestamp = "2018-12-08T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_117(self):
        NOW = "2018-12-11T10:30:0"
        result = point_of_time("schedule a meeting with Krishna and Virgil on this weekend evening at 6", NOW)
        expected_timestamp = "2018-12-15T18:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_118(self):
        NOW = "2018-12-11T10:30:0"
        result = point_of_time("schedule a meeting with Krishna and Virgil on this weekend morning", NOW)
        expected_timestamp = "2018-12-15T06:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_119(self):
        NOW = "2018-12-11T10:30:0"
        result = point_of_time("schedule a meeting with Krishna and Virgil on this weekend noon", NOW)
        expected_timestamp = "2018-12-15T12:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)

    def test_point_of_time_120(self):
        NOW = "2018-12-11T10:30:0"
        result = point_of_time("schedule a meeting with Krishna and Virgil on this weekend afternoon", NOW)
        expected_timestamp = "2018-12-15T13:00:00"
        self.assertEqual(result[0], expected_timestamp)
        self.assertEqual(result[1], True)


class TimestampRoutes_Period_of_time_Tests(unittest.TestCase):

    def test_period_of_time_0(self):
        result = period_of_time("Search meetings from yesterday", NOW)
        expected_timestamp = ('2018-11-30T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_01(self):
        result = period_of_time("Search meetings from February", NOW)
        expected_timestamp = ('2018-02-01T00:00:00', '2018-02-28T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_02(self):
        result = period_of_time("Search meetings from last November", NOW)
        expected_timestamp = ('2017-11-01T00:00:00', '2017-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_03(self):
        result = period_of_time("Search meetings from November", NOW)
        expected_timestamp = ('2018-11-01T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_04(self):
        result = period_of_time("Search meetings from August to November", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_05(self):
        result = period_of_time("Search meetings from last August to November", NOW)
        expected_timestamp = ('2017-08-01T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_06(self):
        result = period_of_time("Search meetings from August till now", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-12-01T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_07(self):
        result = period_of_time("Search meetings from last August till now", NOW)
        expected_timestamp = ('2017-08-01T00:00:00', '2018-12-01T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_08(self):
        result = period_of_time("Search meetings from January 5th to November 3rd", NOW)
        expected_timestamp = ('2018-01-05T00:00:00', '2018-11-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_09(self):
        result = period_of_time("Search meetings from last August 5th to last November 3rd", NOW)
        expected_timestamp = ('2017-08-05T00:00:00', '2017-11-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_10(self):
        result = period_of_time("Search meetings from this August 5th to November 3rd", NOW)
        expected_timestamp = ('2018-08-05T00:00:00', '2018-11-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'To be handled')
    def test_period_of_time_11(self):
        result = period_of_time("Search meetings from 2018 to 2019", NOW)
        expected_timestamp = ("2018-01-01:00:00:00", "2019-12-31:23:59:59")
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_12(self):
        result = period_of_time("Search meetings from last August to November", NOW)
        expected_timestamp = ('2017-08-01T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_13(self):
        result = period_of_time("Search meetings from last August 5th to November 3rd", NOW)
        expected_timestamp = ('2017-08-05T00:00:00', '2018-11-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_14(self):
        result = period_of_time("Search meetings for last week", NOW)
        expected_timestamp = ('2018-11-19T00:00:00', '2018-11-24T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_15(self):
        result = period_of_time("Search meetings for last month", NOW)
        expected_timestamp = ('2018-11-01T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_16(self):
        result = period_of_time("Search meetings for last year", NOW)
        expected_timestamp = ('2017-01-01T00:00:00', '2017-12-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_17(self):
        result = period_of_time("Search meetings for last 2 months", NOW)
        expected_timestamp = ("2018-10-01:00:00:00", "2018-11-30:23:59:59")
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_18(self):
        result = period_of_time("Search meetings for this month", NOW)
        expected_timestamp = ('2018-12-01T00:00:00', '2018-12-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_19(self):
        result = period_of_time("Search meetings for this week", NOW)
        expected_timestamp = ('2018-11-26T00:00:00', '2018-12-01T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_20(self):
        result = period_of_time("Search meetings for this year", NOW)
        expected_timestamp = ('2018-01-01T00:00:00', '2018-12-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_21(self):
        result = period_of_time("Search meetings for last 2 weeks", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_22(self):
        result = period_of_time("Search meetings for last 2 years", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_23(self):
        result = period_of_time("Search meetings in 3rd week of this month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_24(self):
        result = period_of_time("Search meetings in 3rd week of last month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_25(self):
        result = period_of_time("Search meetings from 3rd week of this month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_26(self):
        result = period_of_time("Search meetings from 3rd week of last month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_27(self):
        result = period_of_time("Search meetings from August 5th to November 3rd this year", NOW)
        expected_timestamp = ('2018-08-05T00:00:00', '2018-11-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_28(self):
        result = period_of_time("Search meetings from last August 5th to last November 3rd", NOW)
        expected_timestamp = ('2017-08-05T00:00:00', '2017-11-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_29(self):
        result = period_of_time("Search meetings from last August till yesterday", NOW)
        expected_timestamp = ('2017-08-01T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_30(self):
        result = period_of_time("Search meetings from this August till yesterday", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_31(self):
        result = period_of_time("Search meetings from August till yesterday", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_32(self):
        result = period_of_time("Search meetings from last August 3rd till yesterday", NOW)
        expected_timestamp = ('2017-08-03T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_33(self):
        result = period_of_time("Search meetings from this August 3rd till yesterday", NOW)
        expected_timestamp = ('2018-08-03T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_34(self):
        result = period_of_time("Search meetings from August 3rd till yesterday", NOW)
        expected_timestamp = ('2018-08-03T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_35(self):
        result = period_of_time("Search meetings after this August", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-08-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_36(self):
        result = period_of_time("Search meetings after last August", NOW)
        expected_timestamp = ('2017-08-01T00:00:00', '2017-08-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_37(self):
        result = period_of_time("Search meetings after August", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-08-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_38(self):
        result = period_of_time("Search meetings after August 2002", NOW)
        expected_timestamp = ('2002-08-01T00:00:00', '2002-08-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_39(self):
        result = period_of_time("Search meetings after this August 3rd", NOW)
        expected_timestamp = ('2018-08-03T00:00:00', '2018-08-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_40(self):
        result = period_of_time("Search meetings after last August 3rd", NOW)
        expected_timestamp = ('2017-08-03T00:00:00', '2017-08-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_41(self):
        result = period_of_time("Search meetings after August 3rd", NOW)
        expected_timestamp = ('2018-08-03T00:00:00', '2018-08-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_42(self):
        result = period_of_time("Search meetings till yesterday", NOW)
        expected_timestamp = ('2018-11-30T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_43(self):
        result = period_of_time("Search meetings from 2018", NOW)
        expected_timestamp = ('2018-01-01T00:00:00', '2018-12-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_44(self):
        result = period_of_time("Search meetings before August 3rd", NOW)
        expected_timestamp = ('2018-08-03T00:00:00', '2018-08-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_45(self):
        result = period_of_time("Search meetings before this August 3rd", NOW)
        expected_timestamp = ('2018-08-03T00:00:00', '2018-08-03T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_46(self):
        result = period_of_time("Search meetings before last September 13th", NOW)
        expected_timestamp = ('2017-09-13T00:00:00', '2017-09-13T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_47(self):
        result = period_of_time("Search meetings before February", NOW)
        expected_timestamp = ('2018-02-01T00:00:00', '2018-02-28T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_48(self):
        result = period_of_time("Search meetings before last December", NOW)
        expected_timestamp = ('2017-12-01T00:00:00', '2017-12-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_49(self):
        result = period_of_time("Search meetings before this August", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-08-31T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_50(self):
        result = period_of_time("Search meetings in August and September", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-09-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_51(self):
        result = period_of_time("Search meetings in this August and September", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-09-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    # TODO TO BE DISCUSSED
    def test_period_of_time_52(self):
        result = period_of_time("Search meetings in August and September", NOW)
        expected_timestamp = ('2018-08-01T00:00:00', '2018-09-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_53(self):
        NOW = "2018-12-21T15:18:0"
        result = period_of_time("Search meetings from yesterday", NOW)
        expected_timestamp = ('2018-12-20T00:00:00', '2018-12-20T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_54(self):
        result = period_of_time("Search meetings from yesterday evening", NOW)
        expected_timestamp = ('2018-11-30T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_55(self):
        NOW = "2018-12-21T15:18:0"
        result = period_of_time("Search meetings from last Monday", NOW)
        expected_timestamp = ('2018-12-10T00:00:00', '2018-12-10T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_56(self):
        NOW = "2018-12-21T15:18:0"
        result = period_of_time("Search meetings from this Monday", NOW)
        expected_timestamp = ('2018-12-17T00:00:00', '2018-12-17T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_57(self):
        NOW = "2018-12-21T15:18:0"
        result = period_of_time("Search meetings from next Tuesday", NOW)
        expected_timestamp = ('2018-12-25T00:00:00', '2018-12-25T23:59:59')
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_58(self):
        result = period_of_time("Search meetings from second Monday of this month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_59(self):
        result = period_of_time("Search meetings from second Monday of last month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_60(self):
        result = period_of_time("Search meetings from second Monday of this August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_61(self):
        result = period_of_time("Search meetings from second Monday of last August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_62(self):
        result = period_of_time("Search meetings from Monday to Friday", NOW)
        expected_timestamp = ('2018-11-26T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_63(self):
        result = period_of_time("Search meetings from last Monday to last Friday", NOW)
        expected_timestamp = ('2018-11-19T00:00:00', '2018-11-23T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_64(self):
        result = period_of_time("Search meetings from this Monday to this Friday", NOW)
        expected_timestamp = ('2018-11-26T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_65(self):
        result = period_of_time("Search meetings from Monday morning", NOW)
        expected_timestamp = ('2018-11-26T00:00:00', '2018-11-26T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_66(self):
        result = period_of_time("Search meetings from Tuesday evening", NOW)
        expected_timestamp = ('2018-11-27T00:00:00', '2018-11-27T23:59:59')
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_67(self):
        result = period_of_time("Search meetings from last weekend", NOW)
        expected_timestamp = ('2018-11-17T00:00:00', '2018-11-17T23:59:59')
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_68(self):
        result = period_of_time("Search meetings from last week of August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_69(self):
        result = period_of_time("Search meetings from last week of  this August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_70(self):
        result = period_of_time("Search meetings from third week of August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_71(self):
        result = period_of_time("Search meetings in last week of August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_72(self):
        result = period_of_time("Search meetings in first week of August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_73(self):
        result = period_of_time("Search meetings for second week of this month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_74(self):
        result = period_of_time("Search meetings on second week of last month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_75(self):
        result = period_of_time("Search meetings from second Monday of this month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_76(self):
        result = period_of_time("Search meetings from second Monday of last month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_77(self):
        result = period_of_time("Search meetings for second week of last month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_78(self):
        result = period_of_time("Search meetings on second week of this month", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_79(self):
        result = period_of_time("Search meetings from Monday morning to Thursday evening", NOW)
        expected_timestamp = ('2018-11-26T00:00:00', '2018-11-29T23:59:59')
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_80(self):
        result = period_of_time("Search meetings from Monday morning to Thursday evening in August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_81(self):
        result = period_of_time("Search meetings from Monday morning to Thursday evening this August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_82(self):
        result = period_of_time("Search meetings from Monday morning to Thursday evening last August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_83(self):
        result = period_of_time("Search meetings from Monday morning to Thursday evening in  first week of August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_84(self):
        result = period_of_time("Search meetings from Monday morning to Thursday evening in first week of this August",
                                NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_85(self):
        result = period_of_time("Search meetings from Monday morning to Thursday evening in first week of last August",
                                NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_86(self):
        result = period_of_time("Search meetings in first Monday of August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_87(self):
        result = period_of_time("Search meetings in first Monday of this August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_88(self):
        result = period_of_time("Search meetings in first Monday of last August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_89(self):
        result = period_of_time("Search meetings in first Monday of August 2018", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_90(self):
        result = period_of_time("Search meetings from first week of August to second week of September", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_91(self):
        result = period_of_time("Search meetings from first week and third week of August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_92(self):
        result = period_of_time("Search meetings from first Sunday to last Sunday of August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_93(self):
        result = period_of_time("Search meetings from first Sunday to last Sunday of last August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_94(self):
        result = period_of_time("Search meetings from first Sunday to last Sunday of this August", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_95(self):
        result = period_of_time("Search meetings from first Sunday to last Sunday of August this year", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_96(self):
        result = period_of_time("Search meetings from first Sunday to last Sunday of August in last year", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Too ambitious')
    def test_period_of_time_97(self):
        result = period_of_time("Search meetings from first Sunday to last Sunday of August 2018", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Not handling time level')
    def test_period_of_time_98(self):
        result = period_of_time("Search meetings from yesterday 10 a.m.", NOW)
        expected_timestamp = ('2018-11-30T00:00:00', '2018-11-30T23:59:59')
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Not handling time level')
    def test_period_of_time_99(self):
        result = period_of_time("Search meetings between yesterday 10 a.m. to 4 p.m.", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    @unittest.skipIf(True, 'Not handling time level')
    def test_period_of_time_100(self):
        result = period_of_time("Search meetings between yesterday 10 a.m. to today 4 p.m.", NOW)
        expected_timestamp = ("", "")
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_101(self):
        NOW = "2019-01-03T11:28:0"
        result = period_of_time("Search meetings from next month", NOW)
        expected_timestamp = ("2019-02-01T00:00:00", "2019-02-28T23:59:59")
        self.assertEqual(result, expected_timestamp)

    def test_period_of_time_102(self):
        result = period_of_time("Search meetings for tomorrow", NOW)
        expected_timestamp = ('2018-12-02T00:00:00', '2018-12-02T23:59:59')
        self.assertEqual(result, expected_timestamp)

