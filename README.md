Traceback (most recent call last):
  File "/Users/zeeldarji/Desktop/python files/game/main.py", line 41, in <module>
    game.runnin()
  File "/Users/zeeldarji/Desktop/python files/game/main.py", line 35, in runnin
    self.group.movin()
  File "/Users/zeeldarji/Desktop/python files/game/main.py", line 13, in movin
    self.offset.x = Player.rect.centerx-625
                    ^^^^^^^^^^^
AttributeError: type object 'Player' has no attribute 'rect'
