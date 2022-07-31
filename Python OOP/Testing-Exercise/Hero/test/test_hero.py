import unittest
from unittest import TestCase
from project.hero import Hero


class HeroTest(TestCase):
    USERNAME = "hero"
    LEVEL = 100
    HEALTH = 1000.00
    DAMAGE = 15.5

    def setUp(self):
        self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test__init(self):
        self.assertEqual(self.USERNAME, self.hero.username)
        self.assertEqual(self.LEVEL, self.hero.level)
        self.assertEqual(self.HEALTH, self.hero.health)
        self.assertEqual(self.DAMAGE, self.hero.damage)

    def test__str(self):
        result = self.hero.__str__()
        expected_result = f"Hero {self.USERNAME}: {self.LEVEL} lvl\n" \
               f"Health: {self.HEALTH}\n" \
               f"Damage: {self.DAMAGE}\n"
        self.assertEqual(expected_result, result)

    def test__battle__invalid_enemy(self):
        enemy = self.hero
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertIsNotNone(ex)

    def test__battle__not_enough_health(self):
        self.hero.health = -9
        enemy = Hero("enemy", 90, 120, 20.9)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertIsNotNone(ex)

    def test__battle__enemy_health_not_enough(self):
        enemy = Hero("enemy", 90, 0, 20.9)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertIsNotNone(ex)

    def test__battle__draw(self):
        enemy = Hero("enemy", 90, 1000, 15.5)
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test__battle_win(self):
        enemy = Hero("enemy", 10, 60, 13.9)
        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)

    def test__battle__lose(self):
        enemy = Hero("enemy", 190, 9000, 20.9)
        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)


if __name__ == "__main__":
    unittest.main()
