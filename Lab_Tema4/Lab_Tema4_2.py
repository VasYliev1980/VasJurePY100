# TODO реализовать функцию удаления элемента из списка по индексу

def delete(list_, index=None):
    new_list = []
    if index is None:
        index = len(list_) - 1
    for i in range(len(list_)):
        if i != index:
            new_list.append(list_[i])
    return new_list

if __name__ == '__main__':

print(delete([0, 0, 1, 2], index=1))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))

