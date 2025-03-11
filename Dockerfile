FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

# 设置工作目录
WORKDIR /workspace

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . /workspace/

# 安装Python依赖
RUN pip3 install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV PYTHONPATH="/workspace:${PYTHONPATH}"

# 设置默认命令
CMD ["bash"] 