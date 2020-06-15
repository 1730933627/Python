import jieba
from wordcloud import WordCloud

def read_file(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        dan_mu = f.read()
        return dan_mu

def jieba_cut(str):
    jieba.suggest_freq('华氏老方', tune=True)
    jieba.suggest_freq('起名鬼才', tune=True)
    cut_list = jieba.lcut(str)
    return cut_list

def gen_word_cloud(cut_list, filename):
    word_str = ' '.join(cut_list)
    wc_settings = {
        'font_path': 'msyh.ttc',
        'width': 800,
        'height': 560,
        'background_color': 'white',
        'max_words': 100
    }
    wc = WordCloud(**wc_settings).generate(word_str)
    wc.to_file(filename)

if __name__ == '__main__':
    try:
        BV = input("输入BV号：")
        str = read_file(f'{BV}.txt')
        cut_list = jieba_cut(str)
        gen_word_cloud(cut_list, f'{BV}.png')
    except:
        print("没有找到该文件")
