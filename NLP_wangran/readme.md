# 2. 神经网络训练（求解）
## 2.1 传统优化求解方法
- 拟牛顿法
- Proximal
> 存在问题：需要根据全部样本计算梯度（导数），导致复杂网络求解的不可行。
## 2.2 随机梯度下降法
> 选取 Batch 进行梯度运算。
- SGD
- SGD + Me
- Adam
> 梯度消失 & 梯度爆炸

# 3. 神经网络基本构成
- 损失函数
  - L2 loss(continuous variable): L<sub>2</sub>(y',y) = (y'-y)<sup>2</sup>
  - Cross Entropy(discrete variable): 
- 全连接层
- 激活函数
  - sigmoid()
  - tanh()
  - Relu()
- Dropout
- Batch Normalization

# 4. 网络模型
## 4.1 Embedding
1. 定义
> 形式上讲，Embedding 就是用一个低维稠密的向量 “表示” 一个对象。“表示” 意味着向量能够表达相应对象的某些特征，同时向量之间的距离反映了对象之间的相似性。  
> Word embedding 是一种词的类型表示，具有相似意义的词具有相似的表示，是将词汇映射到实数向量的方法总称。词嵌入是自然语言处理的重要突破之一。
2. 算法
- Embedding Layer
- Word2Vec
  - CBOW
  - Skip-gram
- GloVe

参考资料
> 深度学习推荐系统中各类流行的Embedding方法（上）  
> 自然语言处理：什么是词嵌入(word embedding)？  
> \[Word Embedding系列] one-hot 编码  

## 4.2 循环神经网络（RNN）

