# OCR-RecognitionSystem
Comprehensive design three

### 项目需求

​	本课题主要使用Python语言开发一个名片识别系统，该系统的核心是通过汉王云名片接口获取名片图片的信息，再保存到文件中，最后显示联系人信息到界面上。项目里主要用到了 PyQt5 模块绘制界面，汉王云名片接口获取名片信息、pandas 模块进行数据的保存以及处理、pyecharts 模块中的Pie模块根据联系人信息绘制联系人分布饼图。

具体的功能有：

1. 识别名片联系人信息；
2. 手动录入联系人信息；
3. 编辑联系人信息；
4. 搜索联系人信息；
5. 联系人分布省份饼图；
6. 删除联系人信息。

### 项目设计

​	主要分为了三个板块，分别是GUI、ToolClass、DatabaseClass，其中ToolClass 包括OCR、JsonDataDealer、PyechartGenerator、PhoneSearch，具体调用见下图：

![](https://hss-imgcloud.oss-cn-beijing.aliyuncs.com/img/2020/11/0920201109164623.png)

### TODO

#### 1、项目框架、接口

#### 2、项目的GUI设计与开发

#### 3、详细设计与开发

