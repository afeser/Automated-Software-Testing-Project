import os
import yaml

# Please change to what you need
# This needs to be same as the name of the module inside yaml file (e.g. "apt:")
TARGET_DIRECTORY = 'systemd'

# You can change if you need
SOURCE_YAML = 'sample_website.yaml'

# Do everything inside this folder

os.chdir(TARGET_DIRECTORY)
def get_corresponding_string(value: int):
    """
    Return corresponding string.
    a -> 0
    b -> 1
    ...
    """
    value = value + 10
    out = ''
    while value > 0:
        out = out + chr(97+value%10)
        value = value // 10
    
    return out


# Read the copied file
with open(SOURCE_YAML, 'r') as f:
    lines = f.readlines()

# for counter, line in enumerate(lines):
#     # print(counter, line)
#     if '- ' in line:
#         lines[counter] = line.replace('- ', get_corresponding_string(counter))


lines = ''.join(lines)

data = yaml.safe_load(lines)

all_keys = []
# first pass, get the keys and order them
for point in data:
    try:
        all_keys.extend(list(point[TARGET_DIRECTORY].keys()))
    except KeyError:
        print('KeyError')
all_keys = list(set(all_keys))
all_keys.sort()

os.makedirs('inputs', exist_ok=True)
for file_counter, point in enumerate(data):
    output = ''
    try:
        for key in all_keys:
            if key in point[TARGET_DIRECTORY]:
                output = output + str(point[TARGET_DIRECTORY][key])
            
            output = output + '\n'
    except KeyError:
        print('KeyError')
    
    with open(f'inputs/in_{file_counter}.txt', 'w') as f:
        f.write(output)


# To be used inside the program
# Create required code segment
# This will set the variables
# You can use this one in many different modules
with open(f'arguments_code.py', 'w') as f:
    def write(line):
        """You can add a specific character to each line if you wish!"""
        f.write('    ') # i need 1 tab...
        f.write(line)
    
    write('# AUTO GENERATED CODE START -----------------------------------------------------------------\n')
    write('temp_args ={\n')
    [write('    \'' + a+'\': vars[' + str(counter) + '],\n') for counter, a in enumerate(all_keys)]
    write('}\n')
    write('remove_keys = []\n')
    write('for key in temp_args:\n')
    write('    if temp_args[key] == \'\':\n')
    write('        remove_keys.append(key)\n')
    write('for key in remove_keys:\n')
    write('    del temp_args[key]\n')
    write('set_module_args(temp_args)\n')
    write('# AUTO GENERATED CODE END -------------------------------------------------------------------\n')

