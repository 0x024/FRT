

## 0x00 预览：
![](https://github.com/0x024/FRT/blob/master/data/temp/exp.png) 
## 0x01 环境:

- 最新环境配置请到我的博客查看

- [www.0x024.com](http://www.0x024.com) 

- 星期日, 30. 四月 2017 09:28下午 


## 0x02 目录树:

![image](https://github.com/0x024/FRT/blob/master/data/temp/tree.png)

## 0x03 执行:



```
python import.py   #将保存在./data/import/目录下的图片特征经分析后，将图片信息导入数据库，只可单人照片，要求图片清晰度较高
```
```
python search_img.py   #将需要识别的图片放在./data/search_img/下，完成后保存在本目录（可放置多张）
```
```
python search_cam.py   #实时识别人脸  (可识别多张脸)(Face++和深度学习一起识别)
```
```
python train_img.py   #将需要训练的图片放在./data/train_img，处理后会放在./data/at下，提供训练素材，要求图片清晰度较高(单个照片可多脸)
```
```
python train_cam.py   #实时识别人脸，将识别清楚的图片自动放置在./data/at/下，提供训练的素材
```
