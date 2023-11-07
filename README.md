# Anthropomorphic robot hand design

This concept was developed from a semester-long school project in the Design and Ergonomics of the Medical Products course. But I plan to continue with the project, so it's a work in progress. 

### [Click here to view in the official Autodesk gallery](https://www.autodesk.com/community/gallery/project/168645/prosthetic-hand-1)

<p align="center">
  <img src="https://github.com/sokolmarek/anthropomorphic-robot-hand/blob/main/Gallery/renders/cover.png?raw=true" />
</p>

## Fusion360 Add-in

As part of this project, I also wrote a simple plugin for Fusion360 that reads the data
stored by the OpenCV hand tracking script in real-time. For now, I'm uploading the initial 
version but FusionApi should be able to integrate third-party content into the built-in window 
so later I'll upload an improved version where both scripts will be fused. 

<p align="center">
  <img src="https://github.com/sokolmarek/anthropomorphic-robot-hand/blob/main/Gallery/fusion_addin.gif?raw=true" width="600" />
</p>

The plugin was mainly used to quickly demonstrate the hand movement and for a wow effect. I was
too lazy to read the whole FusionApi documentation.

## Future work

As a hobbyist continuation of this project, I would like to get to design optimization 
and then begin 3D prototyping and printing the finger, along with the construction of a 
functional dual-twist mode actuation mechanism (more in report.pdf).

## References

- [[1] S. H. Jeong, K. -S. Kim and S. Kim, "Designing Anthropomorphic Robot Hand With Active Dual-Mode Twisted String Actuation Mechanism and Tiny Tension Sensors," in IEEE Robotics and Automation Letters, vol. 2, no. 3, pp. 1571-1578, July 2017, doi: 10.1109/LRA.2017.2647800.](https://ieeexplore.ieee.org/document/7805142)
- [[2] S. H. Jeong, K. -S. Kim and S. Kim, "Development of a robotic finger with an active dual-mode twisting actuation and a miniature tendon tension sensor," 2016 IEEE International Conference on Advanced Intelligent Mechatronics (AIM), 2016, pp. 1-6, doi: 10.1109/AIM.2016.7576734.](https://ieeexplore.ieee.org/document/7576734)
- [[3] Y. Cho, Y. Lee, P. Kim, S. Jeong and K. -S. Kim, "The MSC Prosthetic Hand: Rapid, Powerful, and Intuitive," in IEEE Robotics and Automation Letters, vol. 7, no. 2, pp. 3170-3177, April 2022, doi: 10.1109/LRA.2022.3140444.](https://ieeexplore.ieee.org/document/9670648)
- [[4] S. H. Jeong, K. -S. Kim and S. Kim, "Control of and experimentation on an active dual-mode twisted string actuation mechanism," 2017 IEEE International Conference on Advanced Intelligent Mechatronics (AIM), 2017, pp. 987-992, doi: 10.1109/AIM.2017.8014147.](https://ieeexplore.ieee.org/document/8014147)

