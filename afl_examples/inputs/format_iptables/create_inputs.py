import os
import yaml


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
with open('sample_website.yaml', 'r') as f:
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
        all_keys.extend(list(point['iptables'].keys()))
    except KeyError:
        print('KeyError')
all_keys = list(set(all_keys))
all_keys.sort()

os.makedirs('iptables', exist_ok=True)
for file_counter, point in enumerate(data):
    output = ''
    try:
        for key in all_keys:
            if key in point['iptables']:
                output = output + str(point['iptables'][key])
            
            output = output + '\n'
    except KeyError:
        print('KeyError')
    
    with open(f'iptables/in_{file_counter}.txt', 'w') as f:
        f.write(output)


# To be used inside the program
# Create required code segment
# This will set the variables
# You can use this one in many different modules
with open(f'arguments_code.py', 'w') as f:
    f.write('# AUTO GENERATED CODE START -----------------------------------------------------------------\n')
    f.write('temp_args ={\n')
    f.writelines(['\t\'' + a+'\': vars[' + str(counter) + '],\n' for counter, a in enumerate(all_keys)])
    f.write('}\n')
    f.write('remove_keys = []\n')
    f.write('for key in temp_args:\n')
    f.write('\tif temp_args[key] == \'\':\n')
    f.write('\t\tremove_keys.append(key)\n')
    f.write('for key in remove_keys:\n')
    f.write('\tdel temp_args[key]\n')
    f.write('set_module_args(temp_args)\n')
    f.write('# AUTO GENERATED CODE END -------------------------------------------------------------------\n')

