# snapchat-killer
Taking opencv haar classifier to a test drive

Face recognition + draw ears where face is.

#### Requires
opencv and opencv-contrib version 3.3.0-rc

#### Demo
![Demo](/snap.gif?raw=true "Snap demo")

#### How to compile opencv from github:

Install git, camke and some devel libs

```
dnf install "Development Tools" "Engineering and Scientific"
dnf install cmake gtk3-devel
```

Get the code

```
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```

Compile

```
mkdir opencv/build
cd opencv/build

cmake -DOPENCV_EXTRA_MODULES_PATH= ../../opencv_contrib/modules/ ..

make
```

Install
```
sudo make install
```
