import chardet
import operator

with open('newscy.txt','rb') as f:
    data = f.read()
    result = chardet.detect(data)
    print(result)
    text = data.decode(result['encoding'])
    # print(type(text))
    # code = (list(result.values()))
    # print(type(code[0]))

list_text = text.split()
# print(list_text)
# print(list_text.count('России'))

list_text_before_len = []
dict_text_before_word_count = {}

for word in list_text:
    if len(word) > 5:
        # print(word)
        list_text_before_len.append(word)

# def per_finish_sorted(number_word_in_list):
#     return list_text_before_len.count[number_word_in_list]
#
# for i,word, in enumerate(list_text_before_len):
#     after_list_sorted =sorted(list_text_before_len, key = per_finish_sorted(i), reverse=True)
# print(after_list_sorted)

for i,word, in enumerate(list_text_before_len):
    dict_text_before_word_count.update({word : list_text_before_len.count(list_text_before_len[i])})
    # print(list_text_before_len[i],word)
    # print(list_text_before_len.count(list_text_before_len[i]))

print(dict_text_before_word_count)
sorted_x = sorted(dict_text_before_word_count.items(), key = operator.itemgetter(1),reverse = True)
print(sorted_x[0:10])


# def sortByLength(inputStr):
#     # if len(inputStr) > 5:
#     return len(inputStr)
#
#
#
# sort_list_text = sorted(list_text, key=sortByLength, reverse = True)
# print(sort_list_text)
# list_text.sort(key=sortByLength)

# =========================================================================
# list_text_before_len = []
# dict_text_before_word_count = {}
# for word in list_text:
#     if len(word) > 5:
#         # print(word)
#         list_text_before_len.append(word)
#
# for word in list_text_before_len:
#     word_count = {}
#     i = 0
#     if word in list_text_before_len:
#         for word_equal in list_text_before_len:
#             if word == word_equal:
#                 i += 1
#             dict_text_before_word_count.update({word : i})
#                 # word_count.update({word : i})
#                 # print(word_count)
#
# # print(dict_text_before_word_count)
# sorted_x = sorted(dict_text_before_word_count.items(), key = operator.itemgetter(1),reverse = True)
# print(sorted_x[0:10])

# [('туристов', 56), ('России', 41), ('Seasons', 28), ('россиян', 24), ('отдыха', 22), ('Интерфакс', 20), ('Туризм', 20), ('человек', 20), ('которые', 19), ('Cyprus', 18)]
# ================================================================
    # print(type(word))
# print(list_text_before_len)
# print(type(list_text))
# print(list_text)

# with open('newscy.txt', encoding = code[0]) as NewsPaper:
#     for line_news in NewsPaper:
#         print(line_news)

# with open('newscy.txt', encoding = result["encoding"]) as NewsPaper:
#     for line_news in NewsPaper:
#         print(line_news)

# with open('newsafr.txt', encoding = 'utf-8') as NewsPaper:
#     for line_news in NewsPaper:
#         print(line_news)


# with open('newscy.txt', encoding = 'koi8-r') as NewsPaper:
#     for line_news in NewsPaper:
#         print(line_news)

# with open('newsfr.txt', encoding = 'ISO-8859-5') as NewsPaper:
#     for line_news in NewsPaper:
#         print(line_news)

# with open('newsit.txt', encoding = 'cp1251') as NewsPaper:
#     for line_news in NewsPaper:
#         print(line_news)