"""
通过Python面向对象实现八数码问题求解
--------------------------------------------
date: 2022-10-17
author: 史文朔 | Vincent SHI
--------------------------------------------
"""
import warnings


class Box:
    """
    Box(value: list, history: str = '-> ') -> 'Box'

    八数码问题处理的九宫格对象 | Box object for 8-puzzle problem
    >> value: 九宫格对象的值 | value of Box object
    >> history: 九宫格对象的移动历史 | history of Box object
    << 实例化新的九宫格对象 | new Box object
    """

    def __init__(self, value: list, history: str = '-> ') -> None:
        if len(value) != 9 or set(value) != {0, 1, 2, 3, 4, 5, 6, 7, 8}:
            raise ValueError(
                '输入值必须是由 0-8 组成的 9 位整数列表 | value must be a list of 9 int in 0-8')
        if history[:3] == '-> ':
            history = history[3:]
        elif history[:2] == '->':
            history = history[2:]
        if set(history) - {'U', 'D', 'L', 'R'}:
            raise ValueError("历史记录只能含有 'U', 'D', 'L' 和 'R' | history can only contain 'U', 'D', 'L' and 'R'")
        self._value = value
        self._history = '-> ' + history
        self._zero = self._value.index(0)

    def __str__(self):
        """九宫格对象的格式化输出 | formatted output of Box object"""
        return 'moved via {}:\n[ {} {} {}\n  {} {} {}\n  {} {} {} ]\n'.format(
            self._history, *[i if i != 0 else '*' for i in self._value])

    @property
    def value(self) -> list:
        """
        'Box'.value -> list

        九宫格对象的值 | value of Box object
        """
        return self._value

    def set_value(self, value: list) -> None:
        """
        'Box'.set_value(value: list) -> None

        修改当前九宫格对象的值而不改变其历史记录 | change value of Box object without change history
        >> value: 新的值 | new value
        """
        if len(value) != 9 or set(value) != {0, 1, 2, 3, 4, 5, 6, 7, 8}:
            raise ValueError(
                '输入值必须是由 0-8 组成的 9 位整数列表 | value must be a list of 9 int in 0-8')
        self._value = value
        self._zero = self._value.index(0)
        # 警告: set_value 方法不会改变历史记录 | Warning: set_value method will not change history
        warnings.warn('set_value 方法不会改变历史记录 | set_value method will not change history', SyntaxWarning)

    @property
    def history(self) -> str:
        """
        'Box'.history -> str

        九宫格对象的移动历史 | history of Box object
        """
        return self._history

    def add_history(self, history: str) -> None:
        """
        'Box'.add_history(history: str) -> None

        添加历史记录而不改变九宫格对象的值 | add history without change value of Box object
        >> history: 新的历史记录 | new history
        """
        if set(history) - {'U', 'D', 'L', 'R'}:
            raise ValueError("历史记录只能含有 'U', 'D', 'L' 和 'R' | history can only contain 'U', 'D', 'L' and 'R'")
        self._history += history
        # 警告: add_history 方法不会改变九宫格对象的值 | Warning: add_history method will not change value of Box object
        warnings.warn(
            'add_history 方法不会改变九宫格对象的值 | add_history method will not change value of Box object', SyntaxWarning)

    def del_history(self, length: int = 1) -> str:
        """
        'Box'.del_history(length: int = 1) -> str

        删除历史记录而不改变九宫格对象的值 | delete history without change value of Box object
        >> length: 删除的长度 | length of deleted history
        << 返回被删除的历史记录 | return deleted history
        """
        if length < 1:
            raise ValueError('length 必须大于 0 | length must be greater than 0')
        if length > len(self._history) - 3:
            raise ValueError('length 不能大于历史记录长度 | length cannot be greater than length of history')
        deleted_history = self._history[-length:]
        self._history = self._history[:-length]
        # 警告: del_history 方法不会改变九宫格对象的值 | Warning: del_history method will not change value of Box object
        warnings.warn(
            'del_history 方法不会改变九宫格对象的值 | del_history method will not change value of Box object', SyntaxWarning)
        return deleted_history

    def up(self) -> 'Box':
        """
        'Box'.up() -> 'Box'

        向上移牌 | move up
        << 返回新的九宫格对象 | return new Box object
        """
        if self._zero in (6, 7, 8):
            raise ValueError('不能向上移牌 | cannot move up')
        value = self._value.copy()
        value[self._zero], value[self._zero +
                                 3] = value[self._zero + 3], value[self._zero]
        return Box(value, self._history + 'U')

    def down(self) -> 'Box':
        """
        'Box'.down() -> 'Box'

        向下移牌 | move down
        << 返回新的九宫格对象 | return new Box object
        """
        if self._zero in (0, 1, 2):
            raise ValueError('不能向下移牌 | cannot move down')
        value = self._value.copy()
        value[self._zero], value[self._zero -
                                 3] = value[self._zero - 3], value[self._zero]
        return Box(value, self._history + 'D')

    def left(self) -> 'Box':
        """
        'Box'.left() -> 'Box'

        向左移牌 | move left
        << 返回新的九宫格对象 | return new Box object
        """
        if self._zero in (2, 5, 8):
            raise ValueError('不能向左移牌 | cannot move left')
        value = self._value.copy()
        value[self._zero], value[self._zero +
                                 1] = value[self._zero + 1], value[self._zero]
        return Box(value, self._history + 'L')

    def right(self) -> 'Box':
        """
        'Box'.right() -> 'Box'

        向右移牌 | move right
        << 返回新的九宫格对象 | return new Box object
        """
        if self._zero in (0, 3, 6):
            raise ValueError('不能向右移牌 | cannot move right')
        value = self._value.copy()
        value[self._zero], value[self._zero -
                                 1] = value[self._zero - 1], value[self._zero]
        return Box(value, self._history + 'R')

    @property
    def able(self) -> list[callable]:
        """
        'Box'.able -> list[callable]

        查询可用的移动方法 | query usable move method
        << 返回可用的移动方法列表 | return list of usable move method
        """
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

    def expand(self) -> list['Box']:
        """
        'Box'.expand() -> list['Box']

        拓展下一层 | expand next layer
        << 返回新的九宫格对象列表 | return list of new Box object
        """
        return [i() for i in self.able]


def input_box(prompt: str = False) -> 'Box':
    """
    input_box(prompt: str = False) -> 'Box'

    交互式输入九宫格对象 | interactive input Box object
    >> prompt: 提示信息 | prompt message
    << 返回新的九宫格对象 | return new Box object
    """
    _WDICT = {'0': 0, ' ': 0, '': 0, '*': 0, '9': 0, '1': 1,
              '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}

    def _handle(word: str) -> int:
        try:
            return _WDICT[word]
        except KeyError:
            raise ValueError('无法识别你的输入 | cannot recognize your input')

    value = []
    print(prompt if prompt else '请按提示直接输入数值. 若以空格分隔, 则 0 或 * 可代表空位\nenter the value directly as '
                                'prompted.\nWhen separated by a space, 0 or * can be used to represent blank')
    for i in range(1, 4):
        line = input('第 {} 行 | row {}: '.format(i, i))
        if ',' in line:
            line = line.replace(' ', '').split(',')
        elif len(line) == 3:
            pass
        elif ' ' in line:
            line = line.split()
        else:
            raise ValueError('无法识别你的输入 | cannot recognize your input')
        if len(line) == 3:
            value += [_handle(i) for i in line]
        elif len(line) == 4 and line[3] == '':
            value += [_handle(i) for i in line[:3]]
        elif len(line) == 9 and i == 1:
            value += [_handle(i) for i in line]
            break
        else:
            raise ValueError('无法识别你的输入 | cannot recognize your input')
    print('[ {} {} {}\n  {} {} {}\n  {} {} {} ]\n'.format(
        *[i if i != 0 else '*' for i in value]))
    return Box(value)


if __name__ == '__main__':
    a = input_box()
    a = a.up().up()
    print(a)
    print(a.del_history())
    b = input_box()
    b.add_history('UDLR')
    print(b.del_history(2))

if __name__ == 'eight-puzzle':
    pass
