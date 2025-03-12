from ultralytics import YOLO
import os
from ultralytics.utils import SETTINGS

def quick_train():
    # 获取当前工作目录的绝对路径
    current_dir = os.path.abspath(os.path.dirname(__file__))
    data_yaml = os.path.join(current_dir, 'CAT-3/data.yaml')
    
    # 设置数据集目录
    SETTINGS['datasets_dir'] = os.path.join(current_dir, 'CAT-3')
    
    # 加载最小的YOLOv8模型
    model = YOLO('yolov8n.pt')
    
    # 配置训练参数（快速测试用）
    results = model.train(
        data=data_yaml,          # 数据集配置文件
        epochs=1,                # 只训练1轮
        imgsz=320,              # 较小的图像尺寸
        batch=4,                # 较小的批次大小
        device='cpu',           # 使用CPU
        workers=0,              # CPU训练
        patience=1,             # 较小的早停耐心值
        project='test_runs',    # 项目名称
        name='quick_test',      # 实验名称
        exist_ok=True,          # 覆盖已存在的实验目录
        pretrained=True,        # 使用预训练权重
    )
    
    print("训练完成！")

if __name__ == "__main__":
    quick_train() 