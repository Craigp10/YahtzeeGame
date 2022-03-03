import unittest
# import Scoring
from Scoring import Scoring

class TestScoring(unittest.TestCase):

    def test_straighScore(self):
        scoring = Scoring([2,2,3,4,5], ["One", "Two", "Three",
      "Four", "Five", "Six", "Small Straight", "Big Straight",
      "Three of A Kind","Four of A Kind","Full House",
      "Yahtzee", "Chance"])
        self.assertEqual(scoring.StraightScores(4,30), 30)
        scoring.updateDice([2,2,2,4,4])
        self.assertEqual(scoring.StraightScores(4,30), 0)
        scoring.updateDice([1,2,3,4,5])
        self.assertEqual(scoring.StraightScores(5,40), 40)
        scoring.updateDice([1,2,3,4,4])
        self.assertEqual(scoring.StraightScores(5,40), 0)
        scoring.updateDice([2,3,4,5,6])
        self.assertEqual(scoring.StraightScores(5,40), 40)

    def test_fullHouse(self):
        scoring = Scoring([2,2,3,3,3], ["One", "Two", "Three",
      "Four", "Five", "Six", "Small Straight", "Big Straight",
      "Three of A Kind","Four of A Kind","Full House",
      "Yahtzee", "Chance"])
        self.assertEqual(scoring.FullHouseScore(), 25)
        scoring.updateDice([2,2,2,4,5])
        self.assertEqual(scoring.FullHouseScore(), 0)
        scoring.updateDice([1,1,1,1,2])
        self.assertEqual(scoring.FullHouseScore(), 0)
        scoring.updateDice([2,2,4,4,4])
        self.assertEqual(scoring.FullHouseScore(), 25)

    def test_Yahtzee(self):
        scoring = Scoring([2,2,3,3,3], ["One", "Two", "Three",
      "Four", "Five", "Six", "Small Straight", "Big Straight",
      "Three of A Kind","Four of A Kind","Full House",
      "Yahtzee", "Chance"])
        self.assertEqual(scoring.CheckYahtzee(5), 0)
        scoring.updateDice([2,2,2,2,2])
        self.assertEqual(scoring.CheckYahtzee(5), 50)
        scoring.updateDice([2,2,2,2,1])
        self.assertEqual(scoring.CheckYahtzee(5), 0)

    def test_Chance(self):
        scoring = Scoring([2,2,3,3,3], ["One", "Two", "Three",
      "Four", "Five", "Six", "Small Straight", "Big Straight",
      "Three of A Kind","Four of A Kind","Full House",
      "Yahtzee", "Chance"])
        self.assertEqual(scoring.ChanceScore(), 13)
        scoring.updateDice([2,2,2,2,2])
        self.assertEqual(scoring.ChanceScore(), 10)
        scoring.updateDice([1,1,4,5,6])
        self.assertEqual(scoring.ChanceScore(), 17)
        scoring.updateDice([1])
        self.assertEqual(scoring.ChanceScore(), 1)
    
    def test_OfAKindScore(self):
        scoring = Scoring([2,3,3,3,3], ["One", "Two", "Three",
      "Four", "Five", "Six", "Small Straight", "Big Straight",
      "Three of A Kind","Four of A Kind","Full House",
      "Yahtzee", "Chance"])
        self.assertEqual(scoring.OfAKindScore(3), 9)
        scoring.updateDice([1,2,3,4,5])
        self.assertEqual(scoring.OfAKindScore(3), 0)
        scoring.updateDice([1,1,1,5,6])
        self.assertEqual(scoring.OfAKindScore(4), 0)
        scoring.updateDice([4,4,4,4,6])
        self.assertEqual(scoring.OfAKindScore(4), 16)

    def test_CheckDiceValue(self):
        scoring = Scoring([1,1,3,4,5], ["One", "Two", "Three",
      "Four", "Five", "Six", "Small Straight", "Big Straight",
      "Three of A Kind","Four of A Kind","Full House",
      "Yahtzee", "Chance"])
        self.assertEqual(scoring.CheckDiceValue(1), 2)
        self.assertEqual(scoring.CheckDiceValue(2), 0)
        self.assertEqual(scoring.CheckDiceValue(3), 3)
        self.assertEqual(scoring.CheckDiceValue(4), 4)
        self.assertEqual(scoring.CheckDiceValue(5), 5)
        self.assertEqual(scoring.CheckDiceValue(6), 0)

    def test_RemoveRepeatDice(self):
        scoring = Scoring([1,1,3,4,5], ["One", "Two", "Three",
      "Four", "Five", "Six", "Small Straight", "Big Straight",
      "Three of A Kind","Four of A Kind","Full House",
      "Yahtzee", "Chance"])
        self.assertListEqual(scoring.RemoveRepeatDice([1,1,3,4,5]), [1,3,4,5])
        self.assertListEqual(scoring.RemoveRepeatDice([1,1,1,1,1]), [1])

if __name__ == '__main__':
    unittest.main()
