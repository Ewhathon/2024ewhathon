from ultralytics import YOLO
from ultralytics.data.utils import autosplit

## card_train
autosplit(path='../../../data/card_data/data')

model = YOLO('yolov8m.pt')
results = model.train(
    data='../../../data/card_data/data.yaml',
    batch=16,
    epochs=50,
    name='card_train')


## old_card_name_train
autosplit(path='../../../data/name_data/old_card_data/data')

model = YOLO('yolov8m.pt')
results = model.train(
    data='../../../data/name_data/old_card_data/data.yaml',
    batch=16,
    epochs=50,
    name='old_card_name_train')


## new_card_name_train
autosplit(path='../../../data/name_data/new_card_data/data')

model = YOLO('yolov8m.pt')
results = model.train(
    data='../../../data/name_data/new_card_data/data.yaml',
    batch=16,
    epochs=50,
    name='new_card_name_train')

