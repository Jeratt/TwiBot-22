import pandas as pd
from tqdm import tqdm

#path='../datasets/Twibot-22/'

# edge_gen = pd.read_csv('test_edge.csv', chunksize=3e0)
# edge = None
# cnt = 0
# with tqdm() as pbar:
#     for batch in edge_gen:
#         df = pd.DataFrame(batch)
#         edge = pd.concat([edge, pd.DataFrame(batch)])
#         if df.empty:
#             break
#         cnt += 1
#         pbar.update(1)
#
# print(f"EDGE.CSV PARSED: {cnt}")

with open("../datasets/Twibot-22/edge.csv", 'r') as fin:
    cnt = 0
    while(fin.readline() != ""):
        cnt += 1

print(cnt)