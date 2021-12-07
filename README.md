## System introduction

Open source projects have always been something I want to do. I have seen many excellent Python open source projects. In order to exercise and improve the open source ability, I decided to use my spare time to write a background system modeled on other excellent open source systems. The technology stack includes Django + redis + celery + MySQL (SQLite is used in the early stage).

## System architecture 

![image-20211202081015030](https://cdn.jsdelivr.net/gh/jiac3366/image-host@master/mysqlbizhbihui/微信图片_202112020851041.447l0c2ht1c0.png)



## Built in function

![image-20211202080636982](https://cdn.jsdelivr.net/gh/jiac3366/image-host@master/recruitment/image.18f8q2k4cek.png)

1.  用户管理：管理员是系统操作者，该功能主要完成系统用户配置。
2.  角色管理：系统有面试官和HR两种角色，按角色进行数据范围权限划分。
3.  候选人管理：配置显示候选人头像，使用对象存储管理应聘者上传的的PDF。
4.  岗位管理：对招聘岗位进行编辑管理。
6.  钉钉通知：HR可以通知面试官及时给相应面试者进行面试，监控生产环境运行中出现的异常，并及时上报；
7.  定时任务：在线（添加、修改、删除)任务调度包含执行结果日志。
8.  数据可视化：结合AdminLTE 3开源，简历数据可视化大屏展示。
9.  服务监控：监视当前系统CPU、内存、磁盘、堆栈等相关信息。
10.  连接池监视：集成Sentry监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。
11.  云原生部署，提供部署至Docker的镜像，以及部署K8s环境的Yaml配置。
11.  CI/CD，使用Jenkins Pileline实施Devops，后期可以使用Github Action / Gitlab CICD

## Demo

<table>
    <tr>
        <td><img src="https://cdn.jsdelivr.net/gh/jiac3366/image-host@master/recruitment/d9cc940692e076efa5e5b961a3ac6f8.357jfhnm5zw0.png"/></td>
        <td><img src="https://cdn.jsdelivr.net/gh/jiac3366/image-host@master/recruitment/c225f3457bd5649c851ee8ec4a41d20.1v7klg955lj4.png"/></td>
    </tr>
    <tr>
        <td><img src="https://cdn.jsdelivr.net/gh/jiac3366/image-host@master/recruitment/图片4.3zskb8hr4vu0.png"/></td>
        <td><img src="https://cdn.jsdelivr.net/gh/jiac3366/image-host@master/recruitment/图片2.5ixzq5owm680.png"/></td>
    </tr>
    <tr>
        <td><img src="https://cdn.jsdelivr.net/gh/jiac3366/image-host@master/recruitment/微信图片_20211202091324.1hpge3cwn3gg.png"/></td>
        <td><img src="https://cdn.jsdelivr.net/gh/jiac3366/image-host@master/recruitment/cef78864090d81d4c51a9f857a55b09.4l2m3z32vii0.png"/></td>
    </tr>
</table>



## Experience

- guest/cadmin1234
- 演示地址：http://47.113.203.197:10086/



