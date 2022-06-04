# Twibot-22 Baselines
This repo contains the official implementation of [TwiBot-22]() baselines.

### Introduction
TwiBot-22 is the largest and most comprehensive Twitter bot detection benchmark to date. Specifically, [TwiBot-20](https://dl.acm.org/doi/pdf/10.1145/3459637.3482019) is designed to address the challenges of limited dataset scale, imcomplete graph structure, and low annotation quality in previous datasets. For more details, please refer to the [TwiBot-22 paper]() and [statistics](descriptions/statistics.md).
![compare](./pics/compare.png)

### Dataset Format
Each dataset contains `node.json`, `label.csv`, `split.csv` and `edge.csv` (for datasets with graph structure). See [here](descriptions/metadata.md) for a detailed description of these files.

### How to download TwiBot-22 dataset
`gdown --id`

### Requirements
- pip: `pip install -r requirements.txt`
- conda : `conda install --yes --file requirements.txt `

### How to run baselines
1. clone this repo by running `git clone ` 
2. download datasets to `./datasets`
3. change directory to `src/{name_of_the_baseline}`
4. run experiments under the guidance of corresponding `readme.md`

### Baseline Overview

| baseline      | acc on Twibot-22 | f1 on Twibot-22 | type | tags                |
| ------------- | ---------------- | --------------- | ---- | ------------------- |
| [NameBot](src/NameBot/) | 0.7061           | 0.0050          | None | `Logistic Regression` |
| [Bot Hunter](src/BotHunter/) |0.7279|0.2346|P|`random forest`|
| [Botomater](src/Botometer/) |      49.87       |      42.75      | P T G |      |
| [BotRGCN](src/BotRGCN/) |0.7691| 0.4579          |P T G|`BotRGCN`|
| [Cresci et al.](src/Cresci/)|-|-|T|`DNA`|
| [efthimion](src/efthimion/)|0.7481|0.2758|P T|`efthimion`|
| [Kipf et al.](src)       | 0.7489           | 0.2513          | P T G | `Graph Neural Network` |
| [Velickovic et al.](src/V) | 0.7585           | 0.4394          | P T G | `Graph Neural Network`   |
| [Alhosseini et al.](src/Alhosseini/)|0.6103|0.5473|P G|`gcn`|
| [GraphHist](src/GraphHist/) | /                | /               | P T G | `random forest` |
| [Guo et al.](src/Guo/)|  0.7055                0.00         |    P |`BERT GAT`|
| [Hayawi et al.](src/Hayawi/) |0.7187|0.1325|P|`lstm`|
| [HGT](src/HGT_SimpleHGN/)|0.7491|0.3960|P T G|`Graph Neural Networks`|
| [SimpleHGN](src/HGT_SimpleHGN/)|0.7672|0.4544|P T G|`Graph Neural Networks`|
| [Kantepe et al.](src/Kantepe/))|0.764|0.587|P T|`random forest`|
| [Knauth et al](src/Knauth/) | /                | /               | P T G | `random forest` |
| [Kouvela et al.](src/Kouvela/)|76.44|30.03|P T|`random forest`|
| [Kudugunta et al.](src/Kudugunta/)|0.6587|0.5167|P|`SMOTENN, random forest`|
| [Lee et al.](src/Lee/)|76.28|30.41|P T|`random forest`|
| [LOBO](src/LOBO/) |0.7570|0.3857|P T|`random forest`|
| [Miller et al.](src/Miller/)|/|/|P T|`k means`|
| [Moghaddam et al.](src/Moghaddam/)|0.7378|0.3207|P G|`random forest`|
| [Abreu et al.](src/Abreu/) | 0.7066           | 0.5344          | P    | `random forest` |
| [RGT](src/RGT/) | 0.7647 | 0.4294 | P T G |`Graph Neural Networks`|
| [RoBERTa](src/RoBERTa/)|0.7196|0.1915|P T|`RoBERTa`|
| [Rodrguez-Ruiz](src/Rodrguez-Ruiz/)|0.7071|0.0008|P T G|`SVM`|
| [Santos et al.](src/Santos/)|/|/|P T|`decision tree`|
|  [SATAR](src/SATAR/)   |        -         |        -        | P T G |      |
| [T5](src/Varol/)|0.7170|0.1565|T|`T5`|
| [Varol et al.](src/Varol)|0.7392|0.2754|P T|`random forest`|
| [Wei et al.](src/Wei/)|0.702|0.536|T||
| [SGBot](src/SGBot/)|0.7392|0.2754|P T|`random forest`|
| [EvolveBot](src/EvolveBot/) |0.7109|0.1408|P T G|`random forest`|

### How to contribute
1. New dataset: convert the original data to the [TwiBot-22 defined schema](descriptions/metadata.md).
2. New baseline: load well-formatted dataset from the dataset directory and define your model.

Welcome PR!