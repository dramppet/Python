# def get_info(**kwargs):
#     return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"

def get_info(name,town,age):
    return f"This is {name} from {town} and he is {age} years old"

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))