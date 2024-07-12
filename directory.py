import requests
class Mulu:

    def __init__(self):
        pass

    def get_contents(self,file_path):  # 读字典文件文件
        with open(file_path, 'r', encoding='utf-8') as f:
            dict = f.read().splitlines()
        return dict

    def get_url(self, url , dict):  # 拼接URL
        url_ = []
        for value in dict:
            new_url ="http://" + url + "/" + value
            res = requests.get(new_url)
            if res.status_code == 200 or res.status_code == 302 or res.status_code == 403:  # 判断状态码
                url_.append(new_url)
        return url_

if __name__ == '__main__':

    mulu=Mulu()
    dict = mulu.get_contents("./dir.txt")
    url = input("请输入你需要扫描的网址:")
    print(f"结果为: {mulu.get_url(url, dict)}")
