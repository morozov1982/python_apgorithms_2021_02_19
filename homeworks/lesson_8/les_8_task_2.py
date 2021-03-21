"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter, deque


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def create_tree(data):
    while len(data) > 1:
        left = data.popleft()
        right = data.popleft()
        value = left[1] + right[1]
        node = (Node(left=left[0], right=right[0]), value)

        for idx, el in enumerate(data):
            if el[1] < value:
                continue
            else:
                data.insert(idx, node)
                break
        else:
            data.append(node)

    return data


def encode(tree, table, path: str = ''):
    if not isinstance(tree, Node):
        table[tree] = path
    else:
        encode(tree=tree.left,  table=table, path=f'{path}0')
        encode(tree=tree.right, table=table, path=f'{path}1')


string = 'beep boop beer!'  # проверял и на других строках

frequency = deque(sorted(Counter(string).items(), key=lambda x: x[1]))
print(f'\33[33mЧастоты символов:\33[0m "{dict(frequency)}"')

tree_ = create_tree(frequency)
dict_ = dict()
encode(tree_[0][0], dict_)
print(f'\33[33mКоды символов:\33[0m "{dict_}"\n')

coded_string = ''.join([dict_[i] for i in string])

print(f'\33[32mПроверочная строка:\33[0m "{string}"')
print(f'\33[32mЗакодированная строка:\33[0m "{coded_string}"')
