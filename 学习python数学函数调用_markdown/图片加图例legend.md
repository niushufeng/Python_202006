给生成的figure加legend
===
# 之前的代码片段
```python
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0, linestyle='--' )
```
## 在没有添加图例之前生成的图片
上传不上去emmmmm:flushed:
----
# 改过之后的代码
```python
l1, = plt.plot(x,y2,label="up")  # label 指的是标签
l2, = plt.plot(x,y1,color='red',linewidth=1.0, linestyle='--',label="down")
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc="best")  # legent 指的是图例 
# handles 指的是控制，把控的意思，用best挑选一个数据最少的位置
```
'aaa'和'bbb'就是标签的名称，loc是local的简写，代表标签的位置，'best'指的是挑选一个最适合的位置
## 改过之后生成的图片
上传不上去emmmm:bowtie:
----
[回到顶部](#readme)
----
