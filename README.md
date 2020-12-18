# Video Course Creator

A simple script to create a lightweight HTML5 webpage (front-end), based on bootstrap 5, for playing videos that you would get from an online course. The UI is similar to sites like Udemy or CBT-Nuggets, except not as nice, but it was designed to handle content from them. This is to make it easier to go through a video series offline.


Usage
-----
To get started, copy these files to the root of the folder with your videos. There should be sub-folders containing video files and other resources. Each folder in the root will be the sorted and be turned into a module. All video files under the module folder will be sorted and added to the module. All other files will be sorted and turned into resource files.

To create the course, open a command prompt and run `python create_course.py'

A 'course-json.js' file will be created. Open 'course.html' and you
