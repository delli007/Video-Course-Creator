# Video Course Creator

A simple script to create a lightweight HTML5 webpage (front-end), based on bootstrap 5, for playing videos that you would get from an online course. The UI is similar to sites like Udemy or CBT-Nuggets, except not as nice, but it was designed to handle content from them. This is to make it easier to go through a video series offline, or to enable a webserver to host the files.

Features Include:
 - HTML5, responsive, Single Page Application based on Bootstrap. Only 3 files, and the python script can be removed after it generates the json.
 - Self contained, no calls to internet based resources.
 - Keeps track of the current video between browser restarts, uses the browsers localStorage.
 - Shows a badge next to the current video being played.
 - Continuous Play option.
 - Video Speed Control.
 - Dark theme so the video takes the main stage.
 - Recursively scans your folder structure for videos and resource files.
 

Usage
-----
To get started, copy these files to the root of the folder with your videos. There should be sub-folders containing video files and other resources. Each folder in the root will be the sorted and be turned into a module. All video files under the module folder will be sorted and added to the module. All other files will be sorted and turned into resource files.

To create the course, open a command prompt and run `python create_course.py`

A 'course-json.js' file will be created. Open 'course.html' and you
