# CLGDD - 玉米叶病害检测系统

基于 YOLOv8 的玉米叶片病害检测系统，用于识别以下病害类型：
- 灰斑病 (Gray Leaf Spot)
- 北方叶枯病 (Northern Leaf Blight)
- 南方叶枯病 (Southern Leaf Blight)

## 项目结构
```
CLGDD/
├── CAT-3/              # 数据集目录
├── ultralytics/        # YOLOv8 核心代码
├── quick_train.py      # 快速训练脚本
├── requirements.txt    # 项目依赖
└── README.md          # 项目说明
```

## 环境要求
- Python 3.8+
- PyTorch 2.0+
- 其他依赖见 requirements.txt

## 快速开始

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行训练：
```bash
python quick_train.py
```

## 版本说明

### v0.1.0 (2024-03-12)
- 初始版本
- 实现基础的模型训练功能
- 支持三种玉米叶片病害的检测
- 使用 YOLOv8-nano 模型进行快速训练测试

## 待办事项
- [ ] 优化模型性能
- [ ] 添加验证集评估指标
- [ ] 实现模型导出功能
- [ ] 添加 Web 界面

## 许可证
本项目采用 MIT 许可证。详见 LICENSE 文件。 