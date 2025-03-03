import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("./.datasets/BTC-2021min.csv")

    print(df)

if __name__ == "__main__":
    main()
    