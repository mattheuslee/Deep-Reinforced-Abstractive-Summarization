import os
from tqdm import tqdm
import numpy as np

story_filenames = os.listdir("./cnn")
np.random.shuffle(story_filenames)
tqdm.write("{}".format(len(story_filenames)))

with open("cnn_stories.txt", mode = "w", encoding = "utf-8") as cnn_stories_file:
    for story_filename in story_filenames[:30000]:
        story_lines = open("./cnn/" + story_filename, mode = "r", encoding = "utf8").readlines()
        story_lines = [
            line.replace("-LRB-", "").replace("-RRB-", "").replace("''", '"').replace("``", '" ').strip() for line in story_lines if line != "\n"
        ]
        paragraph = []
        summary = []
        in_summary = False
        for i, line in enumerate(story_lines):
            if line == "@highlight":
                in_summary = True
                summary.append(story_lines[i + 1])
            elif not in_summary:
                paragraph.append(line)
        if len(paragraph) > 0 and len(summary) > 0:
            paragraph = " ".join(paragraph)
            summary = " ".join(summary)
            cnn_stories_file.write(paragraph + "\t" + summary + "\n")

with open("cnn_test_stories.txt", mode = "w", encoding = "utf-8") as cnn_test_stories_file:
    for story_filename in story_filenames[-10:]:
        story_lines = open("./cnn/" + story_filename, mode = "r", encoding = "utf8").readlines()
        story_lines = [
            line.replace("-LRB-", "").replace("-RRB-", "").replace("''", '"').replace("``", '" ').strip() for line in story_lines if line != "\n"
        ]
        paragraph = []
        summary = []
        in_summary = False
        for i, line in enumerate(story_lines):
            if line == "@highlight":
                in_summary = True
                summary.append(story_lines[i + 1])
            elif not in_summary:
                paragraph.append(line)
        if len(paragraph) > 0 and len(summary) > 0:
            paragraph = " ".join(paragraph)
            summary = " ".join(summary)
            cnn_test_stories_file.write(paragraph + "\t" + summary + "\n")
