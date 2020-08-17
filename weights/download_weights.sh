#!/bin/bash
# Download weights for backbone network trained on Imagenet
# wget -c https://pjreddie.com/media/files/darknet53.conv.74
#Download full model weights for Hygiene monitor
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1sx2uz3_t3pR1-Vc04CKqlTuJgyal1tdD' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1sx2uz3_t3pR1-Vc04CKqlTuJgyal1tdD" -O yolov3_ckpt_99.pth && rm -rf /tmp/cookies.txt