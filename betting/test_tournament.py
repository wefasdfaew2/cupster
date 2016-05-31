import unittest
from hamcrest import *
from tournament import *


class TestTournament(unittest.TestCase):

    def init(self, toml):
        self.cup = Tournament()
        self.cup.load(toml)

    def test_create_empty_Tournament(self):
        tr = Tournament()
        assert_that(tr, instance_of(Tournament))

    def test_load_returns_dict(self):
        self.init('')
        actual = self.cup.get_config()
        assert_that(actual, instance_of(dict))

    def test_load_returns_config(self):
        toml = 'name = "foo"\ngroups = [ ["op", "oop"], ["opo", "ioi"] ]'
        self.init(toml)
        config = self.cup.get_config()
        assert_that(config['name'], equal_to('foo'))

    def test_get_name(self):
        toml = 'name = "VM 2014"'
        self.init(toml)
        assert_that(self.cup.get_name(), is_(equal_to('VM 2014')))

    def test_get_number_of_groups(self):
        toml = 'name = "foo"\ngroups = [ ["op", "oop"], ["opo", "ioi"] ]'
        self.init(toml)
        assert_that(self.cup.get_number_of_groups(), is_(equal_to(2)))

    def test_match_score(self):
        match = ['brasil', 'kroatia']
        self.init('')
        assert_that(self.cup.match_score(match, 'h'), is_(equal_to(['brasil', 'brasil', 'brasil'])))
        assert_that(self.cup.match_score(match, 'b'), is_(equal_to(['kroatia', 'kroatia', 'kroatia'])))
        assert_that(self.cup.match_score(match, 'u'), is_(equal_to(['brasil', 'kroatia'])))

    def test_tally_group_results(self):
        self.init('')
        winners = ['brasil', 'brasil', 'brasil', 'brasil', 'england', 'england',
                   'england', 'sweden', 'sweden', 'cuba']
        first, second, third = self.cup.tally_group_results(winners)
        assert_that(first, is_(equal_to('brasil')))
        assert_that(second, is_(equal_to('england')))
        assert_that(third, is_(equal_to('sweden')))

    def test_tally_group_results_when_draw(self):
        self.init('')
        winners = ['brasil', 'brasil', 'brasil', 'england', 'england',
                   'england', 'sweden', 'sweden', 'cuba']
        first, second, third = self.cup.tally_group_results(winners)
        assert_that(first, is_(tuple), 'first')
        assert_that(second, is_(tuple), 'second')
        assert_that(third, is_(equal_to('sweden')), 'third')

        winners = ['brasil', 'brasil', 'brasil', 'brasil', 'england', 'england',
                   'sweden', 'sweden', 'cuba']
        first, second, third = self.cup.tally_group_results(winners)
        assert_that(first, is_(equal_to('brasil')))
        assert_that(second, is_(tuple))
        assert_that(third, is_(tuple), 'third')

    def test_get_non_qualifiers(self):
        self.init('')
        points = ['brasil', 'brasil', 'brasil', 'england', 'england',
                   'england', 'sweden', 'sweden', 'cuba']
        winner = 'brasil'
        runnerUp = 'england'
        remaining =['sweden', 'sweden', 'cuba']
        actual = self.cup.get_non_qualifiers(points, winner, runnerUp)
        assert_that(actual, is_(equal_to(remaining)))

    def test_get_top_four(self):
        self.init('')
        points = ['brasil', 'brasil', 'brasil', 'england', 'england',
                   'england', 'sweden', 'sweden', 'cuba', 'lithuania',
                   'italy', 'italy', 'italy', 'italy']
        actual = self.cup.get_top_four(points)
        assert_that(actual, has_items('italy', 'brasil', 'england', 'sweden'))

if __name__ == '__main__':
    unittest.main()
