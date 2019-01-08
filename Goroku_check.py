import twitter
import requests
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup  # スクレイピングするための部品(モジュール)

url_acceed = "http://dic.nicovideo.jp/a/%E6%B7%AB%E5%A4%A2%E8%AA%9E%E9%8C%B2%28coat%29"

HTML_acceed = requests.get(url_acceed)

soup_acceed = BeautifulSoup(HTML_acceed.content, "html.parser")

div_acceed = soup_acceed.find_all("table")

file = open('text.txt','w')
#div_acceed = div_acceed[1:11]
div_acceed = div_acceed[1:10]
for i in div_acceed:
    i = i.find_all("td")
    #print(j)
    for n, a in enumerate(i):
        if n % 4 == 0:
            file.write(a.get_text() + '\n')

def goroku_check_acceed(text):
    myfile = open("text.txt")
    datas = myfile.readlines()
    myfile.close()

    text += "\n"#改行文字を足さないとnullになってしまう

    for data in datas:
        if text in datas:#「in」演算子の左辺のオブジェクトを持つ値が右辺のリストオブジェクトの要素の中に存在している場合は「True」を返します。存在しない場合は「False」を返します。
            return True

def goroku_check_cort(text):
    
    url_cort = "http://dic.nicovideo.jp/a/%E6%B7%AB%E5%A4%A2%E8%AA%9E%E9%8C%B2%28acceed%29"  # URLを指定する。文字列としてurlという変数に格納
    HTML_cort = requests.get(url_cort)
    soup_cort = BeautifulSoup(HTML_cort.content, "html.parser")  # 
    # 指定したURLのソースを得る
    div_cort = soup_cort.find_all("table")
    goroku = [10]

    for i in div_cort[:-8]:#余分なtableを除外
        i = i.find_all("tr")


        for goroku in i[1:]:#最初にnullが入っている？
            goroku = (goroku.find("td"))
            if goroku.get_text() in text:
                return True

if __name__ == '__main__':
    api_key = "xxxx"
    api_secret = "xxxx"
    access_key = "xxxx"
    access_secret = "xxxx"

# please use your keys
    auth = twitter.OAuth(consumer_key="xxxx",
    consumer_secret="xxxx",
    token="xxxx",
    token_secret="xxxx")

    auth2 = OAuth1Session(api_key, api_secret, access_key, access_secret)

    favo = "https://api.twitter.com/1.1/favorites/create.json"
    tweet = "https://api.twitter.com/1.1/statuses/update.json"
    inmu_rist = "https://api.twitter.com/1.1/lists/members/create.json"
    
    #Userstreamを用いる
    t_userstream = twitter.TwitterStream(auth=auth,domain='userstream.twitter.com')

    #自分のタイムラインのツイートおよびユーザーの情報が流れる
    #淫夢のリストに追加するように実装する
    for msg in t_userstream.user():
        if('retweeted' in msg.keys() and msg['retweeted'] == True):
            continue

        if ('text' in msg.keys() and goroku_check_cort(msg['text'])==True):
            print(msg.keys())
            
            print(msg['text'])
            
            params={'id' : msg['id_str']}
            
            request = auth2.post(favo, params = params)#ファボする
            
            print(msg['id_str'])
            
            params_tweet={'in_reply_to_status_id':msg['id_str'],'status':'@' + msg["user"]['screen_name'] + " FF外？から失礼するゾ〜。このツイート語録スギィ！！自分、指摘していいっすか？？淫夢知ってそうだから淫夢のリストにぶち込んでやるぜ！！すいません、許してください！！何でもしますから（何でもするとは言ってない）"}
            
            request2 = auth2.post(tweet, params = params_tweet)#クソリプする

            params_list={'list_id':'953194341513621505','screen_name':msg["user"]['screen_name']}

            request3 = auth2.post(inmu_rist, params = params_list)#リストにぶち込む
            
        
        elif ('text' in msg.keys() and goroku_check_acceed(msg['text'])==True):
            print(msg.keys())
            
            print(msg['text'])
            
            params={'id' : msg['id_str']}
            
            request = auth2.post(favo, params = params)#ファボする
            
            print(msg['id_str'])
            
            params_tweet={'in_reply_to_status_id':msg['id_str'],'status':'@' + msg["user"]['screen_name'] + " FF外？から失礼するゾ〜。このツイート語録スギィ！！自分、指摘していいっすか？？淫夢知ってそうだから淫夢のリストにぶち込んでやるぜ！！すいません、許してください！！何でもしますから（何でもするとは言ってない）"}
            
            request2 = auth2.post(tweet, params = params_tweet)#クソリプする

            params_list={'list_id':'953194341513621505','screen_name':msg["user"]['screen_name']}

            request3 = auth2.post(inmu_rist, params = params_list)#リストにぶち込む
