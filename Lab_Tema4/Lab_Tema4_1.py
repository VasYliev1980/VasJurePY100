def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    new_dict = {}

    for i in str_.lower():
        if i.isalpha():
            new_dict[i] = new_dict.get(i, 0) + 1
    return new_dict  # порядок не важен

def get_weight_char(dict_):
    # TODO посчитать вес (%) каждой буквы в строке в аргументе str_
    s = sum(dict_.values())

    for i in dict_.keys():
        dict_[i] = round(dict_[i] * 100 / s, 2)
    return dict_

main_str = """
Данное предложение будет разбиваться на отдельные слова. В качестве разделителя для встроенного метода split будет выбран символ
пробела. На выходе мы получим список отдельных слов. Далее нужно отсортировать слова в алфавитном порядке, а после сортировки
склеить их с помощью метода строк join. Приступим!!!!
 """
d = get_count_char(main_str)

print(d)
