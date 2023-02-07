import os

def save_extensions(dir_name,first_level=False):
    for file_name in os.listdir(dir_name):
        file = os.path.join(dir_name,file_name)
        if os.path.isfile(file):
            extension = file_name.split('.')[-1]
            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(file_name)
        elif os.path.isdir(file) and not first_level:
            save_extensions(file + "/" + file_name,first_level=True)


directory = input()
extensions = {}
result = []

extensions = sorted(extensions.items(), key=lambda kvp: kvp[0])
print(extensions)

for key, value in extensions:
    result.append(f".{key}")

    for file in sorted(value):
        result.append(f"- - - {file}")

with open("report.txt", "w") as file:
    file.write('\n'.join(result))
