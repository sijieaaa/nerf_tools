# nerf_tools

A combination of both LLFF and torch-ngp for better NeRF processing.

- https://github.com/Fyusion/LLFF
- https://github.com/ashawkey/torch-ngp



Usage

data/fern/images/1.png 2.png ...
```
LLFF: 
python imgs2poses.py data/fern
python resize_images_4_8.py data/fern

torch-ngp:
python scripts/llff2nerf.py data/fern
python main_nerf.py data/fern --workspace trial_nerf -O --gui
```

