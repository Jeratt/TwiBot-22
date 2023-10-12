import json
import ijson
from itertools import islice
import pandas as pd
from tqdm import tqdm

#import ijson.backends.yajl2_c as ijson
def parse_json_tweets():
    print('loading raw data')
    path='../datasets/Twibot-22/'

    ijson_data = ijson.items(open(path+'user.json', 'rb'), 'item')
    user = None
    while batch := islice(ijson_data, int(5.0e3)):
        df = pd.DataFrame(batch)
        if df.empty:
            break
        user = pd.concat([user, df], axis=0)
    # user=pd.read_json(path+'user.json')

    user_idx=user['id']
    uid_index={uid:index for index,uid in enumerate(user_idx.values)}
    user_index_to_uid = list(user.id)
    # uid_to_user_index = {x : i for i, x in enumerate(user_index_to_uid)}

    print("USER.JSON PARSED")

    print("extracting each_user's tweets")

    for i in range(9):
        id_tweet = {i: [] for i in range(len(user_idx))}
        name='tweet_'+str(i)+'.json'
        user_tweets=ijson.items(open("../datasets/Twibot-22/"+name,'rb'), 'item')
        for each in tqdm(user_tweets):
            uid='u'+str(each['author_id'])
            text=each['text']
            try:
                index=uid_index[uid]
                id_tweet[index].append(text)
            except KeyError:
                continue
        json.dump(id_tweet,open('./processed_data/id_tweet.json','w'))

def check_size():
    name = 'tweet_' + str(4) + '.json'
    path = "../datasets/Twibot-22/" + name
    cnt = 0
    # user_tweets = ijson.items(open("../datasets/Twibot-22/" + name, 'rb'), 'item', buf_size = int(1e8))
    # while batch := islice(user_tweets, int(1e6)):
    #     key = False
    #     for _ in tqdm(batch):
    #             cnt += 1
    #             key = True
    #     if not key:
    #         break
    #     print(cnt)

    user_tweets = ijson.items(open("../datasets/Twibot-22/" + name, 'rb'), 'item')
    for _ in tqdm(user_tweets):
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    parse_json_tweets()
