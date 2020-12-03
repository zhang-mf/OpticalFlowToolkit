from lib import flowlib as fl
from glob import glob
from os import path

flofiles = glob('./OF/fig8/*.flo')

for flo in flofiles:
    flow_Middlebury = fl.read_flow(flo)

    for i in range(0,35):
        # Find a color ring on the Net
        # Adjust `start point` and `distribution` to get the same Optical Flow of different color
        start_point = i/35.0
        distribution = [15,6,4,11,13,6]
        fl.save_flow_image(flow_Middlebury,'./result/fig8/%d.jpg'%(i),start_point,distribution)
    # break

    # start_point = 1/25#4*4+110
    # distribution = [15,6,4,11,13,6] # [15,6,4,11,13,6]
    # fl.save_flow_image(flow_Middlebury,'./result/fig8/%s_%d.jpg'%(path.basename(flo),start_point),start_point,distribution)
