import os

online_names = []
n = 0
file_list = os.listdir('/Users/moxie/PycharmProjects/peiqi_new/online/')


for file in file_list:
    online_names.append(str(str(file).split('+')[0]))
    old_name = '/Users/moxie/PycharmProjects/peiqi_new/online/' + str(file)
    new_name = '/Users/moxie/PycharmProjects/peiqi_new/online/' + str(file.split('+')[0]) + '.json'
    os.rename(old_name, new_name)
    n += 1
