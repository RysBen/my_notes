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
