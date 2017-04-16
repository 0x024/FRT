## 0x00 预览：
![](https://github.com/0x024/FRT/blob/master/data/temp/exp.png) 
## 0x01 环境:
[![](https://img.shields.io/badge/Ubuntu-16.04LTS-brightgreen.svg)]()
[![](https://img.shields.io/badge/Python-2.7-brightgreen.svg)]()
[![](https://img.shields.io/badge/OpenCV-3.2.0-brightgreen.svg)]()
[![](https://img.shields.io/badge/Mysql-5.7.*-brightgreen.svg)]()
[![](https://img.shields.io/badge/phpmyadmin-*-brightgreen.svg)]()
[![](https://img.shields.io/badge/ShadowSocks-Linux-brightgreen.svg)]()

```
curl安装：
	sudo apt-get install curl
```

```python
MySQLdb安装：
      sudo apt-get install python-pip     
      sudo apt-get install libmysqlclient-dev
      pip install mysql-python
```
OpenCV 3.2.0——-关于如何安装OpenCV，这里就简单的说一下下，


```
安装依赖包:
      sudo apt-get install build-essential
      sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
      sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev                                   libjasper-dev libdc1394-22-dev
```

```
从github上下载OpenCV最新的源码:
      git clone https://github.com/opencv/opencv.git       #这个是最新的OpenCV 公布在github上的代码
      git clone https://github.com/opencv/opencv_contrib.git #这个里面有一些模块，比如freetype，face，等需要用到
```
官网的教程里面将两个包分开进行编译，但是里面的许多包我们确实用不到，所以，最好的办法，就是将./opencv_contrib/moudles/freetype和face文件夹直接复制到./opencv/moudles/下

``` 
进行安装
	cd ~/opencv
	mkdir release
	cd release
	cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
	make -j4  #这里的-j4代表怎么说好呢，反正越大，编译的速度越快
	sudo make install
```
这里说一下了。在运行cmake的时候，需要下载几个文件，比如
```
ippicv_linux_20151201.tgz，
```
需要挂代理，，关于如何在ubuntu上安装shadowsocks科学上网，我的博客也有写过，


## 0x02 目录树:
![image](https://github.com/0x024/FRT/blob/master/data/temp/tree.png)


## 0x03 执行:

```
运行前，

	需要将./face/FaceAPI.py中的api_key和api_secret换成你的
	(为了便于您测试,我以将我的key放在里面，为了防止多人使用outer_id冲突，希望您后期换成自己的)
	需要将./face/FaceAPI.py中的outer_id设置成自己喜欢的标识
	需要在搭建的MYSQL中创建一个FRT数据库，并且事先在FRT中创建一个表，表名和值可任意设置！
	需要将./face/Dbconnect.py中的数据库信息换成自己的
	需要将所有的图片ID设置成12位数字
	如果需要重新导入或者识别同一张照片，需要在.data/log/*.log 删除对应log即可
```


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
