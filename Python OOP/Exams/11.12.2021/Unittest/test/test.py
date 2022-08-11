from project.team import Team
import unittest


class TeamTest(unittest.TestCase):
    NAME = 'Team'

    def setUp(self):
        self.team = Team(self.NAME)

    def test__init(self):
        self.assertEqual(self.NAME, self.team.name)
        self.assertEqual({}, self.team.members)

        self.team.members = {'John': 34, 'Kris': 21}
        self.assertEqual({'John': 34, 'Kris': 21}, self.team.members)

        self.team.members = {12: 2, 3: 'K'}
        self.assertEqual({12: 2, 3: 'K'}, self.team.members)

    def test__name_property(self):
        result = self.team.name
        self.assertEqual(self.NAME, result)
        self.team.name = 'BestTEAM'
        self.assertEqual('BestTEAM', self.team.name)

        with self.assertRaises(ValueError) as error:
            self.team.name = ''
        self.assertIsNotNone(error.exception)
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.team.name = ' '
        self.assertIsNotNone(error.exception)
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.team.name = 'a1'
        self.assertIsNotNone(error.exception)
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.team.name = 'team_1'
        self.assertIsNotNone(error.exception)
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.team.name = 'Te AM'
        self.assertIsNotNone(error.exception)
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.team.name = '0'
        self.assertIsNotNone(error.exception)
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.team.name = '!?'
        self.assertIsNotNone(error.exception)
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test__add_member__no_params_passed(self):
        result = self.team.add_member()
        self.assertEqual("Successfully added: ", result)

    def test__add_member__one_passed(self):
        result = self.team.add_member(**{'Tom': 12})
        self.assertEqual("Successfully added: Tom", result)

    def test__add_member(self):
        name_age = {'Bob': 13, 'Lilly': 90, 'Nick': 23}
        result = self.team.add_member(**name_age)
        self.assertEqual("Successfully added: Bob, Lilly, Nick", result)
        self.assertEqual({'Bob': 13, 'Lilly': 90, 'Nick': 23}, self.team.members)

    def test__add_member__wrong_params(self):
        name_age = {'tom': 'anna', '_0': 'e', 'k_': 23}
        result = self.team.add_member(**name_age)
        self.assertEqual("Successfully added: tom, _0, k_", result)

        name_age = {0: 'anna', 12: 'e', 'k_': 23}
        with self.assertRaises(TypeError) as error:
            self.team.add_member(**name_age)
        self.assertIsNotNone(error.exception)

    def test__remove_member__name_in_members(self):
        self.team.add_member(**{'Nina':23})
        result = self.team.remove_member('Nina')
        self.assertEqual("Member Nina removed", result)

    def test__remove_member__name_not_in_members(self):
        result = self.team.remove_member('Bob')
        self.assertEqual("Member with name Bob does not exist", result)

        self.team.add_member(**{'Nina': 23})
        result = self.team.remove_member('Mike')
        self.assertEqual("Member with name Mike does not exist", result)

    def test__gt_expect_error(self):
        with self.assertRaises(TypeError) as error:
            team = Team()
        self.assertIsNotNone(error.exception)

        with self.assertRaises(TypeError) as error:
            team = Team()
            result = self.team.__gt__()
        self.assertIsNotNone(error.exception)

    def test__gt(self):
        team = Team("team")
        team.add_member(**{"Josh": 45, 'Clark': 96, 'Sid': 78})
        self.team.add_member(**{'Lorrie': 4, 'Steph': 23})
        result = self.team.__gt__(team)
        self.assertFalse(result)

        team = Team("team")
        team.add_member(**{"Josh": 45})
        self.team.add_member(**{'Lorrie': 4, 'Steph': 23})
        result = self.team.__gt__(team)
        self.assertTrue(result)

    def test__len(self):
        self.assertEqual(0, self.team.__len__())

        self.team.add_member(**{'Bob': 13, 'Lilly': 90, 'Nick': 23})
        self.assertEqual(3, self.team.__len__())

        self.team.add_member(**{'Bob': 13, 'Mike': 90, 'Dan': 23})
        self.assertEqual(5, self.team.__len__())

    def test__add(self):
        team = Team("team")
        team.add_member(**{"Josh":45, 'Clark':96})
        self.team.add_member(**{'Lorrie':4, 'Steph':23})
        result = self.team.__add__(team)
        self.assertEqual(f'{self.NAME}team', result.name)
        self.assertEqual({'Lorrie':4, 'Steph':23, "Josh":45,'Clark':96}, result.members)

    def test__str(self):
        result = self.team.__str__()
        expected = 'Team name: Team'
        self.assertEqual(result, expected)

        self.team.add_member(**{'Bob': 13, 'Lilly': 90, 'Nick': 23})
        result = self.team.__str__()
        expected = f"Team name: Team\nMember: Lilly - 90-years old\n" \
                   f"Member: Nick - 23-years old\nMember: Bob - 13-years old"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
