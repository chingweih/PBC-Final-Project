# PBC Final Project —— 信任遊戲

## Trust 模組

### 開啟新回合

宣告一個變數，存放 Trust 物件，並提供這局對戰的人物（字串，以下清單其中一個）
```python
["copy_cat", "always_black", "always_coop", "coop_until_cheated", "sherlock", "copy_kitten"]
```

此外若有需要調整配分方式，也可以額外傳入分數字典，格式如下預設值：

```python
{ 'coop': 2, 'cheat': 3, 'opponent_cheat': -1, 'both_cheat': 0 }
```

範例：

```python
game = Trust("copy_cat")
```

### 對戰

使用上面定義好的物件，可以呼叫 Trust.battle 函數，傳入本次玩家選擇（True/False），並得到回傳的本局結果（清單，如下）

```python
[回合數, 玩家當局選擇, 對手當局選擇, 玩家分數, 對手分數]
```

範例：

```python
result = game.battle(True) # [1, True, True, 2, 2]
```

每一次呼叫 Trust.battle 函數，就會開啟新的對戰，
即如果要對戰五次，就呼叫五次函數。

### 取得最終成績
