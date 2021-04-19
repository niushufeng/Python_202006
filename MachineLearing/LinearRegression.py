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

def MBGD(self,alpha,batch_size):
    """
    这是利用MBGD算法进行一次迭代调整参数的函数 
    : param alpha:学习率
    : param batch_size:小批量样本规模 
    """
    # 首先将数据集随即打乱，减少数据集顺序对参数调优的影响 
    shuffle_sequence = self.Shuffle_Sequence()
    self.InputData = self.InputData[shuffle_sequence]
    self.Result = self.Result[shuffle_sequence]
    # 遍历每个小批量样本 
    for start in np.arange(0,len(shuffle_sequence),bath_size):
        # 判断start + batch_size是否大于数组长度  
        # 防止最后一组批量样本规模可能小于bath_size的情况
        end = np.min([start + batch_size,len(shuffle_sequence)])
        # 获取训练小批量样本集及标签 
        mini_batch = shuffle_sequence[start:end]
        Mini_Train_Data = self.InputData[mini_batch]
        Mini_Train_Result = self.Result[mini_batch]
        # 定义梯度增量数组 
        gradient_increasment = []
        # 对小样本训练集进行遍历，利用每个样本的梯度增量的平均值对模型参数进行更新
        for(data,result) in zip(Mini_Train_Data,Mini_Train_Result):
            # 计算每组input_data的梯度增量，并放入梯度增量数组 
            g = (result - data.dot(self.Thata) * data)
            gradient_increasment.append(g)
        # 按列计算每组小样本训练的梯度增量的平均值，并改变其形状 
        avg_g = np.average(gradient_increasment,0)
        avg_g = avg_g.reshape((len(avg_g),1))
        # 更新模型参数self.theta
        self.Theta = self.Theta + alpha * avg_g
        def train_BGD(self,iter,alpha):
    """ 
    这是利用BGD算法迭代优化的函数 
    ：param iter：迭代次数 
    ：param alpha:学习率 
    """
    # 定义平均训练损失函数，记录每轮迭代的训练数据集的损失 
    Cost = []
    # 开始进行迭代训练 
    for i in range(iter):
        # 利用学习率alpha,结合BGD算法对模型进行训练
        self.BGD(alpha)
        # 记录每次迭代的平均训练损失
        Cost = np.array(self.Cost())
        Cost = np.array(Cost)
        return Cost

def train_SGD(self,iter,alpha):
    """
    这是利用SGD算法迭代优化的函数
    ：param iter:迭代次数
    : param alpha：学习率 
    """
    # 定义平均训练损失函数，记录每轮迭代的训练数据集的损失 
    Cost = []
    # 开始进行迭代训练 
    for i in range(iter):
        # 利用学习率alpha,结合SGD算法对模型进行训练 
        self.
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

    
    
                

    
