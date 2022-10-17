'''
通过Python面向对象实现八数码问题求解
date: 2022-10-17
author: 史胤隆
--------------------------------------------
class box(value, history): 八数码问题处理的九宫格对象 | box object for 8-puzzle problem
    用于实例处理八数码问题, 支持格式化打印. | used to process 8-puzzle problem. format print supported.
    box.value: 九宫格对象的值 | value of box object
    box.history: 九宫格对象的移动历史 | history of box object
    box.up(): 向上移牌 | move up
    box.down(): 向下移牌 | move down
    box.left(): 向左移牌 | move left
    box.right(): 向右移牌 | move right
    box.able: 返回可用的移动方法 | return able move method
    box.expand(): 拓展下一层 | expand next layer
'''


class box:
    '''
    八数码问题处理的九宫格对象 | box object for 8-puzzle problem
    >> value: 九宫格对象的值 | value of box object
    >> history: 九宫格对象的移动历史 | history of box object
    '''

    def __init__(self, value: list, history: str = '-> ') -> None:
        if len(value) != 9 or set(value) != {0, 1, 2, 3, 4, 5, 6, 7, 8}:
            raise ValueError(
                '输入值必须是由 0-8 组成的 9 位整数列表 | value must be a list of 9 int in 0-8')
        self._value = value
        self._history = history
        self._zero = self._value.index(0)

    def __str__(self):
        '九宫格对象的格式化输出 | formatted output of box object'
        return 'moved via {}:\n[ {} {} {}\n  {} {} {}\n  {} {} {} ]'.format(self._history, *[i if i != 0 else '*' for i in self._value])

    @property
    def value(self):
        '九宫格对象的值 | value of box object'
        return self._value

    @property
    def history(self):
        '九宫格对象的移动历史 | history of box object'
        return self._history

    def up(self) -> 'box':
        '向上移牌 | move up'
        if self._zero in (6, 7, 8):
            raise ValueError('不能向上移牌 | cannot move up')
        value = self._value.copy()
        value[self._zero], value[self._zero +
                                 3] = value[self._zero + 3], value[self._zero]
        return box(value, self._history + 'U')

    def down(self) -> 'box':
        '向下移牌 | move down'
        if self._zero in (0, 1, 2):
            raise ValueError('不能向下移牌 | cannot move down')
        value = self._value.copy()
        value[self._zero], value[self._zero -
                                 3] = value[self._zero - 3], value[self._zero]
        return box(value, self._history + 'D')

    def left(self) -> 'box':
        '向左移牌 | move left'
        if self._zero in (2, 5, 8):
            raise ValueError('不能向左移牌 | cannot move left')
        value = self._value.copy()
        value[self._zero], value[self._zero +
                                 1] = value[self._zero + 1], value[self._zero]
        return box(value, self._history + 'L')

    def right(self) -> 'box':
        '向右移牌 | move right'
        if self._zero in (0, 3, 6):
            raise ValueError('不能向右移牌 | cannot move right')
        value = self._value.copy()
        value[self._zero], value[self._zero -
                                 1] = value[self._zero - 1], value[self._zero]
        return box(value, self._history + 'R')

    @property
    def able(self) -> list:
        '返回可用的移动方法 | return able move method'
        able = []
        if self._zero not in (6, 7, 8):
            able.append(self.up)
        if self._zero not in (0, 1, 2):
            able.append(self.down)
        if self._zero not in (2, 5, 8):
            able.append(self.left)
        if self._zero not in (0, 3, 6):
            able.append(self.right)
        return able

    def expand(self) -> list:
        '拓展下一层 | expand next layer'
        return [i() for i in self.able]


if __name__ == '__main__':
    pass

if __name__ == 'eightpuzzle':
    pass
