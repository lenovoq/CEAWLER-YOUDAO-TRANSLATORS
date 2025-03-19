import requests

while True:
    wd = input('请输入翻译的单词：')
    if wd.lower() == 'exit' or wd.lower() == 'quit':
        print('感谢使用，再见！')
        break

    url = 'https://aidemo.youdao.com/trans'
    my_data = {
        'q': wd,
        'from': 'Auto',
        'to': 'Auto'
    }

    res = requests.post(url, data=my_data)
    print(res.json().get('translation')[0])

