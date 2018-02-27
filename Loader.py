import chardet
import operator

newsafr = 'newsafr.txt'
newscy = 'newscy.txt'
newsfr = 'newsfr.txt'
newsit = 'newsit.txt'


def news_sorted(text_on_sorted):
    with open(text_on_sorted,'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print(result)
        text = data.decode(result['encoding'])

    list_text = text.split()
    list_text_before_len = []
    dict_text_before_word_count = {}

    for word in list_text:
        if len(word) > 5:
            list_text_before_len.append(word)

    for i,word, in enumerate(list_text_before_len):
        dict_text_before_word_count.update({word : list_text_before_len.count(list_text_before_len[i])})

    sorted_finish = sorted(dict_text_before_word_count.items(), key = operator.itemgetter(1), reverse = True)
    return print(sorted_finish[0:10])


print("Сортировка Топ-10 Африка")
news_sorted(newsafr)
print("Сортировка Топ-10 Россия")
news_sorted(newscy)
print("Сортировка Топ-10 Россия-2")
news_sorted(newsfr)
print("Сортировка Топ-10 Италия")
news_sorted(newsit)