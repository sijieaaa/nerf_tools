import shutil
from PIL import Image

import os
import argparse
import torchvision.transforms as TVT
import torchvision.transforms.functional as TVF
from tqdm import tqdm
def main(opt):
    scene_folder = opt.path
    # scene_folder = 'data/fern'


    images_folder = os.path.join(scene_folder, 'images')
    images4_folder = os.path.join(scene_folder, 'images_4')
    images8_folder = os.path.join(scene_folder, 'images_8')

    if os.path.exists(images4_folder):
        shutil.rmtree(images4_folder)
    os.mkdir(images4_folder)
    
    if os.path.exists(images8_folder):
        shutil.rmtree(images8_folder)
    os.mkdir(images8_folder)


    images_list = os.listdir(images_folder)
    images_list = sorted(images_list)

    for image_name in tqdm(images_list):
        image_path = os.path.join(images_folder,image_name)
        image4_path = os.path.join(images4_folder,image_name)
        image8_path = os.path.join(images8_folder,image_name)

        image = Image.open(image_path)
        w,h = image.size
        # a=min([w,h])

        image4 = TVT.Resize(
            min([w,h])//4,interpolation=TVF.InterpolationMode.BILINEAR)(image)
        image8 = TVT.Resize(
            min([w,h])//8,interpolation=TVF.InterpolationMode.BILINEAR)(image)



        image4.save(image4_path)
        image8.save(image8_path)

    return None


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help="root directory to the LLFF dataset (contains images/ and pose_bounds.npy)")

    opt = parser.parse_args()

    # main(1)
    main(opt)