import unittest
import runner_test
import test_run_tour

for_test = unittest.TestSuite()
for_test.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
for_test.addTest(unittest.TestLoader().loadTestsFromTestCase(test_run_tour.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(for_test)