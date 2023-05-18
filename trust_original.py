# 原始檔案

import random
import time
player_decide = str()
player_score = 0
pc_score = 0
total_score = 0
game_count = 1
cheat_count = 0

# 與新的對手對局時，重新定義變數


def new_round():
    global player_decide, player_score, pc_score, game_count, cheat_count
    player_decide = str()
    player_score = 0
    pc_score = 0
    game_count = 1
    cheat_count = 0

# 讓使用者決定是否要與對方合作並判斷結果


def coop_or_cheat(pc_decide):
    global player_score, pc_score, player_decide, cheat_count
    player_decide = str(input("要與對方合作(y)或是欺騙(n)？"))
    if player_decide == "y" and pc_decide == "y":
        player_score += 2
        pc_score += 2
        print("...")
        time.sleep(0.5)
        print("你和對方都選擇了「合作」，你們將獲得兩分")
        time.sleep(0.5)
        print("目前比數為 " + str(player_score) + "：" + str(pc_score))
        print("---")
    elif player_decide == "n" and pc_decide == "n":
        player_score += 0
        pc_score += 0
        cheat_count = 1
        print("...")
        time.sleep(0.5)
        print("你和對方都選擇了「欺騙」，你們都不會獲得分數")
        time.sleep(0.5)
        print("目前比數為 " + str(player_score) + "：" + str(pc_score))
        print("---")
    elif player_decide == "y" and pc_decide == "n":
        player_score += -1
        pc_score += 3
        print("...")
        time.sleep(0.5)
        print("對方選擇了「欺騙」，他將會獲得三分")
        time.sleep(0.5)
        print("目前比數為 " + str(player_score) + "：" + str(pc_score))
        print("---")
    elif player_decide == "n" and pc_decide == "y":
        player_score += 3
        pc_score += -1
        cheat_count = 1
        print("...")
        time.sleep(0.5)
        print("對方選擇了「合作」，你將獨得三分")
        time.sleep(0.5)
        print("目前比數為 " + str(player_score) + "：" + str(pc_score))
        print("---")
    else:
        print("請重新輸入（y或n）")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        coop_or_cheat(pc_decide)

# 模仿貓_判斷程式


def copy_cat():
    global player_decide, game_count
    return "y" if game_count == 1 else player_decide

# 黑到底_判斷程式


def always_black():
    return ("n")

# 紅櫻仔_判斷程式


def always_coop():
    return ("y")

# 牛文聰_判斷程式


def coop_untill_cheated():
    global game_count, cheat_count
    if game_count == 1 or cheat_count == 0:
        return ("y")
    # 如果先前被欺騙過，則會一直欺騙
    elif cheat_count == 1:
        return ("n")

# 福爾摩星兒_判斷程式


def sherlock():
    global game_count, cheat_count, player_decide
    # 第一、三、四回合「合作」
    if game_count in [1, 3, 4]:
        return ("y")
    elif game_count == 2:
        return ("n")
    else:
        # 若沒有被欺騙過，則騙到底
        return "n" if cheat_count == 0 else player_decide

# 主要對局程式


def battle_with(player):
    global player_score, pc_score, total_score, player_decide, cheat_count, game_count
    for _ in range(random.randint(4, 7)):
        if player == "copy_cat":
            coop_or_cheat(copy_cat())
        elif player == "always_black":
            coop_or_cheat(always_black())
        elif player == "always_coop":
            coop_or_cheat(always_coop())
        elif player == "coop_untill_cheated":
            coop_or_cheat(coop_untill_cheated())
        elif player == "sherlock":
            coop_or_cheat(sherlock())
        game_count += 1
    total_score += player_score
    new_round()
    print("回合結束！")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print(f"你目前的總分是：{str(total_score)} 分")
    print("---")

# 遊戲介紹


def intro():
    print("《信任的演化》遊戲")
    print("---")
    print("在接下來的遊戲中，你需要選擇與對方「合作」，或者「欺騙」對方")
    time.sleep(0.5)
    print("若你們雙方都選擇「合作」，你們都可以獲得兩分")
    time.sleep(0.1)
    print("但若你們其中有一方選擇了「欺騙」，欺騙的那一方將可以獲得三分，另一人則會被扣一分")
    print("...")
    time.sleep(0.5)
    print("接下來，你將與五名不同的玩家進行遊戲，每個人都有他們自己的「遊戲策略」。")
    time.sleep(0.1)
    print("每位玩家會與你對局 3 到 7 步，你並不知道哪一步是這局的最後一步。")
    time.sleep(0.1)
    print("你可以相信他們嗎？或者說...他們可以相信你嗎？")
    print("...")
    time.sleep(0.5)
    print("遊戲開始！")
    print("---")

# 通知玩家第幾局


def round_display(round):
    print(f"第{round}回合")
    print(f"對手：玩家{round}")
    print("...")
    time.sleep(0.5)

# 結束資訊


def outro():
    print("感謝遊玩！ \n遊戲原作及詳細資訊：https://ncase.me/trust/")

# 遊戲結束，給予分數並介紹角色


def game_over():
    global total_score
    a = str()
    print("遊戲結束！")
    print(f"你的總分是：{str(total_score)} 分")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    end = input("是否要查看各玩家的策略？（y/n）")
    if end == "y":
        print("玩家一：模仿貓 \n哈囉！我第一次會出「合作」。 \n之後，我會選和你前一步一模一樣的選擇喔喵～")
        a = input("按下 Enter 繼續查看下個玩家的策略...")
        print("---")
        time.sleep(0.5)
        print("玩家二：黑到底 \n絕不合作，這是弱肉強食的世界。")
        a = input("按下 Enter 繼續查看下個玩家的策略...")
        print("---")
        time.sleep(0.5)
        print("玩家三：紅嬰仔 \n我們大家做朋友吧！ <3")
        a = input("按下 Enter 繼續查看下個玩家的策略...")
        print("---")
        time.sleep(0.5)
        print("玩家四：牛文聰 \n我哞佮意輸的感覺。 \n我會先給你面子「合作」，但是最好不要用「欺騙」惹我生氣， \n我袂爽就會想要報仇！")
        a = input("按下 Enter 繼續查看下個玩家的策略...")
        print("---")
        time.sleep(0.5)
        print("玩家五：福爾摩星兒 \n分析人是我的特長。 \n遊戲開始我會「合作」、「欺騙」、「合作」、「合作」。 \n如果你反過來欺騙我，我就會像模仿貓那樣跟著你出牌。 \n如果你一直不騙回來，那我就會像黑到底那樣榨乾你。 \n這是常識啊，我親愛的花生兒～")
        a = input("按下 Enter 結束遊戲...")
        print("---")
        time.sleep(0.5)
    outro()


intro()
round_display("一")
battle_with("copy_cat")
round_display("二")
battle_with("always_black")
round_display("三")
battle_with("always_coop")
round_display("四")
battle_with("coop_untill_cheated")
round_display("五")
battle_with("sherlock")
game_over()
