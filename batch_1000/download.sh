#!/bin/bash
mkdir batch_1000
for i in {0..79}
do
    wget -O batch_1000/cnn_stories_80000_$i.txt https://raw.githubusercontent.com/mattheuslee/Deep-Reinforced-Abstractive-Summarization/master/batch_1000/cnn_stories_80000_$i.txt -q
done
