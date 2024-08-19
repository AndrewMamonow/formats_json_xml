# Функция чтения файла json в список слов
def file_read_list(file_name):
    import json
    with open("files/newsafr.json", encoding="utf-8") as f:
        json_data = json.load(f)
    news_list = json_data['rss']['channel']['items']
    all_news = []
    for new in news_list:
        all_news.extend(new['description'].lower().split())
        # Для подсчета слов в заголовках, включить строку:
        # all_news.extend(new['title'].lower().split())
    return all_news
# Функция подсчета количества слов длиной больше 6 в списке 
def word_dict(all_news, len_word=6):
    news_dict = {}
    for word in all_news:
        if len(word) > len_word:
            news_dict.setdefault(word, 0)
            news_dict[word] += 1
    return news_dict
# Функция сортировки словаря и выбора из списка слов топ 10 по частоте
def sort_dict(news_dict, count_word=10):
    news_dict_sort = {}
    for key in sorted(news_dict, key = news_dict.get, reverse=True):
        news_dict_sort[key] = news_dict[key]
    return list(news_dict_sort)[:count_word]
# Задача №1
if __name__ == '__main__':
    all_news = file_read_list("files/newsafr.json")
    news_dict=word_dict(all_news)
    result = sort_dict(news_dict)
    print(result)