# Some tips for dev

[TOC]

# Docker

Docker Cheat Sheet( [Github](https://github.com/wsargent/docker-cheat-sheet), [pdf](https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf) )

```bash
# Log into a registry
# Create repo in https://hub.docker.com
docker login
docker login [my.registery.com:8000] --username=yourhubusername --email=youremail@company.com


## Images
# Get one image
docker pull [repo]/[image]:[tag]
# Build an image from Dockerfile and tag the image
docker build -t myapp:1.0 .
# List all images
docker images
# Delete an image from local image store
docker rmi [repo]/[image]:[tag]
# Retag a local image
docker tag myapp:1.0 myrepo/myapp:1.0
# Push an image to registry
docker push myrepo/myapp:1.0

## Containers
# List all running containers
docker ps
# List all exited containers
docker ps -aq -f status=exited
# Remove stopped containers
docker ps -aq --no-trunc -f status=exited | xargs docker rm
# Stop one container
docker stop [container name]
# Remove one container
docker rm [container name]

# Run image in a container
docker run -ti --rm -e DISPLAY=$DISPLAY -v /home/ubuntu:/var/ myapp /bin/bash
# Exit from a container
exit
```

Examples

```bash
docker pull minio/minio
docker run -dti -p 9001:9000 --name demoMinio   -e "MINIO_ACCESS_KEY=admin"   -e "MINIO_SECRET_KEY=admin"   -v /home/ubuntu/data:/data   -v /home/ubuntu/.minio:/root/.minio   minio/minio server /data
```

[Docker CE Alpine](https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management)

```bash
apk update
apk search xxx
apk add xxx
```

References

> + [Remove docker container](https://zaiste.net/removing_docker_containers/)
> + [Openface](https://github.com/cmusatyalab/openface/blob/master/Dockerfile)
> + [Docker tutorial](https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html)

# Code Editor

atom

sublime

visual studio

# Git

[Git cheat sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf) ([copy](../cheatsheet/gitcheatsheet.pdf))

Common

```bash
# Clone projects
git clone <project url>

# Set credentials
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com

# If username and password pop up often when commit
# we can use this cmd before commits
git config credential.helper store

# Add commits
git commit -a -m "commits"

# Generate keys
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
cat ~/.ssh/irs.pub
```



Clone one branch only

```bash
git clone -b mybranch --single-branch git://sub.domain.com/repo.git
```

Submodule

```bash
# Add one submodule
git submodule add https://github.com/socketio/socket.io 
# Update one submodule 
git submodule update --init --recursive
# Clone a project with submodules
git clone --recursive <project url>
```

Delete history

```bash
# $1 is SHA-1 of the commit you want to keep
git checkout --orphan temp $1 
git commit -m "Truncated history" 
git rebase --onto temp $1 master 
git branch -D temp
git gc --prune=all
git repack -a -f -F -d
```





# C++ Profiling in Linux

[cpuload example](https://github.com/gklingler/cpuProfilingDemo/blob/master/cpuload.cpp).

## valgrind

```bash
#!/bin/bash
# install valgrind & kcachegrind
sudo apt-get install valgrind
sudo apt-get install kcachegrind

# build the program (no special flags are needed)
g++ -std=c++11 cpuload.cpp -o cpuload

# run the program with callgrind; generates a file callgrind.out.12345 that can be viewed with kcachegrind
valgrind --tool=callgrind ./cpuload

# open profile.callgrind with kcachegrind
kcachegrind callgrind.out.xxxxx
```

Note that, please enable debug information when compiling by

```bash
CFLAGS+=-ggdb
NOSTRIP=1
```

## gperftools

Step 1. Make binary with debug information

```bash
sudo apt-get install google-perftools
sudo apt-get install tau
sudo ln -s /usr/lib/libprofiler.so.0 /usr/lib/libprofiler.so

CFLAGS += -DWITHGPERFTOOLS
LFLAGS += -lprofiler
```

Step 2. Run a binary as normal

```bash
./cpuload
```

Step 3. Run prof

```bash
google-pprof --callgrind ./cpuload profile.log > profile.callgrind
kcachegrind profile.grind
```



## gprof

Step 1. Add -pg argument to the compiler's command line

```bash
g++ -Wall -g -pg cpuload.cpp -o kruse
```

The binary should not loop infinitely. 

Step 2. Run a binary as normal

```bash
./kruse param1 param2
```

After execution, gmon.out wil be obtained automatically.

Step 3. Run grof binary > output.log

```bash
gprof kruse > output.log
```

 

References

> - [gprof, valgrind, gperftool](http://gernotklingler.com/blog/gprof-valgrind-gperftools-evaluation-tools-application-level-cpu-profiling-linux/)
> - [gprof Quick-Start Guide](https://web.eecs.umich.edu/~sugih/pointers/gprof_quick.html)

# Others



```bash
# check missing .so dependencies
ldd binary
```



# Author

duangenquan@gmail.com