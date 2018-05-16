# Some tips for dev

[TOC]

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

