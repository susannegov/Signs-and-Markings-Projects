# author: quant61
# Link: https://github.com/tensorflow/models/issues/1601
from object_detection.protos.string_int_label_map_pb2 import StringIntLabelMap, StringIntLabelMapItem
from google.protobuf import text_format


def convert_classes(classes, start=1):
    msg = StringIntLabelMap()
    for id, name in enumerate(classes, start=start):
        msg.item.append(StringIntLabelMapItem(id=id, name=name))

    text = str(text_format.MessageToBytes(msg, as_utf8=True), 'utf-8')
    return text


if __name__ == '__main__':
    labels = ['no left turn sign','except with ut permit sign',
    'turning vehicle yield symbol to ped symbol sign',
    'bicyclists must use ped signal sign','no right turn on red sign',
    'street name sign','left turn yield on flashing yellow arrow sign',
    'no right turn sign','dont block the box sign',
    'left turn not protected sign','left turn yield on green sign',
    'turning vehicle yield to ped sign','one way arrow sign',
    'left turn only sign','straight arrow only sign','red parking tow sign',
    'left turn signal sign','green bus sign','do not block intersection sign',
    'except bicycle sign','straight right turn sign',
    'no left turn except bicycles','bike symbol may use full lane sign',
    'do not enter sign','straight left turn sign','right turn only sign',
    'no train horn sign','no ped crossing symbol use arrow sign']
    txt = convert_classes(labels)
    print(txt)
    with open('label_map.pbtxt', 'w') as f:
        f.write(txt)
