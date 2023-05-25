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
