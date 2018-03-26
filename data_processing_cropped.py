import os
from tqdm import tqdm
import numpy as np
from sklearn.model_selection import train_test_split

NUM_STORIES_TO_SAVE   = 100000
STORY_LENGTH          = 100
NUM_SUMMARIES_TO_SAVE = 1

story_filenames = os.listdir("./cnn")
np.random.shuffle(story_filenames)
tqdm.write("Number of stories: {}".format(len(story_filenames)))

stories = []
for story_filename in tqdm(story_filenames):
    if len(stories) == NUM_STORIES_TO_SAVE:
        break
    story_lines = open("./cnn/" + story_filename, mode = "r", encoding = "utf8").readlines()
    story_lines = [
        line.replace("-LRB- CNN Student News -RRB- --", "")
            .replace("-LRB- CNN -RRB- --", "")
            .replace("-LRB-", "")
            .replace("-RRB-", "")
            .replace("''", '" ')
            .replace("``", '" ')
            .strip() for line in story_lines if line != "\n"
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
        paragraph = " ".join(" ".join(paragraph).split()[:STORY_LENGTH + 1])
        summary = " ".join(summary[:NUM_SUMMARIES_TO_SAVE])
        stories.append({"paragraph": paragraph, "summary": summary})
        #cnn_stories_file.write(paragraph + "\t" + summary + "\n")

train, test = train_test_split(stories, train_size = 0.8)
test, valid = train_test_split(test, train_size = 0.8)

with open("./cnn_stories_cropped_train.txt", mode = "w", encoding = "utf8") as train_file:
    for story in train:
        train_file.write(story["paragraph"] + "\t" + story["summary"] + "\n")

with open("./cnn_stories_cropped_test.txt", mode = "w", encoding = "utf8") as test_file:
    for story in test:
        test_file.write(story["paragraph"] + "\t" + story["summary"] + "\n")

with open("./cnn_stories_cropped_valid.txt", mode = "w", encoding = "utf8") as valid_file:
    for story in valid:
        valid_file.write(story["paragraph"] + "\t" + story["summary"] + "\n")
