import random


class Trust:
    def __init__(self, opponent: str) -> None:
        opponents = ["copy_cat", "always_black",
                     "always_coop", "coop_until_cheated", "sherlock"]
        if opponent not in opponents:
            raise ValueError('Opponent not in list.')
        self.player_choice = bool
        self.player_score = 0
        self.opponent_score = 0
        self.game_count = 1
        self.player_cheat = 0
        self.opponent = opponent

    def add_points(self, player, opponent, cheat=0) -> None:
        self.player_score += player
        self.opponent_score += opponent
        self.player_cheat += cheat

    def copy_cat(self) -> bool:
        return True if self.game_count == 1 else self.player_choice

    def always_black(self) -> bool:
        return False

    def always_coop(self) -> bool:
        return True

    def coop_until_cheated(self) -> bool:
        return self.player_cheat < 1

    def sherlock(self) -> bool:
        if self.game_count in [1, 3, 4]:
            return True
        elif self.game_count == 2:
            return False
        else:
            return False if self.player_cheat == 0 else self.player_choice

    def battle(self, choice: bool) -> list:
        opponent_glossary = {
            "copy_cat": self.copy_cat(),
            "always_black": self.always_black(),
            "always_coop": self.always_coop(),
            "coop_until_cheated": self.coop_until_cheated(),
            "sherlock": self.sherlock()
        }
        opponent_choice = opponent_glossary[self.opponent]

        if choice and opponent_choice:
            self.add_points(2, 2)
        elif not choice and not opponent_choice:
            self.add_points(0, 0, 1)
        elif choice:
            self.add_points(-1, 3)
        else:
            self.add_points(3, -1, 1)

        self.player_choice = choice
        self.game_count += 1

        return [self.game_count - 1, choice, opponent_choice, self.player_score, self.opponent_score]


def testing(opponent):
    game = Trust(opponent)
    test_list = [random.choice([True, False]), random.choice([True, False]), random.choice(
        [True, False]), random.choice([True, False]), random.choice([True, False])]

    for test_data in test_list:
        print(opponent, game.battle(test_data))


if __name__ == '__main__':
    opponents = ["copy_cat", "always_black",
                 "always_coop", "coop_until_cheated", "sherlock"]
    for opponent in opponents:
        testing(opponent)
