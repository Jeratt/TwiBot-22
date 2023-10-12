import pandas as pd
import numpy as np
import torch
from tqdm import tqdm
from datetime import datetime as dt
from itertools import islice
import json
import ijson
import gc
import os.path as osp

def edges_from_csv_to_tensors():
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
    uid_to_user_index = {x : i for i, x in enumerate(user_index_to_uid)}

    print("USER.JSON PARSED")


    for j in range(1, 19):
        edge_gen = pd.read_csv(path+f'edge_{j}.csv', chunksize=5e5)
        edge = None
        with tqdm() as pbar:
            for batch in edge_gen:
                df = pd.DataFrame(batch)
                edge = pd.concat([edge, pd.DataFrame(batch)])
                if df.empty:
                    break
                pbar.update(1)
        print("EDGE.CSV PARSED")

        print('extracting edge_index&edge_type')
        edge_index = []
        edge_type = []
        for i in tqdm(range(len(edge))):
            sid = edge['source_id'][i]
            tid = edge['target_id'][i]
            if edge['relation'][i] == 'followers':
                try:
                    edge_index.append([uid_index[sid], uid_index[tid]])
                    edge_type.append(0)
                except KeyError:
                    continue
            elif edge['relation'][i] == 'following':
                try:
                    edge_index.append([uid_index[sid], uid_index[tid]])
                    edge_type.append(1)
                except KeyError:
                    continue

        torch.save(torch.LongTensor(edge_index).t(), f"./processed_data/edge_index_{j}.pt")
        torch.save(torch.LongTensor(edge_type), f"./processed_data/edge_type_{j}.pt")

def cat_tensors():
    path = "./processed_data"
    edge_type = None
    edge_index = None
    for i in range(2, 19):
        edge_t = torch.load(osp.join(path, f'edge_type_{i}.pt'))
        edge_i = torch.load(osp.join(path, f'edge_index_{i}.pt'))
        if edge_type is None:
            edge_type = edge_t.clone()
        else:
            edge_type = torch.cat([edge_type, edge_t], dim=0)
        if edge_index is None:
            edge_index = edge_i.clone()
        else:
            edge_index = torch.cat([edge_type, edge_i], dim=1)
    torch.save(torch.LongTensor(edge_index).t(), "./processed_data/edge_index.pt")
    torch.save(torch.LongTensor(edge_type), "./processed_data/edge_type.pt")

def check_tensor(path="./processed_data"):
    edge_t = torch.load(osp.join(path, 'edge_type.pt'))
    edge_i = torch.load(osp.join(path, 'edge_index.pt'))
    print(edge_t.shape)
    print(edge_i.shape)

if __name__ == "__main__":
    check_tensor()