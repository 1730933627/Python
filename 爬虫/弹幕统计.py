def get_dan_mu(in_filename):
    with open(in_filename,mode='r',encoding='utf-8')as fi:
        dan_mu = fi.read()
    return dan_mu

def save_file(out_filename,arr):
    with open(out_filename,mode='w',encoding='utf-8')as fo:
        for sort_wold in arr:
            fo.write("{0}   >{1:->10}次".format(sort_wold[0],sort_wold[1]))
            fo.write('\n')

def count_word(dan_mu):
    dicts = {}
    wold_list = dan_mu.split("\n")
    for wold in wold_list:
        dicts[wold] = dicts.get(wold,0)+1
    arr = list(dicts.items())
    arr.sort(key=lambda x:x[1],reverse=True)
    return arr
    
def main(in_filename,out_filename):
    dan_mu = get_dan_mu(in_filename)
    arr = count_word(dan_mu)
    save_file(out_filename,arr)

if __name__ == '__main__':
    try:
        BV = input("输入BV号：")
        in_filename = f'{BV}.txt'
        out_filename = f'{BV}-统计.txt'
        main(in_filename,out_filename)
    except:
        print("没有文件可以被打开")
