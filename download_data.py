from roboflow import Roboflow
rf = Roboflow(api_key="r6C04SAbekzFdxM6iyIp")
project = rf.workspace("clgd2").project("cat-vqyem")
version = project.version(3)
dataset = version.download("yolov8") 