----

> 这个是原作者版本及文档说明，稳定版及发布的app可从他的github上进行下载

# Movie Catcher

搜索电影/美剧资源，集成热门资源站，借助某度网盘实现离线下载以及在线播放功能。

## 详见
[https://evilcult.github.io/moviecatcher](https://evilcult.github.io/moviecatcher/index.html)

## 使用说明
[传送门](https://github.com/EvilCult/moviecatcher/wiki/Application-Guide)





---

> 这里是我的个人修改版本，介于学习的目的，我会看情况给作者pull request的，目前已被作者merge的是第一次更新，因为时间原因(毕业告急:joy:)，更新会从浅层开始，偏向于一些(不用脑子的，懒)细节。



## 更新 2017.10.17

1. 新增豆瓣影评检索
2. 改善电影/电视剧注释
3. 修复启动无输入时的伪查询
4. 已通过测试，但没有重新生成app(Bl文件中多了一个setup.py属于误操作，请删除)，望知

![](https://camo.githubusercontent.com/1796775be96cbe73542737efdf61a939e65d3346/68747470733a2f2f7773312e73696e61696d672e636e2f6c617267652f303036744e6337396c7931666b69386764796964356a33306e79307a6b6863722e6a7067)



----



## 更新 2017.10.23

1. 新增 知乎话题，空值时默认搜索 "有哪些好看的影视"， 赋值时搜索 "如何评价 $赋值项"

2. 修改豆瓣影评，空值时默认跳转至 豆瓣电影 主页，赋值时正常搜索

3. 修复了一些奇奇怪怪但是我忘记了的bugs

4. 已通过mac端测试，发布版本位于 dist 目录下，mac用户自行食用，win用户，可根据packwin.spec 和 参考 [将自己的python程序打包成.exe/.app(秀同学一脸呐)](http://blog.csdn.net/mrlevo520/article/details/51840217) 进行打包，当然也可以下原作者的版本，毕竟我没有在本质上进行更新，只是一些tiny feature和fix bugs

   ​

![](https://ws2.sinaimg.cn/large/006tNc79ly1fl8sor7zv2j30pc11g1kx.jpg)



## Pay Attention

1. 程序的入口在，Bl目录下的App.py，所以从那开始读代码吧~(`python App.py`进行测试)


1. 关于打包文件过大问题，出现原因是自己装的包太多了，然后使用pyinstaller的时候会把没用的包都关联进去，所以刚开始没脑子的打包导致文件150M。。。解决方案是，使用anaconda的版本控制，新建一个虚拟环境，新的环境中只需要如下包即可，然后切到根目录下，执行 `pyinstaller packmac.spec `即可(win 的执行packwin.spec)

- altgraph==0.14
- certifi==2016.2.28
- dis3==0.1.1
- future==0.16.0
- image==1.5.16
- macholib==1.8
- olefile==0.44
- pefile==2017.9.3
- Pillow==4.3.0
- PyInstaller==3.3
- pytz==2017.2
- selenium==3.6.0

2. 还是没有修复mac端gui直接输入中文的bug。。。。。