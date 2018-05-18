# Some tips for dev

[TOC]

## Code Editor

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

 

## References

[gprof, valgrind, gperftool](http://gernotklingler.com/blog/gprof-valgrind-gperftools-evaluation-tools-application-level-cpu-profiling-linux/)

[gprof Quick-Start Guide](https://web.eecs.umich.edu/~sugih/pointers/gprof_quick.html)

