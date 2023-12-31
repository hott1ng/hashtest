import hashlib


dictionary = []
with open('./PasswordDictionary.txt', 'r') as f:
    txt = f.readlines()
for i in txt:
    dictionary.append(i.replace('\n', ''))


# 替换规则
def mangle_words(word):

    word = word.lower()
    word = word.replace('$', 's')
    word = word.replace('!', 'i')

    return word


def dictionary_attack(hashed_password, dictionary):
    ans = {}
    # 遍历txt文件，加密成sha512密码
    for password in dictionary:
        hashed_attempt = hashlib.sha512(password.encode()).hexdigest()
        # 如果加密出来的密码位于列表中
        if hashed_attempt in hashed_password:
            # 在答案字典中存入{原文：密码}
            ans.update({password: hashed_attempt})
    # 把答案字典还原处理
    # 遍历字典，k为键password，v为值hashed_attempt
    for k, v in ans.items():
        # 把原文传入还原函数替换
        # 输出密码=>原文=>替换后的原文
        print(v, "=>", k, '=>', mangle_words(k))


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


dictionary_attack(passwords_to_crack, dictionary)
