from datasets import load_dataset
import pandas as pd

dataset = load_dataset("imdb")

train_df = pd.DataFrame(dataset["train"])
test_df = pd.DataFrame(dataset["test"])

train_df.to_csv("data/train_en.csv", index=False)
test_df.to_csv("data/test_en.csv", index=False)
