from ultralytics import YOLO
import easyocr

import sys
import os

import cv2

file_path = os.path.dirname(os.path.abspath(__file__))

# input = sys.argv[1]

# if len(sys.argv) != 1:
#    print("incorrect argument")
#    sys.exit()

def croppedBox(img, box):
    obj = img[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
    return obj

def verify(input):
  image = input
  pathname = os.path.dirname(image)
  imagename = os.path.basename(image)
  imagenametext = list(os.path.splitext(imagename))
  img = cv2.imread(image)

  # reader = easyocr.Reader(['ko'], gpu=False)
  reader = easyocr.Reader(['ko'])

  card_model = YOLO(file_path + '/ultralytics/runs/detect/card_train/weights/best.pt')  # load a custom model
  card_results = card_model(source=image, save=False)


  for card_result in card_results:
      card_boxes = card_result.boxes.xyxy.tolist()
      card_clss = card_result.boxes.cls.cpu().tolist()
      card_names = card_result.names.keys()

      # 0:old_sign, 1:old_card, 2:new_sign, 3:new_card
      if (0 and 1) or (2 and 3) in card_names:
          for card_box, card_cls in zip(card_boxes, card_clss):
            # 만약 sign label이면 통과
            if (card_cls == 0) or (card_cls == 2):
              continue

            card_label = ""

            if card_cls == 1:
              card_label = "old_card_name_train"
            elif card_cls == 3:
              card_label = "new_card_name_train"

            card_img = croppedBox(img, card_box)

            # 이름 검출
            name_model_path = file_path + "/ultralytics/runs/detect/" + card_label + "/weights/best.pt"

            name_model = YOLO(name_model_path)
            name_results = name_model(source=card_img, save=False)

            for name_result in name_results:
              name_boxes = name_result.boxes.xyxy.tolist()
              name_clss = name_result.boxes.cls.cpu().tolist()
              name_names = name_result.names.keys()

              # 만약 검출된 이름이 없다면 통과
              if not 0 in name_names:
                continue

              for name_box, name_cls in zip(name_boxes, name_clss):
                name_img = croppedBox(card_img, name_box)

                ocr_result = reader.readtext(name_img)
                detected_name = ocr_result[0][1]

                print(detected_name)
                return(detected_name)
              
# verify(input=input)