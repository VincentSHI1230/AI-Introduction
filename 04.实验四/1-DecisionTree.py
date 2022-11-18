# -*- coding: utf-8 -*- #
import graphviz
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
from sklearn import preprocessing
import csv

# 载入数据
Dtree = open(r'DecisionTreeSet.csv', 'r')
reader = csv.reader(Dtree)

# 读取第一行
headers = reader.__next__()

# 定义两个列表，存放特征和标签
feature = []
label = []

for row in reader:  # 每次从reader里面读取一行
    # 把label存入list
    label.append(row[-1])  # 每一行最后一列的数据存入标签的list中
    rowDict = {}
    for i in range(1, len(row) - 1):  # 某一行的每一列(除第一行，最后一列以外)对应元素遍历，存入rowDict中
        # 建立一个数据字典
        rowDict[headers[i]] = row[i]
    # 把数据字典存入list
    feature.append(rowDict)  # 再将每个rowDict保存到特征list

# 将上面的字符表示转化为数字
vec = DictVectorizer()  # DictVectorizer类可以将字典里的字符转换为数字形式
x = vec.fit_transform(feature).toarray()
print('转换成数字表示的x: ' + str(x))

# x中每一列对应的属性名称，1代表属于该类
print('属性名称为：', vec.get_feature_names())

# 把标签转换成 0 1表示
lb = preprocessing.LabelBinarizer()
y = lb.fit_transform(label)
print("标签y:", label)
print("转换后的标签y:" + str(y))

# 创建决策树模型
# criterion默认是gini，即CART算法，entropy是ID3算法
model = tree.DecisionTreeClassifier(criterion='entropy')
model.fit(x, y)

# 画出决策树

dot_data = tree.export_graphviz(model,
                                out_file=None,
                                feature_names=vec.get_feature_names(),
                                class_names=lb.classes_,
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('BuyComputer')
