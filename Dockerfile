FROM python:3.9-alpine
RUN sed -i 's/https/http/' /etc/apk/repositories
RUN apk add curl
WORKDIR /data/meetingroom
ENV server_params=
COPY requirements.txt ./
RUN apk add --update --no-cache curl jq py3-configobj py3-pip py3-setuptools python3 python3-dev \
  && apk add --no-cache gcc g++ jpeg-dev zlib-dev libc-dev libressl-dev musl-dev libffi-dev \
  && python -m pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del gcc g++ libressl-dev musl-dev libffi-dev python3-dev \
  && apk del curl jq py3-configobj py3-pip py3-setuptools \
  && rm -rf /var/cache/apk/*
COPY . .
EXPOSE 8000
CMD ["/bin/sh", "/data/meetingroom/bash_command/start.local.bat"]

# apk add --update --no-cache add安装之前先最新本地镜像源，不用任何本地的缓存
# RUN 是在 docker build时运行
# CMD 是在 docker run 时运行 相当于run的时候默认带上这条命令 但是可以被docker run命令中的shell命令(外部CMD)代替
# 1. 可以用shell格式：CMD echo $HOME 等价于 CMD [ "sh", "-c", "echo $HOME" ]
# 2. 推荐使用的格式是exec 格式：CMD ["可执行文件", "参数1", "参数2"...] eg:CMD ["nginx", "-g", "daemon off;"]
# 3. 还有一种作用是参数列表格式：因为ENTRYPOINT可以不被docker run命令中的shell命令代替
# 那么run命令的shell命令(外部CMD)可以作为ENTRYPOINT的额外后置参数（场景一）
# 运行ENTRYPOINT ["docker-entrypoint.sh"]后，用内部CMD作为默认参数，外部CMD作为动态参数

# ARG 是在 docker build时运行
# ENV 在bulid和run过程都生效

# EXPOSE 8000 帮助镜像使用者理解这个镜像服务的守护端口，以方便配置宿主机端口映射到8000。

