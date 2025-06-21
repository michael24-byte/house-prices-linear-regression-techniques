import pandas as pd
 
def main():

    df = pd.read_csv("sample_submission.csv")
    print(df)


if __name__ == '__main__':
    main()