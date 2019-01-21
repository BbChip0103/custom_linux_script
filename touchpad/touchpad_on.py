import subprocess

# result = subprocess.check_output("xinput list", shell=True)
# lines = [line for line in result.splitlines() 
#                 if line.find('TouchPad') != -1]
# touchpad_string = lines[0]

### 1-1
result = subprocess.check_output("xinput list", shell=True)
### 1-2
lines = result.splitlines()
### 1-3
touchpad_string = ''
for line in lines:
    if line.find('TouchPad') != -1:
        touchpad_string = line
        break
### 1-4
device_id = touchpad_string.split('\tid=')[1].split('\t')[0]
### 2-1
subprocess.call(['xinput', 'enable', device_id])

'''
1. get the touchpad's device id
    1-1. execute 'xinput list' command, and get stdout result
    1-2. parse lines
    1-3. if line in 'TouchPad' keyword, get the line.
    1-4. extract device id from line
2. enable touchpad by 'xinput enable {device id}' command
    2-1. execute command 'xinput enable {device_id}'
'''