from requests import get
from datetime import datetime
from shutil import copy

now = datetime.now().strftime("%d-%m-%y_%H-%M")

expb = get("https://media21.bechirot.gov.il/files/expb.csv")
open("expb.csv", "wb").write(expb.content)
copy("expb.csv", "expb-" + now + ".csv")

ballots = get("https://bechirot21.bechirot.gov.il/election/Kneset20/Documents/kalpies_full_report.xls")
open("kalpies_full_report.xls", "wb").write(ballots.content)
copy("kalpies_full_report.xls", "kalpies_full_report" + now + ".xls")