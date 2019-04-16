from data import expb
from sklearn.cluster import KMeans
from json import dumps

model = KMeans(n_clusters=20)

st=expb[expb.keys()[7:]].divide(expb['כשרים'], axis=0)

model.fit(st)
segments = model.predict(st)

# find what don't fit in any cluster
dists = model.transform(st)
mins = dists.min(axis=1)
interesting = (mins>0.4)

open("nofit.txt", "wt").write("\n".join([
	"{} {} {:.2}".format(expb["שם ישוב"][i], expb["מספר קלפי"][i], mins[i])
		for i in range(len(interesting)) if interesting[i]]))