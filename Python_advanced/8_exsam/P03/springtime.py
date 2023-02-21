def start_spring(**data):
    spring_object = {}
    result = []

    for value, key in data.items():
        if key not in spring_object:
            spring_object[key] = []
        spring_object[key].append(value)

    spring_object = sorted(spring_object.items(), key=lambda kvp:(-len(kvp[1]), kvp[0]))

    for spring_obj, values in spring_object:
        result.append(f"{spring_obj}:")
        for v in sorted(values):
            result.append(f"-{v}")

    return '\n'.join(result)

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
