import os
import json
import numpy as np

image_folder = './2024_02_24_02_03_23'
output_file = 'transforms.json'

def read_transform_matrix(data):
    if 'cameraPoseARFrame' in data:
        matrix = np.array(data['cameraPoseARFrame']).reshape(4, 4)
        return matrix.tolist()
    else:
        return None

frames = []
for file in sorted(os.listdir(image_folder)):
    if file.endswith('.json'):
        json_path = os.path.join(image_folder, file)
        img_file = file.replace('.json', '.jpg')
        
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        transform_matrix = read_transform_matrix(data)
        frames.append({
            "file_path": f"images/{img_file}",
            "transform_matrix": transform_matrix
        })

transforms = {
    "frames": frames
}

with open(output_file, 'w') as f:
    json.dump(transforms, f, indent=4)

print(f'transforms.json creado para {image_folder}')

with open(output_file, 'w') as f:
    json.dump(transforms, f, indent=4)

    # Ask for confirmation before deleting
    confirmation = input(f"Quieres eliminar todos los archivos .json de {image_folder}? (y/n): ")

    if confirmation.lower() == "y":
        # Delete all .json files in the folder
        for file in os.listdir(image_folder):
            if file.endswith('.json'):
                file_path = os.path.join(image_folder, file)
                os.remove(file_path)
        print("Archivos .json eliminados.")
