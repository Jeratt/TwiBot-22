import os
#print(os.path.abspath("BotRGCN"))
#os.chdir("./BotRGCN")
order="python preprocess_1.py"
os.system(order)
order="python preprocess_2.py"
os.system(order)