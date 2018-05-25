# Django搭建Blog可以参考这里 https://www.cnblogs.com/fnng/p/3737964.html
## 项目目录介绍
### blog /
### admin.py  :  django 自带admin后面管理，将models.py 中表映射到后台。
### apps.py :  blog 应用的相关配置。
### models.py  : Django 自带的ORM，用于设计数据库表。
### tests.py  :  用于编写Django单元测试。
### veiws.py ：视图文件，用于编写功能的主要处理逻辑。

### mysite/
### settings.py ： 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
### urls.py ： 负责把URL模式映射到应用程序。
### wsgi.py :  用于项目部署。

### manage.py ： Django项目里面的工具，通过它可以调用django shell和数据库等。
