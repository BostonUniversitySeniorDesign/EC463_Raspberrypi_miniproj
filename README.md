<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
  </a>

  <h3 align="center">EC463_EE_Miniproject</h3>

  <p align="center">
    A Raspberry Pi with Wifi & Bluetooth Probe Feature 
    <br />
    <a href="https://github.com/BostonUniversitySeniorDesign/2021-hardware-miniproj"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#raspberry-pi">Raspberry Pi</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#data-and-analysis">Data and Analysis</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Basic Intro of background:

Here are our intended features:
* detect Bluetooth legacy devices in the area
* detect BlE devices in the area
* detect wifi hotspots over time and put into a JSON file
* plot wifi hotspots over time


### Raspberry Pi

Addressing why choose raspberry pi and its performance & attachments:

Raspberry Pi is a powerful embeded system for educational researches and Pi 4's design offers capability to connect to monitors for better visualization. Raspberry Pi OS is Python supported and it helps us to be familar to Python and its basic packages.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

One of the main difficulties we had when setting up the Raspberry Pi was getting the correct setup. As an example, we tried to use a macbook as our monitor, but soon found that would not work, so we had to adapt and get a monitor with an HDMI cable to interact with the UI for the Raspberry Pi. Additionally, after setting up the SSH with the wifi on an on campus apartment. We had difficulties using the SSH from one of the BU dorms, namely because the wifi router at the apartment did not allow the computer in the dorm to connect.

In addition, we learned a lot about the syntax for the Raspberry Pi and Python 3 specifically. There were many times the code was not working because we were ussing the incorrect syntax. When running [wifi_plot.py](wifi_plot.py), the file was not working because an argument had to be called for the filename when executing the script. 
```sh
python3 wifi_plot.py wifi_2021-09-16T12_02_16.json
```

### Modifications

Although not many modifications were made because the code was given, we did make 2 small changes in order to increase functionality and get a feel for using Raspberry Pi. 

First, we added to the bluetooth.discover_devices command in [bt_scan.py](bt_scan.py), so that the script also returned the device name in addition to the bluetooth address.

```sh
disc_devs = bluetooth.discover_devices(duration=5, lookup_names=True) 
```

This was done primarily to see what devices we were detecting to get a feel for how the script operated. Namely, how the script only picked up on our phones and laptops when they were actively looking to connect to a bluetooth device. 

The second addition was to [wifi_plot.py](wifi_plot.py). We added more labels to the plot, so it looked more professional and easy to understand. 

```sh
matplotlib.pyplot.xlabel("Time (Day of the Month/Hour/Minute)")
    matplotlib.pyplot.ylabel("Number of Hotspots")
    matplotlib.pyplot.title("Hotspots over time in Photonics")
    matplotlib.pyplot.show()
```
<!-- Data & Analysis EXAMPLES -->
## Data and Analysis
