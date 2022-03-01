import numpy as np
import random
from skimage import io
from skimage import img_as_ubyte
import argparse
import os
import sys
from xml.dom.minidom import Document
import json
from mlagents.envs.environment import UnityEnvironment
from utils import * 

parser = argparse.ArgumentParser(description='outputs')
parser.add_argument('--setting',default='./settings/FSL-NV.json',type=str, help='./target dataset and attribute definition')
parser.add_argument('--train_mode',type=str2bool, nargs='?',
                        const=True, default=False, help="Whether to run the environment in training or inference mode")
parser.add_argument('--random_inference',type=str2bool, nargs='?',
                    const=True, default=True, help="Whether to run the environment in training or inference mode")
parser.add_argument('--env_path', type=str, default='./Build-win/Unity Environment.exe')
parser.add_argument('--out_lab_file', type=str, default='label.xml')

opt = parser.parse_args()
env_name = opt.env_path # is ./Build-linux/ if linux is used
train_mode = opt.train_mode  # Whether to run the environment in training or inference mode

print("Python version:")
print(sys.version)

# check Python version
if (sys.version_info[0] < 3):
    raise Exception("ERROR: ML-Agents Toolkit (v0.3 onwards) requires Python 3")
if (not os.path.exists("./train2014") and train_mode == False):
    raise Exception("The inference mode requre background images")

# env = UnityEnvironment(file_name=None)
env = UnityEnvironment(file_name=env_name) # is None if you use Unity Editor
# Set the default brain to work with

default_brain = env.brain_names[0]
brain = env.brains[default_brain]
# distance_bias = 12.11

print ("Begin generation")

random.seed(1)
np.random.seed(1)

doc = Document()
TrainingImages = doc.createElement('TrainingImages')
TrainingImages.setAttribute("Version", "1.0")  
doc.appendChild(TrainingImages)
Items = doc.createElement('Items')
Items.setAttribute("number", "-")  
TrainingImages.appendChild(Items)

def get_save_images_by_attributes(attribute_list, control_list, cam_id, dataset_size, output_dir, generated_num):
    if not os.path.isdir(output_dir):  
        os.mkdir(output_dir)
    z = generated_num
    cnt = generated_num

    angle_inx = order_list.index("orientation")
    inplane_rot_idx = order_list.index("in-plane rotation")
    Cam_height_idx = order_list.index("camera height")
    Cam_distance_idx = order_list.index("camera distance")
    Light_int_idx = order_list.index("light intensity") 
    Light_dir_idx = order_list.index("light direction")

    if opt.random_inference:
        inplane_rot = np.random.uniform(min(control_list[inplane_rot_idx]), max(control_list[inplane_rot_idx]), size=dataset_size * 3)
        angle = np.random.uniform(min(control_list[angle_inx]), max(control_list[angle_inx]), size=dataset_size * 3)
        temp_intensity_list = np.random.uniform(min(control_list[Light_int_idx]), max(control_list[Light_int_idx]), size=dataset_size * 3)
        temp_light_direction_x_list = np.random.uniform(min(control_list[Light_dir_idx]), max(control_list[Light_dir_idx]), size=dataset_size * 3)
        Cam_height_list = np.random.uniform(min(control_list[Cam_height_idx]), max(control_list[Cam_height_idx]), size=dataset_size * 3)
        Cam_distance_y_list = np.random.uniform(min(control_list[Cam_distance_idx]), max(control_list[Cam_distance_idx]), size=dataset_size * 3)
    else:
        inplane_rot = np.random.permutation (ancestral_sampler_fix_sigma(mu = attribute_list[inplane_rot_idx:inplane_rot_idx + 3], size=dataset_size * 3, length = 3))
        angle = np.random.permutation (ancestral_sampler(mu = attribute_list[angle_inx:angle_inx + 6], sigma = [200 for i in range(6)], size=dataset_size * 3, length = 6))
        temp_intensity_list = np.random.normal(loc=attribute_list[Light_int_idx], scale=np.sqrt(0.4), size=dataset_size * 3)  
        temp_light_direction_x_list = np.random.normal(loc=attribute_list[Light_dir_idx], scale=np.sqrt(50), size=dataset_size * 3)
        Cam_height_list = np.random.normal(loc=attribute_list[Cam_height_idx], scale=0.5, size=dataset_size * 3) 
        Cam_distance_y_list = np.random.normal(loc=attribute_list[Cam_distance_idx], scale=0.5, size=dataset_size * 3) 
    cam_str = "c" + str(cam_id).zfill(3)
    env_info = env.reset(train_mode=True)[default_brain]
    while cnt < dataset_size:
        done = False
        angle[z] = 90 #angle[z] % 360
        inplane_rot[z] = 180
        temp_intensity_list[z] = min(max(min(control_list[Light_int_idx]), temp_intensity_list[z]), max(control_list[Light_int_idx]))
        temp_light_direction_x_list[z] = min(max(min(control_list[Light_dir_idx]), temp_light_direction_x_list[z]), max(control_list[Light_dir_idx]))
        Cam_height_list[z] = min(max(min(control_list[Cam_height_idx]), Cam_height_list[z]), max(control_list[Cam_height_idx]))
        Cam_distance_y_list[z] = min(max(min(control_list[Cam_distance_idx]), Cam_distance_y_list[z]), max(control_list[Cam_distance_idx]))
        while angle[z] < 0:
            angle[z] =  angle[z] + 360
        while Cam_height_list[z]**2 + Cam_distance_y_list[z]**2 < 0.6 or abs(Cam_height_list[z]) < 0.1 or abs(Cam_distance_y_list[z]) < 0.1:
            if opt.random_inference:
                Cam_height_list[z] = np.random.uniform(min(control_list[Cam_height_idx]), max(control_list[Cam_height_idx]))
                Cam_distance_y_list[z] = np.random.uniform(min(control_list[Cam_distance_idx]), max(control_list[Cam_distance_idx]))
            else:
                Cam_height_list[z] = np.random.normal(loc=attribute_list[Cam_height_idx], scale=variance_list[Cam_height_idx])
                Cam_distance_y_list[z] = np.random.normal(loc=attribute_list[Cam_distance_idx], scale=variance_list[Cam_distance_idx])
        Cam_distance_x = 0 # random.uniform(-0.5, 0.5)
        scene_id = random.randint(1,59) 
        env_info = env.step([[angle[z], temp_intensity_list[z], temp_light_direction_x_list[z], Cam_distance_y_list[z], Cam_distance_x, Cam_height_list[z], inplane_rot[z], scene_id, train_mode, model_ID]])[default_brain] 
        done = env_info.local_done[0]
        car_id = int(env_info.vector_observations[0][4])
        color_id = int(env_info.vector_observations[0][5])
        type_id = int(env_info.vector_observations[0][6])
        if done:
            env_info = env.reset(train_mode=True)[default_brain]
            continue
        observation_gray = np.array(env_info.visual_observations[1])
        x, y = (observation_gray[0,:,:,0] > 0).nonzero()
        observation_gray[observation_gray > 0] = 1
        observation = np.array(env_info.visual_observations[0])
        if observation.shape[3] == 3 and len(y) > 0 and min(y) > 10: 
            print (cam_id, cnt, angle[z], temp_intensity_list[z], temp_light_direction_x_list[z], Cam_distance_y_list[z], Cam_distance_x, Cam_height_list[z], scene_id)
            ori_img = observation[0,min(x):max(x),min(y):max(y),:]
            seg_label = observation_gray[0,min(x):max(x),min(y):max(y),:]
            cnt = cnt + 1
            filename = "0" + str(car_id).zfill(4) + "_" + str(cnt) + ".jpg"
            filename_seg = "0" + str(car_id).zfill(4) + "_" + str(cnt) + "_seg "+ ".jpg"
            io.imsave(output_dir + filename,img_as_ubyte( ori_img))
            io.imsave(output_dir + filename_seg,img_as_ubyte( seg_label))
            Item = doc.createElement('Item')
            Item.setAttribute("typeID", str(type_id))  
            Item.setAttribute("imageName", filename)   
            Item.setAttribute("cameraID", cam_str)  
            Item.setAttribute("vehicleID", str(car_id).zfill(4))  
            Item.setAttribute("colorID", str(color_id))  
            Item.setAttribute("orientation",str(round(angle[z], 1)))
            Item.setAttribute("lightInt",str(round(temp_intensity_list[z], 1)))
            Item.setAttribute("lightDir",str(round(temp_light_direction_x_list[z], 1)))
            Item.setAttribute("camHei",str(round(Cam_height_list[z], 1)))
            Item.setAttribute("camDis",str(round(Cam_distance_y_list[z], 1)))
            Items.appendChild(Item)
        else:
            # cnt = cnt + 1
            # filename = "0" + str(car_id).zfill(4) + "_" + cam_str + "_" + str(cnt) + "_full.jpg"
            # io.imsave(output_dir + filename,img_as_ubyte( observation[0,:,:,:]))
            print ("object is not detected")
        z = z + 1

with open(opt.setting) as f:
    task_info = json.load(f)

for cam_id in range(0, task_info['camera number']):
    cam_info = task_info['camera list'][cam_id]
    model_ID = cam_info['camera id']  
    control_list, attribute_list, variance_list, order_list = get_cam_attr(cam_info)
    generated_num = cam_info['generated num'] if 'generated num' in cam_info else 0
    get_save_images_by_attributes(attribute_list, control_list, int(cam_info["camera id"]), cam_info['data size'], cam_info['output dir'], generated_num)

with open(opt.out_lab_file, 'wb') as f:
    f.write(doc.toprettyxml(indent='\t', newl = "\n", encoding='utf-8'))
f.close()  
