def words_sorting(*args):
    info_dic = dict()
    total_values_sum = 0
    return_string = ''

    for word in args:
        ascii_sum = 0
        for idx in range(len(word)):
            ascii_sum += ord(word[idx])
        total_values_sum += ascii_sum
        info_dic[word] = ascii_sum

    if total_values_sum % 2 == 0:
        info_dic = sorted(
            info_dic.items(),
            key=lambda x: x[0]
        )
    else:
        info_dic = sorted(
            info_dic.items(),
            key=lambda x: -x[1]
        )

    for key, value in info_dic:
        return_string += key + ' - ' + str(value) + '\n'

    return return_string


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print()

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print()

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
