# YOLO项目

这是一个基于YOLOv8的目标检测项目，支持多人远程协作开发。

## 环境要求

- CUDA 11.8+
- Docker
- Git

## 快速开始

1. 克隆项目
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. 构建Docker镜像
```bash
docker build -t yolo-project .
```

3. 运行Docker容器
```bash
docker run --gpus all -it --rm -v $(pwd):/workspace yolo-project
```

## 项目结构

```
.
├── Dockerfile          # Docker配置文件
├── requirements.txt    # Python依赖
├── ultralytics/       # YOLOv8核心代码
├── datasets/          # 数据集目录
└── models/            # 模型目录
```

## 开发指南

1. 创建新分支进行开发
```bash
git checkout -b feature/your-feature-name
```

2. 提交代码
```bash
git add .
git commit -m "your commit message"
git push origin feature/your-feature-name
```

3. 创建Pull Request进行代码审查

## 注意事项

- 请确保在开发新功能时创建新的分支
- 提交代码前请进行充分测试
- 遵循项目的代码规范
- 保持代码的可读性和可维护性

## 许可证

本项目基于YOLOv8开源协议 