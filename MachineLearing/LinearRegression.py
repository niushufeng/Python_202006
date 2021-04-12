# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class LinearRegression(object):
    def __init__(self,input_data,realresult,theta = None):
    def Cost(self):
    def BGD(self,alpha):
    def SGD(self,alpha):
    def Shuffle_Sequence(self):
    def MBGD(self,alpha,batch_size):
    def getNormalEquation(self):
    def train_BGD(self,iter,alpha):
    def train_SGD(self,iter,alpha):
    def train_MBGD(self,iter,mini_batch,alpha):
    def test(self,test_data):
    def predict(self,data):
        
def __init__(self,input_data,realresult,theta = None):
    """
    :param input_data:输入数据
    :param realresult:真实结果
    :param theta:线性回归的参数，默认为None
    """
    # 获取数据集的形状
    row,col = np.shape(input_data)
    # 构造输入数据数组
    self.InputData = [0] * row
    # 给每组输入数据增添常数项1
    for(index,data) in enumerate(input_data):
        Data = [1.0]
        # 把input_data拓展到Data内，即把input_data的每一维数据添加到Data
        Data.extend(list(data))
        self.InputData[index] = Data
    self.InputData = np.array(self.InputData)
    # 构造输入数据对应的结果
    self.Result = realresult
    # 参数theta不为None时，利用theta构造模型参数
    if theta is not None:
        self.Theta = theta
    else:
        # 随机生成服从标准正态分布的函数
        self.Theta = np.random.normal((col + 1,1))

def BGD(self,alpha):
    """
    这是利用BGD算法进行一次迭代调整参数的函数
    : param alpha:学习率
    """
    # 定义梯度增量数组
    gradient_increasment = []
    # 对输入的训练数据及其真实结果进行依次便利
    for(input_data,real_result) in zip(self.InputData,self.Result):
        # 计算每组input_data的梯度增量，并放入梯度增量数组
        g = (real_result - input_data,dot(self.Theta)) * input_data
        gradient_increasment.append(g)
    # 按列计算属性的平均梯度增量
    avg_g = np.average(gradient_increasment,0)
    # 改变平均梯度增量数组形状
    avg_g = avg_g.reshape(len(avg_g),1)
    # 更新模型参数self.Theta
    self.Theta = self.Theta + alpha * avg_g

def SGD(self,alpha):
    """
    这是利用SGD算法进行一次迭代调整参数的函数 
    : param alpha:学习率 
    """
    # 首先将数据集随机打乱,减少数据集顺序对参数调优的影响 
    shume_sequence = self.Shuffle_Sequence()
    self.InputData = self.InputData[Shuffle_sequence]
    self.Result = self.Result[Shuffle_sequence]
    # 对训练数据集进行遍历，利用每组训练数据对参数进行调整 
    for(input_data,real_result) in zip(self.InputData,self.Result):
        # 计算每组input_data的梯度增量 
        g = (real_result - input_data.dot(self.Theta)) * input_data
        # 调整每组input_data的梯度增量的形状 
        g = g.reshape(len(g),1)
        # 更新线形回归的模型参数
        self.Theta = self.Theta + alpha * g


    
    
                

    
