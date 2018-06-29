
"""
作者：Isabella
时间：2018/6/19
题目：下载进度条 —— 创建一个表示下载进度的进度条
参考：https://blog.csdn.net/programmer_yf/article/details/80512428

思路：
1. 确定文件大小
2. 获取实时下载进度
3. 绘制下载进度

"""
import time
import requests

def downloader(url, path):
    start = time.time()
    size = 0
    response = requests.get(url, stream = True)
    # 每次下载的数据大小
    chunk_size = 1024
    # 文件总大小
    content_size = int(response.headers['content-length'])

    if response.status_code == 200:
        print('文件大小：%0.2f MB' % (content_size / chunk_size / 1024))

        with open(path,'wb') as file:
            for data in response.iter_content(chunk_size = chunk_size):
                file.write(data)
                # 已下载文件大小
                size += len(data)
                # 从指定行第一个字符开始，搭配end=''属性完成覆盖进度条
                print('\r' +'下载进度：%s%.2f%%' % ('>'*int(size*50/content_size),float(size/content_size*100)),end='')
    end = time.time()

    print('\n'+'全部下载完成！用时 %.2f秒' % (end - start))

if __name__ == '__main__':
    url = 'https://newcontinuum.dl.sourceforge.net/project/eric-ide/eric6/stable/18.06/eric6-18.06.zip'
    downloader(url = url,path='eric.zip')


