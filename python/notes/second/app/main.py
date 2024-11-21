from dice.entity.dice import Dice
from dice.repository.dice_repository_impl import DiceRepositoryImpl

print("Our Second Class")

dice = Dice()
dice.rollDice()
dice.printResult()

diceRepository = DiceRepositoryImpl.getInstance()
print(f"문제 없이 실행 되니?: {diceRepository}")

diceRepository2 = DiceRepositoryImpl.getInstance()
print(f"diceRepository2: {diceRepository2}")
diceRepository3 = DiceRepositoryImpl.getInstance()
print(f"diceRepository3: {diceRepository3}")