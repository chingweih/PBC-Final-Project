import random


class Trust:

    # Initialize: 輸入本回合對手 -- ["copy_cat", "always_black", "always_coop", "coop_until_cheated", "sherlock", "whatever"]
    def __init__(self, opponent: str) -> None:

        # Check illegal inputs
        self.opponents_list = ["copy_cat", "always_black",
                               "always_coop", "coop_until_cheated", "sherlock", "whatever"]
        if opponent not in self.opponents_list:
            raise ValueError('Opponent not in list.')

        # Initialize variables
        self.player_choice = bool
        self.player_score = 0
        self.opponent_score = 0
        self.game_count = 1
        self.player_cheat = 0
        self.opponent = opponent

    # Add player and opponent's score and update cheat count
    def add_points(self, player: int, opponent: int, cheat: int = 0) -> None:
        self.player_score += player
        self.opponent_score += opponent
        self.player_cheat += cheat

    # Opponent algorithms (bool): 合作 - True; 欺騙 - False
    # Copy Cat: 第一局合作，後模仿玩家上一局選擇
    def copy_cat(self) -> bool:
        return True if self.game_count == 1 else self.player_choice

    # Always Black: 永遠欺騙
    def always_black(self) -> bool:
        return False

    # Always Coop: 永遠合作
    def always_coop(self) -> bool:
        return True

    # Coop Until Cheated: 先合作，被欺騙過後騙到底
    def coop_until_cheated(self) -> bool:
        return self.player_cheat < 1

    # Sherlock: 一三四局合作、第二局欺騙後，如果玩家沒有欺騙過則欺騙，否則模仿玩家上一局選擇
    def sherlock(self) -> bool:
        if self.game_count in [1, 3, 4]:
            return True
        elif self.game_count == 2:
            return False
        else:
            return False if self.player_cheat == 0 else self.player_choice

    # Whatever: 隨機選擇
    def whatever(self) -> bool:
        return random.choice([True, False])

    # 主對戰程式：輸入玩家當局選擇（布林值）
    # Return List = [回合數, 玩家當局選擇, 對手當局選擇, 玩家分數, 對手分數]
    def battle(self, choice: bool) -> list:

        # Get opponent's choice
        opponent = getattr(self, self.opponent)
        opponent_choice = opponent()

        # Check results and add points accordingly
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

    def final_score(self) -> list:
        return [self.player_score, self.opponent_score, self.player_score + self.opponent_score]


def main():
    get = Trust("copy_cat")
    opponents = get.opponents_list

    for opponent in opponents:
        game = Trust(opponent)
        test_list = [random.choice([True, False]), random.choice([True, False]), random.choice(
            [True, False]), random.choice([True, False]), random.choice([True, False])]
        for test_data in test_list:
            print(opponent, game.battle(test_data))
        print(game.final_score())


if __name__ == '__main__':
    main()
