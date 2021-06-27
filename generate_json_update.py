import os
import PIL.Image as Image
import json


root = 'your path'

test_json = os.path.join(root, 'test')  # test image root
out_file = os.path.join(root, 'test.json')  # test json output path 生成json的位置  

data = {}
data['categories'] = [{'id': 1, 'name': 'pig', 'supercategory': 'none'}] # 数据集的类别
idx = 100  # 自己设定 id
images = []
for name in os.listdir(test_json):
    
    file_path = os.path.join(test_json, name)
    file = Image.open(file_path)
    tmp = dict()
    tmp['id'] = idx
    idx += 1
    tmp['width'] = file.size[0]
    tmp['height'] = file.size[1]
    tmp['file_name'] = name
    images.append(tmp)

data['images'] = images
with open(out_file, 'w') as f:
    json.dump(data, f)

# with open(out_file, 'r') as f:
#     test = json.load(f)
#     for i in test['categories']:
#         print(i['id'])
print('finish')