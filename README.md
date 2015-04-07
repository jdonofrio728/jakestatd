JakestatD
==========
A firewall friendly implementation of jstatd JDK tool

Jstatd is a basic monitoring tool that can be used to remotely monitor you JVM's. It requires 3 ports in order to work by default. The program allows you to pick one of them using the standard command line arguments, while the other 2 are randomly picked. This makes using this tool in larger environments a pain for firewall administrators.

I wrote jakestatd to fix this problem. It has 3 hard coded ports, so you don't have to write some clever wrapper script to figure out the random ones. The ports in use are:

2020
2021
2022

Running jakestatd
-----------------

Make sure you have Java and Maven installed

Jakestatd can be executed under maven by running the following command:

> mvn exec:java

To produce a binary distribution, you can run the following:

> mvn clean package
