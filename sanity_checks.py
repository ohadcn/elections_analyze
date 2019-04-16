from data import expb, ballots, expb_incountry

# TODO: replace this one liner with a readable code
missing_from_ballots = [i for i in range(len(expb))
		if expb['סמל ישוב'][i] != 99999 and not
		any((ballots['סמל קלפי'] == expb['מספר קלפי'][i])
		[(ballots['סמל ישוב בחירות'] == expb['סמל ישוב'][i])])]

if len(missing_from_ballots) != 0:
	print("missing ballots in list:")
	print([(expb["שם ישוב"][i], expb["מספר קלפי"][i]) for i in missing_from_ballots])

# TODO: replace this one liner with a readable code
missing_from_results = [i for i in range(len(ballots))
		if not any((ballots['סמל קלפי'][i] == expb['מספר קלפי'])
		[(ballots['סמל ישוב בחירות'][i] == expb['סמל ישוב'])])]
if len(missing_from_results) != 0:
	print("some ballots has no results")
	print([(ballots["שם ישוב בחירות"][i], ballots["סמל קלפי"][i]) for i in missing_from_results])

too_many_votes = expb_incountry.query('בזב < מצביעים')
if len(too_many_votes) > 0:
	print("more votes than eligibles!")
	print(too_many_votes)

diff_votes_than_voters = (expb["כשרים"] + expb["פסולים"] != expb["מצביעים"])
diff_votes_than_voters = [i for i in range(len(diff_votes_than_voters)) if diff_votes_than_voters[i]]
if len(diff_votes_than_voters) != 0:
	print("כשרים + פסולים != מצביעים")
	print(diff_votes_than_voters)

#מספר הקולות הכשרים זהה לסכום הקולות של המפלגות
diff_votes_than_voters = sum([expb[i] for i in expb.keys()[7:]]) != expb['כשרים']
diff_votes_than_voters = [i for i in range(len(diff_votes_than_voters)) if diff_votes_than_voters[i]]
if diff_votes_than_voters and (len(diff_votes_than_voters) != 0):
	print("sum(votes['parties']) != כשרים")
	print(diff_votes_than_voters)
