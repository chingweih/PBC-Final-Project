import random


class Trust:
    def __init__(self, opponent: str, score_list: dict = None) -> None:
        """Initialize: New round of Trust Game.

        Args:
            opponent (str): 輸入本回合對手 -- ["copy_cat", "always_black", "always_coop", "coop_until_cheated", "sherlock", "copy_kitten"]

            score_list (dict, optional): 各情況分數表 -- 預設值：{ 'coop': 2, 'cheat': 3, 'opponent_cheat': -1, 'both_cheat': 0 }

        Raises:
            ValueError: 提供的對手不在清單中
        """

        # Get default score list
        if score_list is None:
            score_list = {
                "coop": 2,
                "cheat": 3,
                "opponent_cheat": -1,
                "both_cheat": 0,
            }

        # Check illegal inputs
        self.OPPONENTS_LIST = [
            "copy_cat",
            "always_black",
            "always_coop",
            "coop_until_cheated",
            "sherlock",
            "copy_kitten",
        ]
        if opponent not in self.OPPONENTS_LIST:
            raise ValueError("Opponent not in list.")

        # Initialize variables
        self.player_choice = bool
        self.player_score = 0
        self.opponent_score = 0
        self.game_count = 1
        self.player_cheat = False
        self.player_cheat_count = 0
        self.player_continous_cheat = 0
        self.OPPONENT = opponent
        self.SCORE_LIST = score_list

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
        return self.player_cheat == False

    # Sherlock: 一三四局合作、第二局欺騙後，如果玩家沒有欺騙過則欺騙，否則模仿玩家上一局選擇
    def sherlock(self) -> bool:
        if self.game_count in [1, 3, 4]:
            return True
        elif self.game_count == 2:
            return False
        else:
            return False if self.player_cheat == False else self.player_choice

    # Whatever: 隨機選擇
    def whatever(self) -> bool:
        return random.choice([True, False])

    # Copy Kitten: 模仿咪 —— 合作，直到被連續欺騙兩次
    def copy_kitten(self) -> bool:
        return self.player_continous_cheat < 2

    # Add player and opponent's score and update cheat count
    def add_points(self, player: int, opponent: int, cheat: int = 0) -> None:
        self.player_score += player
        self.opponent_score += opponent
        if cheat != 0:
            self.player_cheat = True
            self.player_cheat_count += cheat
            if self.player_cheat_count > self.player_continous_cheat:
                self.player_continous_cheat = self.player_cheat_count
        else:
            self.player_cheat_count = 0

    # Judge player and opponent's move and adjust points accordingly
    def judge_and_adjust_points(self, choice: bool, opponent_choice: bool) -> None:
        # Get socre list
        COOP, CHEAT, OPPONENT_CHEAT, BOTH_CHEAT = set(self.SCORE_LIST.values())

        # Judging
        if choice and opponent_choice:
            self.add_points(COOP, COOP)
        elif not choice and not opponent_choice:
            self.add_points(BOTH_CHEAT, BOTH_CHEAT, 1)
        elif choice:
            self.add_points(OPPONENT_CHEAT, CHEAT)
        else:
            self.add_points(CHEAT, OPPONENT_CHEAT, 1)

    def battle(self, choice: bool) -> list:
        """主對戰程式

        Args:
            choice (bool): 玩家當局選擇（布林值）

        Returns:
            list: 回傳本回合結果 -- [回合數, 玩家當局選擇, 對手當局選擇, 玩家分數, 對手分數]
        """

        # Get opponent's choice
        opponent = getattr(self, self.OPPONENT)
        opponent_choice = opponent()

        self.judge_and_adjust_points(choice, opponent_choice)

        self.player_choice = choice
        self.game_count += 1

        return [
            self.game_count - 1,
            choice,
            opponent_choice,
            self.player_score,
            self.opponent_score,
        ]

    def final_score(self) -> list:
        """回合結束後，提供分數

        Returns:
            list: 回傳玩家分、對手分與總分 -- [玩家分, 對手分, 總分]
        """

        return [
            self.player_score,
            self.opponent_score,
            self.player_score + self.opponent_score,
        ]


# Testing
def main():
    get = Trust("copy_cat")
    opponents = get.OPPONENTS_LIST

    for opponent in opponents:
        game = Trust(opponent)
        test_list = [
            random.choice([True, False]),
            random.choice([True, False]),
            random.choice([True, False]),
            random.choice([True, False]),
            random.choice([True, False]),
        ]
        for test_data in test_list:
            print(opponent, game.battle(test_data))
        print(game.final_score())
    
    game_count, player_choice, opponent_choice, player_score, opponent_score = get.battle(True)
    print(game_count, player_choice, opponent_choice, player_score, opponent_score)


if __name__ == "__main__":
    main()
