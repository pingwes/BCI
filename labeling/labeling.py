import json
import csv
import os


labeling_directory = os.listdir('data')
f = open("data/data"+ str(len(labeling_directory)) + ".csv", "w")
writer = csv.writer(f)

channels = ["CP3","C3","F5","PO3","PO4","F6","C4","CP4"]
header = [(channel + '_' + str(i)) for channel in channels for i in range(0, 16)]

header.append("label")
writer.writerow(header)

bw_dir = '../brainwave/data'
key_dir = '../key/data'
scroll_dir = '../scroll/data'

for filename in os.listdir(bw_dir):

    file = os.path.join(bw_dir, filename)
    if not os.path.isfile(file): continue

    # bw_data = open(file, "r")
    print(filename)





#
# def matrices_to_row():
#     row = []
#     for matrix in data:
#         for vector in matrix:
#             row.append(vector)
#     return row
#
# def create_label(string):
#     string = string.lower()
#     if string == "key.down" or string == "scroll_down":
#         return "down"
#     elif string == "key.up" or string == "scroll_up":
#         return "up"
#     else:
#         return "neutral"
#
#
# key_directory = 'data/key'
# bw_directory = 'data/brainwave'
# mouse_directory = 'data/mouse'
# key_objs = []
# #
# # for filename in os.listdir(key_directory):
# #     file = os.path.join(key_directory, filename)
# #     # checking if it is a file
# #     if os.path.isfile(file):
# #         key_data = open(file, "r")
# #         for line in key_data:
# #             obj = json.loads(line)
# #             key_objs.append(obj)
#
# mouse_objs = []
# total_rows = 0
#
# for filename in os.listdir(mouse_directory):
#     file = os.path.join(mouse_directory, filename)
#     # checking if it is a file
#     if os.path.isfile(file):
#         mouse_data = open(file, "r")
#         print(file)
#         for line in mouse_data:
#             obj = json.loads(line)
#             mouse_objs.append(obj)
#
# print("Mouse objects count: " + str(len(mouse_objs)))
#
# mouse_count = 0
# key_count = 0
# neutral_count = 0
#
# for filename in os.listdir(bw_directory):
#     file = os.path.join(bw_directory, filename)
#     if os.path.isfile(file):
#         bw_data = open(file, "r")
#         print(file)
#
#         for bw in bw_data:
#             bw_obj = json.loads(bw[:-2])
#             time = bw_obj["info"]['startTime']/1000
#             data = bw_obj['data']
#
#             mouse_found = False
#             key_found = False
#
#             for key in key_objs:
#                 if abs(key['time'] - time) < .01:
#                     row = matrices_to_row(data)
#                     label = create_label(key['key'])
#                     if label:
#                         key_count += 1
#                         row.append(label)
#                         total_rows += 1
#                         writer.writerow(row)
#                     key_found = True
#
#             for mouse in mouse_objs:
#                 if abs(mouse['time'] - time) < .01:
#                     row = matrices_to_row(data)
#                     label = create_label(mouse['input'])
#                     if label:
#                         mouse_count += 1
#                         row.append(label)
#                         total_rows += 1
#                         writer.writerow(row)
#                     mouse_found = True
#
#             if not key_found and not mouse_found:
#                 # if neutral_count < mouse_count:
#                 row = matrices_to_row(data)
#                 neutral_count += 1
#                 row.append("neutral")
#                 total_rows += 1
#                 writer.writerow(row)
#
# print("Total rows: " + str(total_rows))
# f.close()
