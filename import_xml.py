# Функция чтения файла xml в список слов
def file_read_list(file_name):
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_name, parser)
    root = tree.getroot()
    news_list = root.findall("channel/item")
    all_news = []
    for news in news_list:
        new = news.find('description').text
        all_news.extend(new.lower().split())
        # Для подсчета слов в заголовках, включить две строки:
        # new = news.find('title').text
        # all_news.extend(new.lower().split())
    return all_news
# Функция подсчета количества слов длиной больше 6 в списке 
def word_dict(all_news, len_word = 6):
    news_dict = {}
    for word in all_news:
        if len(word) > len_word:
            news_dict.setdefault(word, 0)
            news_dict[word] += 1
    return news_dict
# Функция сортировки словаря и выбора из списка слов топ 10 по частоте
def sort_dict(news_dict, count_word = 10):
    news_dict_sort = {}
    for key in sorted(news_dict, key = news_dict.get, reverse=True):
        news_dict_sort[key] = news_dict[key]
    return list(news_dict_sort)[:count_word]
# Задача №2  
if __name__ == '__main__':
    result = sort_dict(word_dict((file_read_list("files/newsafr.xml"))))
    print(result)       
