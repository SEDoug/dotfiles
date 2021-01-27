Step #9: Create your ‘py3cv4’ virtual environment
This step is dead simple once you’ve installed virtualenv and virtualenvwrapper in the previous step. The virtualenvwrapper tool provides the following commands to work with virtual environments:

mkvirtualenv: Create a Python virtual environment
lsvirtualenv: List virtual environments installed on your system
rmvirtualenv: Remove a virtual environment
workon: Activate a Python virtual environment
deactivate: Exits the virtual environment taking you back to your system environment
Assuming Step #8 went smoothly, let’s create a Python virtual environment on our Nano:

How to configure your NVIDIA Jetson Nano for Computer Vision and Deep Learning
$ mkvirtualenv py3cv4 -p python3
I’ve named the virtual environment py3cv4 indicating that we will use Python 3 and OpenCV 4. You can name yours whatever you’d like depending on your project and software needs or even your own creativity.

When your environment is ready, your bash prompt will be preceded by (py3cv4). If your prompt is not preceded by the name of your virtual environment name, at any time you can use the workon command as follows:

How to configure your NVIDIA Jetson Nano for Computer Vision and Deep Learning
$ workon py3cv4
