# PBC Final Project —— 傑哥是你？！

Windows

[![Windows 下載](https://img.shields.io/github/downloads/chingweih/PBC-Final-Project/latest/Trust.exe.svg)](https://github.com/chingweih/pbc-final-project/release/latest/download/Trust.exe)

macOS

[![macOS 下載](https://img.shields.io/github/downloads/chingweih/PBC-Final-Project/latest/Trust.zip.svg)](https://github.com/chingweih/pbc-final-project/release/latest/download/Trust.zip)

---

## 開發與使用

Python 3.6+

使用以下指令安裝所需的模組：

```properties
pip install -r requirements.txt
```

創建執行檔（或是直接到 [Release](https://github.com/chingweih/PBC-Final-Project/releases) 下載）：

```properties
# macOS
pyinstaller --clean --onefile -w --add-data "assets:./assets" -n "Trust" -i assets/icons/icon.icns path_to_app.py

# Windows
pyinstaller --clean --onefile -w --add-data "assets;./assets" -n "Trust" -i assets/icons/icon.ico path_to_app.py
```

## 模組：Trust

### 開啟新回合 — `Trust(opponent, [score_list])`

宣告一個變數，存放 Trust 物件，並提供這局對戰的人物（字串，以下清單其中一個）

```python
[
  "copy_cat",
  "always_black",
  "always_coop",
  "coop_until_cheated",
  "sherlock",
  "copy_kitten"
]
```

此外若有需要調整配分方式，也可以額外傳入分數字典，格式如下預設值：

```python
{
  'coop': 2,
  'cheat': 3,
  'opponent_cheat': -1,
  'both_cheat': 0,
}
```

---

開啟新回合 —— 一般情況範例：

```python
game = Trust("copy_cat")
```

或是需要更改配分表時：

```python
score_list = {
  'coop': 5,
  'cheat': 10,
  'opponent_cheat': -5,
  'both_cheat': 0,
}

game = Trust("always_black", score_list)
```

---

### 對戰 — `Trust.battle(choice) -> list`

使用上面定義好的物件，可以呼叫 Trust.battle 函數，傳入本次玩家選擇（True/False），並得到回傳的本局結果（清單，如下）

```python
[回合數, 玩家當局選擇, 對手當局選擇, 玩家分數, 對手分數]
```

---

對戰 —— 範例：

```python
result = game.battle(True) # [1, True, True, 2, 2]
```

也可以直接解構清單變成單獨的變數：

```python
game_count, player_choice, opponent_choice, player_score, opponent_score = game.battle(True)

print(game_count, player_choice, opponent_choice, player_score, opponent_score)
# 1 True True 2 2
```

每一次呼叫 Trust.battle 函數，就會開啟新的對戰，
即如果要對戰五次，就呼叫五次函數。

---

### 取得最終成績 — `Trust.final_score() -> list`

在所有對戰都結束之後，可以呼叫 Trust.final_score 取得最終成績（清單，如下）

```python
[玩家分, 對手分, 總分]
```

---

取得最終成績 —— 範例：

```python
score = game.final_score() # [10, 10, 20]
```

同樣可以解構清單：

```python
player_final, opponent_final, total = game.final_score()

print(player_final, opponent_final, total)
# 10 10 20
```
