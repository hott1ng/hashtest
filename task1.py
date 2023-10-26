import itertools as its
import string
import hashlib

# 设置字符集
charset = string.digits + string.ascii_lowercase
# 等同于
# charset = '0123456789abcdefghijklmnopqrstuvwxyz'


# sha512加密函数
def sha512encode(text):
    '''
    :param text: 明文
    :return: 加密后的值
    '''
    # 实例化sha512容器
    sha512 = hashlib.sha512()
    # 更新容器内容
    sha512.update(text.encode())
    # 返回值
    return sha512.hexdigest()

# 构造密码函数
def create_pwd(charset, goal):
    '''
    :param charset: 字符集
    :param goal: 解密目标
    :return: 匹配成功则返回
    '''
    k = 1
    while True:
        # 遍历所有可能，k为长度
        base = its.product(charset, repeat=k)

        # 遍历生成的所有可能
        for i in base:
            # 如果和目标一致
            if sha512encode(''.join(i)) == goal:
                # 则返回
                return ''.join(i)

        # 遍历所有可能完毕，未命中，长度+1，进入下一循环
        k+=1

# 目标列表
goal = ['f14aae6a0e050b74e4b7b9a5b2ef1a60ceccbbca39b132ae3e8bf88d3a946c6d8687f3266fd2b626419d8b67dcf1d8d7c0fe72d4919d9bd05efbd37070cfb41a',
        'e85e639da67767984cebd6347092df661ed79e1ad21e402f8e7de01fdedb5b0f165cbb30a20948f1ba3f94fe33de5d5377e7f6c7bb47d017e6dab6a217d6cc24',
        '4e2589ee5a155a86ac912a5d34755f0e3a7d1f595914373da638c20fecd7256ea1647069a2bb48ac421111a875d7f4294c7236292590302497f84f19e7227d80',
        'afd66cdf7114eae7bd91da3ae49b73b866299ae545a44677d72e09692cdee3b79a022d8dcec99948359e5f8b01b161cd6cfc7bd966c5becf1dff6abd21634f4b']



# 声明一个列表存放匹配成功的明文
ls = []

# 遍历目标列表，取每个目标的匹配结果
for i in goal:
    # 结果存入列表中
    ls.append(create_pwd(charset, i))

# 给ls列表排序，会sorted方法会返回一个新列表，原列表不修改
# list.sort()方法则是在远列表上进行修改
# key为排序方式，可自定义排序方式，key
# lambda 函数    :左侧为传入的形参，右侧为返回值
# 等价于
# def key(x):
#     return (len(x), x)
# 先按长度再按字典序
new_ls = sorted(ls, key=lambda x: (len(x), x))

# 遍历新列表，打印，每行结尾为空
for i in new_ls:
    print(i, end="")
