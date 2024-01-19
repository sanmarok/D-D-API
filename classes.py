import random


class dungeon_master():
    def __init__(self) -> None:
        pass

    def dice_roll(self):
        dice_result = random.randint(1,20)
        return dice_result

    def rolls(self, rolls_number):
        result_rolls = {}
        
        for roll in range(rolls_number):
            key = f"roll {roll+1}"
            result_rolls[key] = self.dice_roll()

        return result_rolls