import pandas as pd
import datetime
import sys

def show_nans(df):
    # print columns with nans
    columns_with_nans = df.columns[df.isna().any()].tolist()
    print("Columns with nans: {}".format(columns_with_nans))

    # print rows ids with nans
    rows_with_nans = df[df.isna().any(axis=1)]
    ids_rows_with_nans = rows_with_nans.index.to_list()
    print("Rows with nans: {}".format(ids_rows_with_nans))
    # print(rows_with_nans)
    return ids_rows_with_nans


def invalid_countries_names(df):
    valid_names = ['UNITED STATES OF AMERICA', 'AUSTRALIA', 'UNITED KINGDOM',
                   'BRAZIL', 'MEXICO', 'GERMANY', 'SOUTH KOREA', 'BELGIUM', 'EGYPT',
                   'FRANCE', 'JAPAN', 'SPAIN', 'CHINA', 'SWITZERLAND',
                   'UNITED STATES OF AMERICA ', 'POLAND', 'AUSTRIA', 'CANADA',
                   'BELGIUM ', 'RUSSIA', 'URUGUAY', 'DENMARK', 'SOUTH AFRICA',
                   'UNITED KINGDOM ', 'MEXICO ', 'NORWAY', 'TURKEY', 'GERMANY ',
                   'SWEDEN', 'SOUTH KOREA ', 'JAPAN ', 'EGYPT ',
                   'POLAND ', 'AUSTRALIA ', 'BRAZIL ', 'CHINA ', 'SOUTH AFRICA ']
    sus_name = df[~df['Country'].isin(valid_names)]
    ids_sus_name = sus_name.index.to_list()
    print("Countries with invalid values: {}".format(ids_sus_name))
    return ids_sus_name


def validate_date_column(df, column_name):
    invalid_dates = df[~pd.to_datetime(df[column_name], format='%d/%m/%Y', errors='coerce').notna()]
    ids_invalid_dates = invalid_dates.index.to_list()
    print("Column {} invalid dates: {}".format(column_name, ids_invalid_dates))
    return ids_invalid_dates

def invalid_validation_date(df):
    return validate_date_column(df, "Validation Date")


def invalid_maturity_date(df):
    return validate_date_column(df, "Maturity")



def compare_dates(df):
    maturity_dates = pd.to_datetime(df["Maturity"], format='%d/%m/%Y', errors='coerce')
    validaton_dates = pd.to_datetime(df["Validation Date"], format='%d/%m/%Y', errors='coerce')
    wrong_maturity = df[maturity_dates < validaton_dates].index.to_list()
    print("Validation date earlier than maturity date: {}".format(wrong_maturity))
    return wrong_maturity


def invalid_currency(df):
    ids_invalid_currency = df[df["Currency"] == 'Swiss Franc'].index.to_list()
    print("Swiss Franc appears in: {}".format(ids_invalid_currency))
    return ids_invalid_currency


def stdev(df):
    sigma =df['Amount'].std()
    more_than_3sigma = df.loc[(df['Amount'] > 3 * sigma)]
    ids_more_than_3sigma = more_than_3sigma.index.to_list()
    print("Value less than 3 sigma: {}".format(ids_more_than_3sigma))
    return ids_more_than_3sigma


if __name__ == '__main__':
    df = pd.read_csv('data/data.csv', sep=',')
    #output written to report.txt file
    with open('report.txt', 'w') as f:
        sys.stdout = f

        nan_row_ids = show_nans(df)
        out_2 = invalid_countries_names(df)
        out_3 = invalid_validation_date(df)
        out_4 = invalid_maturity_date(df)
        compare_dates(df)

        out_5 = invalid_currency(df)
        out_6 = stdev(df)




