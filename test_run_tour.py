from unittest import TestCase, main, skipIf
from runner_and_tournament import Runner, Tournament



class TournamentTest(TestCase):
    is_frozen = True # согласно заданию 12.3

    key = 0
    @classmethod
    def setUpClass(cls):
        cls.all_result = {}
        return cls.all_result

    @classmethod
    def tearDownClass(cls):
        for num_run in cls.all_result.items():
            print(num_run)

    def setUp(self):
        self.key +=1
        runner_1 = Runner('Усейн', 10)
        runner_2 = Runner('Андрей', 9)
        runner_3 = Runner('Ник', 3)
        self.list_runner = runner_1, runner_2, runner_3


    def tearDown(self):
        self.assertTrue(self.list_runner[2] == self.all_result[self.key][len(self.all_result[self.key])].name, 'ok')
        print('*' * 100)


    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_case_1(self):
        self.all_result[self.key] = Tournament(90, self.list_runner[0],self.list_runner[2]).start() # Усэйн и Ник

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_case_2(self):
        self.all_result[self.key] = Tournament(90, self.list_runner[1],self.list_runner[2]).start()

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_case_3(self):
        self.all_result[self.key] = Tournament(90, *self.list_runner).start()

if __name__ == '__main__':
    main