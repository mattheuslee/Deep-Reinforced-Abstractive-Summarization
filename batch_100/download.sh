#!/bin/bash
mkdir batch_100
for i in {0..799}
do
    wget -O batch_100/cnn_stories_80000_$i.txt https://raw.githubusercontent.com/mattheuslee/Deep-Reinforced-Abstractive-Summarization/master/batch_100/cnn_stories_80000_$i.txt -q
done
