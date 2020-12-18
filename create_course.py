#!/bin/env python3

import json
import os
import re
import subprocess


# Supplementary Functions

def get_video_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

def natural_keys(text):
    """For sorting strings that have numbers in them. usage: [].sort(key=natural_keys) """
    atoi = lambda text: int(text) if text.isdigit() else text
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def get_all_files(path, exclude_original_path=True):
    """Recursively gets all files in a directory. returns an array"""
    ret = []
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            fpath = subdir + os.sep + filename
            ret.append(fpath.replace(path + os.sep, '') if exclude_original_path else fpath)
    ret.sort(key=natural_keys)
    return ret


# Set our variables
video_extensions = [
    '.3gp','.3g2', '.3gpp',
    '.asf', '.wmv',
    '.avi',
    '.divx',
    '.mkv', '.mk3d',
    '.mp4','.m4p','.m4v',
    '.mpg','.mp2','.mpeg','.mpe','.mpv','.m2v',
    '.m2p', '.ps',
    '.ogv','.ogg', '.ogx',
    '.mts','.m2ts','.ts',
    '.mov','.qt',
    '.rm','.rmvb',
    '.yuv',
    '.svi',
    '.nsv',
    '.vob',
    '.webm'
]

content = {
    'title': 'Course Title',
    'description': '',
    'teachers': '',
    'modules': []
}

# Get some info about the course
content['title'] = input('What\'s the name of this course?\n > ')
content['description'] = input('Would you like to add a one-line description? [press ENTER to skip]\n > ')
content['teachers'] = input('Who are the teacher(s)? [separate multiple teachers with a comma]\n > ')

print('Turning the current folders directory structure into modules...')

# Turn the current folders sub-directories into modules
modules = os.listdir()
modules.sort(key=natural_keys)
for f in modules:
    if os.path.isdir(f):
        # In each "module" recursively get all files
        all_files = get_all_files(f)
        
        # Separate the videos and resources, and format the path for web
        videos = []
        resources = []
        for af in all_files:
            ext = '.' + af.split('.')[-1]
            if ext in video_extensions:
                videos.append(af.replace(os.sep, '/'))
            else:
                resources.append(af.replace(os.sep, '/'))

        # Append the module data
        mod = {
            'title': f, 
            'videos': videos,
            'resources': resources
            }
        content['modules'].append(mod)

# Save the json and we're done
print('Saving data to course-json.js...')
with open('course-json.js', 'w') as f:
    f.write("var courseContent=" + json.dumps(content, indent=2))

print('Complete! Open course.html to view the results.')
