import hashlib

# 创建一个空字典，用于存放解析后的txt
dictionary = []
# r为仅读模式read
with open(r'hashtest/PasswordDictionary.txt', 'r') as f:
    # 多行代码文本需要用readlines，readline只读一行
    # readlines的返回为一个列表
    txt = f.readlines()

# 遍历每一行，读取的时候会有换行符，把换行符删了
for i in txt:
    dictionary.append(i.replace('\n', ''))


# sha512加密方法
def sha512_hash(string):
    sha512 = hashlib.sha512()
    sha512.update(string.encode('utf-8'))
    return sha512.hexdigest()

# 拿文件夹每个内容去尝试和密文列表的内容比较，这就是字典撞击


def dictionary_attack(dictionary, hashes):
    # 撞击成功答案
    cracked_passwords = {}
    # 遍历txt文本
    for password in dictionary:
        # 加密成sha512密码
        hash_ = sha512_hash(password)
        # 如果加密出来的密码位于密文列表中，则该明文是答案
        if hash_ in hashes:
            cracked_passwords[hash_] = password
            print(f"Password cracked: {hash_} => {password}")
    # 返回答案
    return cracked_passwords


# Test with a sample dictionary and a list of hashes
passwords_to_crack = ['31a3423d8f8d93b92baffd753608697ebb695e4fca4610ad7e08d3d0eb7f69d75cb16d61caf7cead0546b9be4e4346c56758e94fc5efe8b437c44ad460628c70',
                      '9381163828feb9072d232e02a1ee684a141fa9cddcf81c619e16f1dbbf6818c2edcc7ce2dc053eec3918f05d0946dd5386cbd50f790876449ae589c5b5f82762',
                      'a02f6423e725206b0ece283a6d59c85e71c4c5a9788351a24b1ebb18dcd8021ab854409130a3ac941fa35d1334672e36ed312a43462f4c91ca2822dd5762bd2b',
                      '834bd9315cb4711f052a5cc25641e947fc2b3ee94c89d90ed37da2d92b0ae0a33f8f7479c2a57a32feabdde1853e10c2573b673552d25b26943aefc3a0d05699',
                      '0ae72941b22a8733ca300161619ba9f8314ccf85f4bad1df0dc488fdd15d220b2dba3154dc8c78c577979abd514bf7949ddfece61d37614fbae7819710cae7ab',
                      '6768082bcb1ad00f831b4f0653c7e70d9cbc0f60df9f7d16a5f2da0886b3ce92b4cc458fbf03fea094e663cb397a76622de41305debbbb203dbcedff23a10d8a',
                      '0f17b11e84964b8df96c36e8aaa68bfa5655d3adf3bf7b4dc162a6aa0f7514f32903b3ceb53d223e74946052c233c466fc0f2cc18c8bf08aa5d0139f58157350',
                      'cf4f5338c0f2ccd3b7728d205bc52f0e2f607388ba361839bd6894c6fb8e267beb5b5bfe13b6e8cc5ab04c58b5619968615265141cc6a8a9cd5fd8cc48d837ec',
                      '1830a3dfe79e29d30441f8d736e2be7dbc3aa912f11abbffb91810efeef1f60426c31b6d666eadd83bbba2cc650d8f9a6393310b84e2ef02efa9fe161bf8f41d',
                      '3b46175f10fdb54c7941eca89cc813ddd8feb611ed3b331093a3948e3ab0c3b141ff6a7920f9a068ab0bf02d7ddaf2a52ef62d8fb3a6719cf25ec6f0061da791'
                      ]


# Perform the dictionary attack
cracked_passwords = dictionary_attack(dictionary, passwords_to_crack)
