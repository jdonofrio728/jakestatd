# jakestatd
A firewall friendly implementation of jstatd JDK tool

Jstatd is a fun basic monitoring tool that can be used to remotely monitor you JVM's. It requires 3 ports in order to work by default. The program allows you to pick one of them using the standard command line arguments, while the other 2 are randomly picked. This makes using this tool in larger environments a pain for firewall administrators.

I wrote jakestatd to fix this problem. It has 3 hard coded ports, so you don't have to write some clever wrapper script to figure out the random ports. The ports in use are

2020
2021
2022

