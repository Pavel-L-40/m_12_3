from unittest import TestCase, main, skipIf
import runner


class RunnerTest(TestCase):
    is_frozen = False
    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_runner = runner.Runner('test runner')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_runner = runner.Runner('test runner')
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_first = runner.Runner('first')
        runner_second = runner.Runner('second')
        for _ in range(10):
            runner_first.run()
            runner_second.walk()
        self.assertNotEqual(runner_first.distance, runner_second.distance)


if __name__ == '__main__':
    main()