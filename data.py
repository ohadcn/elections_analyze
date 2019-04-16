from pandas import read_csv, read_excel

expb = read_csv("expb.csv", encoding="cp1255")
ballots = read_excel("kalpies_full_report.xls")

expb_incountry = expb[expb['סמל ישוב'] != 99999]

final_results = expb.sum()
