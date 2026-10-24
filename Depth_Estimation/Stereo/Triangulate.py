from pathlib import Path 

root_directory = Path("/#/#/#")
K_l_target = "Camera-0-K: "; 
K_r_target = "Camera-1-K: "; 
K_l_target = "Camera-0-K"; 
K_l_target = "Camera-0-K"; 
for file_path in root_directory.rglob("camera_calibration.txt"):
    print("Calibration file found")
    for line in file_path: 
        if line.startswith(K_l_target):
            K_l = line.split(":", 1)[1].strip()
        if line.startswith(K_r_target):
            K_r = line.split(":", 1)[1].strip()

