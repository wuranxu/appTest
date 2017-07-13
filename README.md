Github地址: https://github.com/wuranxu
使用说明

1. 安装配置Mongo数据库
[下载地址](https://www.mongodb.com/dr/fastdl.mongodb.org/win32/mongodb-win32-x86_64-2008plus-ssl-3.4.6-signed.msi/download)
mongo是用来存放元素定位的，截图如下:
通过case_id区分每个case的元素定位
里面提供了value, method和text字段，分别作用是定位的值，定位的方法和要输入的文本内容。

![](http://upload-images.jianshu.io/upload_images/6053915-bfd44479b46c291a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2. 安装Redis
因为被墙，所以给个CSDN下载地址
[戳我下载](http://download.csdn.net/download/chainisit/9400072)
下载后解压，运行redis-server.exe就行
装Redis的原因， 是因为现在想第一个case初始化（包括登陆），其他的case就不需要重复操作了，到后面最后一个用例结束了之后再关掉driver。所以采用了Redis。
当然肯定有更好的方案，暂时先这样了。

![](http://upload-images.jianshu.io/upload_images/6053915-05b8b58858a88499.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3. 编写用例

除了需要登陆的第一个用例(继承于BaseNeedLogin)， 其他的用例都继承于Base类，重写了tearDownClass这类方法。
编写用例可参照Case002来编写，只需要写test函数就行了，记得带上装饰器(auto_pic），如果需要自动截图的话(现在是报错和正常，结束的时候都会截图)。

![](http://upload-images.jianshu.io/upload_images/6053915-bfcfc20b72c1b2d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

4. 运行用例
参照run_case.py文件里头的suite.addTest()方法，先导入用例，然后再run，后期会增加测试报告以及其他方法。

![](http://upload-images.jianshu.io/upload_images/6053915-5a7c7221985dc239.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

框架还不完整，会陆续补充更新的。
app是我们公司自带的， 易途8司导端，账号密码都在mongo数据库里存放了，如果有需要帮忙可以联系我，或者把测试的app改成支付宝这种。

联系方式： QQ619434176