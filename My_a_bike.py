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
list_text_before_len = []
dict_text_before_word_count = {}


for word in list_text:
    if len(word) > 5:
        # print(word)
        list_text_before_len.append(word)

for word in list_text_before_len:
    word_count = {}
    i = 0
    if word in list_text_before_len:
        for word_equal in list_text_before_len:
            if word == word_equal:
                i += 1
            dict_text_before_word_count.update({word : i})
                # word_count.update({word : i})
                # print(word_count)

# print(dict_text_before_word_count)
sorted_x = sorted(dict_text_before_word_count.items(), key = operator.itemgetter(1),reverse = True)
print(sorted_x[0:10])