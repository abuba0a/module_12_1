import Runner as runner
from unittest import TestCase


class RunnerTest(TestCase):

    def test_walk(self):
        runner_1 = runner.Runner('1')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = runner.Runner('2')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_1 = runner.Runner('1')
        runner_2 = runner.Runner('2')
        for i in range(10):
            runner_1.run()
        for i in range(10):
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


RunnerTest()
