import pandas as pd


def create_data_frame() -> pd.DataFrame:
    return pd.read_csv("titanic.csv", index_col="PassengerId")


def show_dimentions(_df: pd.DataFrame) -> None:
    print("shape: ======================")
    print(_df.shape)


def show_dr_data(_df: pd.DataFrame) -> None:
    print("Data: ======================")
    print(_df)


def show_columns(_df: pd.DataFrame) -> None:
    print("Columns: ======================")
    print(_df.columns)
    print("Indexes: ======================")
    print(_df.index.values)


def show_last_10(_df: pd.DataFrame) -> None:
    print("last 10: ======================")
    print(_df.tail(10))


def show_first_10(_df: pd.DataFrame) -> None:
    print("last 10: ======================")
    print(_df.head(10))


def show_odd_rows(_df: pd.DataFrame) -> None:
    print("odd rows: ======================")
    print(_df.iloc[1::2])


def show_seconds_class_names(_df: pd.DataFrame) -> None:
    print("Second class: ======================")
    print(_df[_df["Pclass"] == 2]["Name"].sort_values())


def show_survived_percentage(_df: pd.DataFrame) -> None:
    print("Survived percentage: ======================")
    print(_df["Survived"].value_counts(normalize=True) * 100)


def show_survived_by_class(_df: pd.DataFrame) -> None:
    print("Survived by class: ======================")
    print(_df.groupby("Pclass")["Survived"].value_counts(normalize=True) * 100)


def remove_null_age(_df: pd.DataFrame) -> pd.DataFrame:
    return _df.dropna(subset=["Age"])


def show_women_mean_age_by_class(_df: pd.DataFrame) -> None:
    print("Women's age by class: ======================")
    print(_df.groupby(["Pclass"])["Age"].mean())


def show_survice_percentage_by_age(_df):
    print("Survived percentage by age group: ======================")
    _df.loc[_df.Age <= 17, "Adulto"] = "No"
    _df.loc[_df.Age > 17, "Adulto"] = "Si"
    _df.loc[_df.Survived == 1, "Sobrevivio"] = "Si"
    _df.loc[_df.Survived != 1, "Sobrevivio"] = "No"
    print(
        _df.groupby(["Pclass", "Adulto"])["Sobrevivio"].value_counts(normalize=True)
        * 100
    )


if __name__ == "__main__":
    df = create_data_frame()
    show_dimentions(df)
    show_dr_data(df)
    show_columns(df)
    show_last_10(df)
    show_odd_rows(df)
    show_seconds_class_names(df)
    show_survived_percentage(df)
    show_survived_by_class(df)
    df = remove_null_age(df)
    show_women_mean_age_by_class(df)
    show_survice_percentage_by_age(df)
