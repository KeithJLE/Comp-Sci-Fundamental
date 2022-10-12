# Project 4 – Graduate Rate (2017-2018)
# Name: Keith Lee
# Instructor: Dr. S. Einakian
# Section: 7

# unittest cases for graduate rate will include here
import unittest
from graduate_funcs import *


class TestCases(unittest.TestCase):
    def test_graduate_objects(self):
        self.assertTrue(Graduate(3333, "manufacturing", (220, 212), (23, 33), (2, 1)).__eq__(Graduate(4321, "eating", (220, 212), (23, 33), (2, 1))))
        self.assertFalse(Graduate(3333, "manufacturing", (220, 212), (23, 33), (2, 1)) == (Graduate(4321, "eating", (220, 212), (23, 33), (2, 2))))
        self.assertTrue(Graduate(5436, "lamps", (1322, 4343), (221, 332), (43, 90)) == (Graduate(8762, "making dirt", (1322, 4343), (221, 332), (43, 90))))
        self.assertFalse(Graduate(7643, "monitors", (5220, 2312), (23, 88), (6, 34)).__eq__(Graduate(4321, "watering", (765, 2222), (459, 765), (0, 0))))

    def test_read_file(self):
        self.assertEqual(read_file("test_read_file_1.csv"), ["123, computers, 12, 34, 56, 78, 9, 0"])
        self.assertEqual(read_file("test_read_file_2.csv"), ["9999, corn, 33, 33, 4, 1, 543, 765", "2394, meat, 432, 33, 123, 54, 0, 0"])
        self.assertEqual(read_file("test_read_file_3.csv"), ["8888, good, 2233, 654, 11, 33, 90, 23", "4732, qwruei, 12789, 321, 6, 7, 3, 2", "0923, iower, 0, 0, 0, 0, 0, 0"])

    def test_remove_extra_spaces(self):
        self.assertEqual(remove_extra_spaces(["4323, Engineering technology  general, 43, 33, 22, 44, 1, 1", "9932, qqq,,,, q  , 54, 64, 32, 23, 1, 1"]), ["4323,Engineering technology general,43,33,22,44,1,1", "9932,qqq,,,,q,54,64,32,23,1,1"])
        self.assertEqual(remove_extra_spaces(["4442,     fds  fff    f, 1, 2, 1, 2, 1, 2", "1111, ss    ss s,,  1, 1,   1, 1, 1, 1"]), ["4442,fds fff f,1,2,1,2,1,2", "1111,ss ss s,,1,1,1,1,1,1"])
        self.assertEqual(remove_extra_spaces(["4222,    p    p, 0,   0, 0,0,0,0", "9999, happy     sad, 23, 43, 5, 6, 1, 1"]), ["4222,p p,0,0,0,0,0,0", "9999,happy sad,23,43,5,6,1,1"])

    def test_remove_extra_commas(self):
        self.assertEqual(remove_extra_commas(["4444,,,,,,,engineering,,,,,22,,,1,1,1,32,30", "4323,engine,2,,1,2,3,4,,2,"]), ["4444,engineering,22,1,1,1,32,30", "4323,engine,2,1,2,3,4,2"])
        self.assertEqual(remove_extra_commas(["8888,hot dog,,,3,3,3,3,3,3", "1234,waffle,0,0,0,0,0,0"]), ["8888,hot dog,3,3,3,3,3,3", "1234,waffle,0,0,0,0,0,0"])
        self.assertEqual(remove_extra_commas(["7732,mouse,2,,,321,,,32,,,2,,1,1", "8934,house in cat,90,3,2,2,,,3,,,1,,,,,"]), ["7732,mouse,2,321,32,2,1,1", "8934,house in cat,90,3,2,2,3,1"])

    def test_create_division(self):
        self.assertEqual(create_division(["4444,engineering,22,1,1,1,32,30", "4323,engine,2,1,2,3,4,2,", "3800,computers"]), [Division(3800, "computers")])
        self.assertEqual(create_division(["2300,agriculture", "2222,economics,0,0,0,0,1,1", "1232,waffle,44,22,33,11,22,33"]), [Division(2300, "agriculture")])
        self.assertEqual(create_division(["2300,agriculture", "2200,economics", "1232,waffle,44,22,33,11,22,33"]), [Division(2300, "agriculture"), Division(2200, "economics")])

    def test_create_graduate(self):
        self.assertEqual(create_graduate(["4444,engineering,22,1,1,1,32,30", "4323,engine,2,1,2,3,4,2,", "3800,computers"]), [Graduate(4444, "engineering", (22, 1), (1, 1), (32, 30)), Graduate(4323, "engine", (2, 1), (2, 3), (4, 2))])
        self.assertEqual(create_graduate(["2300,agriculture", "2222,economics,0,0,0,0,1,1", "1232,waffle,44,22,33,11,22,33"]), [Graduate(2222, "economics", (0, 0), (0, 0), (1, 1)), Graduate(1232, "waffle", (44, 22), (33, 11), (22, 33))])
        self.assertEqual(create_graduate(["2300,agriculture", "2200,economics", "1232,waffle,44,22,33,11,22,33"]), [Graduate(1232, "waffle", (44, 22), (33, 11), (22, 33))])

    def test_find_total_avg(self):
        self.assertEqual(find_total_avg([Division(3800, "computers"), Division(2300, "agriculture")], [Graduate(2301, "grass", (9, 9), (1, 1), (0, 0)), Graduate(3802, "computer camera", (22, 1), (1, 1), (32, 30)), Graduate(4444, "engine", (2, 1), (2, 3), (4, 2)), Graduate(3801, "computer science", (10, 20), (30, 40), (50, 60))]), [(297, 148.5), (20, 20)])
        self.assertEqual(find_total_avg([Division(3900, "housing"), Division(2000, "electric")], [Graduate(3901, "grass", (19, 19), (1, 1), (0, 0)), Graduate(2001, "computer camera", (1, 1), (1, 1), (0, 0)), Graduate(1234, "engine", (2, 1), (2, 3), (4, 2)), Graduate(1324, "alphabet", (10, 20), (30, 40), (50, 60))]), [(40, 40), (4, 4)])
        self.assertEqual(find_total_avg([Division(3200, "speakers"), Division(1500, "fire")], [Graduate(3205, "grill", (5, 5), (5, 5), (10, 10)), Graduate(1505, "water", (10, 10), (10, 10), (10, 10)), Graduate(1510, "lid", (0, 0), (3, 3), (7, 7)), Graduate(3230, "plug", (10, 20), (30, 40), (50, 60))]), [(250, 125), (80, 40)])

    def test_find_graduate_rate(self):
        self.assertEqual(find_graduate_rate(Graduate(3802, "computer camera", (22, 1), (1, 1), (32, 30))), (55, 32))
        self.assertEqual(find_graduate_rate(Graduate(3901, "grass", (19, 19), (1, 1), (0, 0))), (20, 20))
        self.assertEqual(find_graduate_rate(Graduate(1505, "water", (10, 10), (10, 10), (10, 10))), (30, 30))

    def test_total_computer_division(self):
        self.assertEqual(total_for_computer_division("computer_test_1.csv"), 18615)
        self.assertEqual(total_for_computer_division("computer_test_2.csv"), 2059)
        self.assertEqual(total_for_computer_division("computer_test_3.csv"), 16310)

    def test_avg_female_and_male_computer_division(self):
        self.assertEqual(avg_male_female_computer([Graduate(3301, "grass", (9, 9), (1, 1), (0, 0)), Graduate(3802, "camera", (22, 1), (1, 1), (32, 30)), Graduate(3444, "computer", (2, 1), (2, 3), (4, 2)), Graduate(3801, "stuff", (10, 20), (30, 40), (50, 60))]), (8.0, 6.0))
        self.assertEqual(avg_male_female_computer([Graduate(3401, "computers", (9, 9), (1, 1), (0, 0)), Graduate(3802, "camera", (15, 2), (3, 8), (12, 40)), Graduate(3444, "computer", (6, 8), (1, 1), (0, 0)), Graduate(3801, "things", (10, 20), (30, 40), (50, 60))]), (8.5, 9.5))
        self.assertEqual(avg_male_female_computer([Graduate(3410, "computing", (11, 22), (5, 10), (5, 10)), Graduate(3102, "tabling", (199, 32), (321, 432), (12, 0)), Graduate(3411, "graphics", (100, 100), (1, 1), (9, 9)), Graduate(3402, "keys", (88, 88), (10, 10), (2, 2))]), (77.0, 84.0))

    def test_total_female_and_male_all_majors(self):
        pass

    def test_total_computer_division_divided_by_total_all_majors(self):
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
