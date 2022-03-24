
import requests
from lxml import etree
import pandas as pd
import calendar
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',# 伪装成浏览器
    'Cookie':'SINAGLOBAL=20037146704.239285.1620219550117; _ga=GA1.2.267774703.1623314703; __gads=ID=2095934ca96ee8e7:T=1623314703:S=ALNI_MYUdC2bauFgWmtwQAyqdNUcPEOqmA; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhXL8pr0Z8U6m2nKrFSaemV5NHD95QfSK-cSKn4e0-RWs4Dqc_zi--ciKn7iKy8i--Xi-z4iKnRi--Ri-2NiKn4i--fi-i8iK.Ni--RiKnNi-8Wi--fi-zNi-zpi--fi-2fi-i2i--fiKnEi-iF; wvr=6; SUB=_2A25MSgs-DeThGeNL7lQU-CfPzjSIHXVvtJV2rDV8PUJbkNAKLUXXkW1NSO9ONJerSkijkdgGhx2UnBE3uGsrvRe8; UOR=,,www.baidu.com; _s_tentry=s.weibo.com; Apache=1182911696326.8848.1632793426585; ULV=1632793426700:8:5:3:1182911696326.8848.1632793426585:1632761927435; webim_unReadCount=%7B%22time%22%3A1632851204628%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A12%2C%22msgbox%22%3A0%7D; WBStorage=6ff1c79b|undefined',
    # 'Cookie':'UOR=vjudge.net,widget.weibo.com,vjudge.net; SINAGLOBAL=4300208395150.551.1622131944984; login_sid_t=b923edee27b8d41ba3303491205e6deb; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=6829139728432.778.1632847024805; ULV=1632847024814:3:1:1:6829139728432.778.1632847024805:1622183752769; SUB=_2A25MVzUkDeRhGeFN6lsQ-SnKyz-IHXVvJSHsrDV8PUNbmtB-LUnwkW9NQEh-rZoEkEFk3zk-sB2kWGCYQm6jIfiX; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0MeqVOb1W.mjPhGD-YK1U5JpX5KzhUgL.FoM0eK.p1KMcehe2dJLoI7D4Ig4yIJLuIg4r; ALF=1664383219; SSOLoginState=1632847220; wvr=6; webim_unReadCount=%7B%22time%22%3A1632847238315%2C%22dm_pub_total%22%3A6%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A57%2C%22msgbox%22%3A0%7D; WBStorage=6ff1c79b|undefined',
    'Host':'s.weibo.com',
    'sec-ch-ua':'"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'Connection': 'keep-alive'
}

SEARCH = "吴亦凡"
timescope = "custom:2021-{:0>2d}-{:0>2d}-{:d}:2021-{:0>2d}-{:0>2d}-{:d}"

S_MONTH,S_DAY = 1,1
E_MONTH,E_DAY = 9,29
PATH = 'weibo_{:s}_{:0>2d}.{:0>2d}-{:0>2d}.{:0>2d}.csv'.format(SEARCH,S_MONTH,S_DAY,E_MONTH,E_DAY)
STEP = 23
# url = 'https://s.weibo.com/weibo/%25E8%25A2%2581%25E9%259A%2586%25E5%25B9%25B3'

data = {}
sum = 0
ID,TIME,FROM,COMMENT,IN1,IN2,IN3,IN4 = [],[],[],[],[],[],[],[]
COLUMNS = ['发布者ID','发布时间','发布来源','发布内容','收藏数','转发数','评论数','点赞数']

comment_xpath = '//div[@id="pl_feedlist_index"]/div[2]/div[{0}]//div[@class="content"]/p[@class="txt"]'
comment_text_xpath = '//div[@id="pl_feedlist_index"]/div[2]/div[{0}]//div[@class="content"]/p[@class="txt"][{1}]//text()'
time_xpath = '//div[@id="pl_feedlist_index"]/div[2]/div[{0}]//div[@class="content"]/p[@class="from"]//text()'
information_xpath = '//div[@id="pl_feedlist_index"]/div[2]/div[{0}]//div[@class="card-act"]/ul/li/a//text()'

proxies={'http':'113.96.219.105:4015',
'https':'113.96.219.105:4015'}

def get_page(url,headers,params):
    try:
        
        response = requests.get(url, headers=headers,params=params,proxies=proxies)
        if response.status_code == 200:
            return response
            # return response.content.decode('utf-8')
        else:
            print('由于爬取数据太多的原因，现在稍等一段时间后再爬')
            import time
            time.sleep(60)
            return get_page(url,headers,params)
    except requests.RequestException:
        print('请求出错')
        return None

def replace_sth(str):
    str = ''.join(str)
    str = str.replace(' ', '')
    str = str.replace('\n',' ')
    str = str.replace('##', '# #')
    str = str.replace('收起全文d', ' ')
    str = str.replace('\xa0', '')
    return str
    
def add_list(id,time,comment_from,comment,information):
    if len(information) != 0:
        ID.append(id)
        TIME.append(time)
        FROM.append(comment_from)
        COMMENT.append(comment)
        IN1.append(information[0])
        IN2.append(information[1])
        IN3.append(information[2])
        IN4.append(information[-1])
        
def create_data():
    data_list = [ID,TIME,FROM,COMMENT,IN1,IN2,IN3,IN4]
    for i in range(len(data_list)):
        data[COLUMNS[i]] = data_list[i]
    return pd.DataFrame(data)

def save_csv(path = 'weibo.csv'):
    data = create_data()
    data.sort_values(['发布时间']).to_csv(path,encoding='utf_8_sig',index=False)

def get_Day_page(month,day,url = 'https://s.weibo.com/weibo'):
    params = {
        'q':SEARCH,
        "typeall":"1",
        "suball":"1",
        'timescope':'custom:2021-05-22:2021-05-22',
        # "Refer":"SWeibo_box",
        "Refer":"g",
        # "nodup":"1"
    }   
    for hour in range(0,23,STEP):
        next_hour = hour + STEP if (hour + STEP) <= 23 else 23
        params['page'] = 1
        params['timescope'] = timescope.format(month,day,hour,month,day,next_hour)
        response = get_page(url, headers, params)
        if response is None:
            continue
        text = response.text
        tree = etree.HTML(text)
        pages = len(tree.xpath('//div[@class="m-wrap"]//div[@class="m-page"]//ul[@class="s-scroll"]/li//text()'))
        if pages == 0:
            print('关于 "{0}" 的微博的页数共有{1}页,时间线为{2}'.format(SEARCH,1,params['timescope']))
            params['page'] = 1
            response = get_page(url, headers, params)

            text = response.text
            tree = etree.HTML(text)
            ids = tree.xpath('//div[@id="pl_feedlist_index"]//div[@class="content"]/div[@class="info"]/div[2]/a[1]/text()')
            # print(titles)
            error = tree.xpath('//div[@id="pl_feedlist_index"]//div[@class="m-error"]//text()')
            if len(error) != 0:
                ids = []
            global sum
            for i in range(len(ids)):
                comment = tree.xpath(comment_xpath.format(i+1))
                time_from = tree.xpath(time_xpath.format(i+1)) 
                if len(comment) > 1:
                    # print(title,'有评论被隐藏:')
                    # print(comment)
                    comment = tree.xpath(comment_text_xpath.format(i+1,2))
                else:
                    # print(title,'无评论被隐藏:')
                    # print(comment)
                    comment = tree.xpath(comment_text_xpath.format(i+1,1))
                id = ids[i]
                information = tree.xpath(information_xpath.format(i+1))
                
                for x in range(len(information)):
                    information[x] = information[x].replace(' ', '')
                    if (len(information[x]) == 2 or len(information[x]) == 0) and x != 4:
                        information[x] = 0
                    else:
                        information[x] = int(information[x]) if x == 4 else int(information[x][2:])
                
                time_from = replace_sth(time_from)
                if '来自' in time_from:
                    comment_time,comment_from = time_from[:time_from.index('来自')],time_from[time_from.index('来自'):]
                else:
                    comment_time,comment_from  = time_from,''
                comment_time = comment_time.replace(' ', '')
                comment = replace_sth(comment)
                add_list(id,comment_time,comment_from,comment,information)
            sum += len(ids)
            print('第{0}页爬取成功，爬取了{1}条微博，已经爬取了{2}条微博,时间线为{3}'.format(1,len(ids),sum,params['timescope']))  
        else:
            print('关于 "{0}" 的微博的页数共有{1}页,时间线为{2}'.format(SEARCH,pages,params['timescope']))
            for page in range(1,pages + 1):
                print('正在爬取第{0}页的数据'.format(page))
                params['page'] = page
                response = get_page(url, headers, params)
                text = response.text

                tree = etree.HTML(text)
                ids = tree.xpath('//div[@id="pl_feedlist_index"]//div[@class="content"]/div[@class="info"]/div[2]/a[1]/text()')
                # print(titles)
                for i in range(len(ids)):
                    comment = tree.xpath(comment_xpath.format(i+1))
                    time_from = tree.xpath(time_xpath.format(i+1)) 
                    if len(comment) > 1:
                        # print(title,'有评论被隐藏:')
                        # print(comment)
                        comment = tree.xpath(comment_text_xpath.format(i+1,2))
                    else:
                        # print(title,'无评论被隐藏:')
                        # print(comment)
                        comment = tree.xpath(comment_text_xpath.format(i+1,1))
                    id = ids[i]
                    information = tree.xpath(information_xpath.format(i+1))
                    
                    for x in range(len(information)):
                        information[x] = information[x].replace(' ', '')
                        if (len(information[x]) == 2 or len(information[x]) == 0) and x != 4:
                            information[x] = 0
                        else:
                            information[x] = int(information[x]) if x == 4 else int(information[x][2:])
                    
                    time_from = replace_sth(time_from)
                    if '来自' in time_from:
                        comment_time,comment_from = time_from[:time_from.index('来自')],time_from[time_from.index('来自'):]
                    else:
                        comment_time,comment_from  = time_from,''
                    comment_time = comment_time.replace(' ', '')
                    comment = replace_sth(comment)
                    add_list(id,comment_time,comment_from,comment,information)        
                    # print(comment + '\n' + time_from + '\n' + ' '.join(information))
                    # break
                    # comment = comment.text
                sum += len(ids)
                print('第{0}页爬取成功，爬取了{1}条微博，已经爬取了{2}条微博,时间线为{3}'.format(page,len(ids),sum,params['timescope']))
                save_csv(PATH)
        print('-'*10 + '2021-{:0>2d}-{:0>2d}天 已经爬完'.format(month,day) + '-'*10)
        save_csv(PATH)

# from multiprocessing.dummy import Pool
from pathos.multiprocessing import ProcessingPool as Pool

if __name__ == '__main__':
    sum = 0
    data = {}
    pool = Pool(8)
    for month in range(S_MONTH,E_MONTH+1):
        # for day in range(1,calendar.monthrange(2021,month)[1] + 1):
            if (month == S_MONTH) or (month == E_MONTH):
            #     continue
                day_list = [i for i in range(S_DAY,E_DAY + 1)]
            day_list = [i for i in range(1,calendar.monthrange(2021,month)[1] + 1)]
            month_list = [month] * len(day_list)
            # print(month_list,day_list)
            # break
            pool.map(get_Day_page,month_list,day_list)
    print('-'*10 + '2021-{:0>2d}月份 已经爬完'.format(month) + '-'*10)
    save_csv(PATH)
    pool.close()
    pool.join()
    print('------------END------------')