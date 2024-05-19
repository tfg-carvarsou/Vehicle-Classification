import os
import subprocess

def get_latest_directory(source, filename):
    # Use find to locate all directories containing the specified file
    find = subprocess.run(['find', source, '-name', filename], capture_output=True, text=True)

    # Parse the output to find the latest directory
    paths = find.stdout.strip().split('\n')
    latest_dir = None
    latest_index = -1
    for path in paths:
        if path:
            directory = os.path.dirname(path)
            dir_name = os.path.basename(directory)
            if dir_name == 'exp':
                index = 0
                if index > latest_index:
                    latest_index = index
                    latest_dir = directory
            if dir_name.startswith('exp') and dir_name[3:].isdigit():
                index = int(dir_name[3:])
                if index > latest_index:
                    latest_index = index
                    latest_dir = directory
    return latest_dir

def get_results(source, dest, list_images):
    dest = os.path.join(dest, 'results')
    os.makedirs(dest, exist_ok=True)

    for img in list_images:
        img_name = os.path.basename(img)
        latest_dir = get_latest_directory(source, img_name)
        
        if latest_dir:
            s = os.path.join(latest_dir, img_name)
        else:
            raise FileNotFoundError(f"{img_name} not found in any 'exp' directories")
        
        print(f"Copying {img_name} from {s}")
        subprocess.run(['cp', s, dest])