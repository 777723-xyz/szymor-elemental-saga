import csv
import sys

sys.path.insert(0, "tools/batches")
import importlib
import fill_62_profiles
importlib.reload(fill_62_profiles)

rows = list(csv.DictReader(open("docs/text/batches/profile.tsv"), delimiter="\t"))
r = [r for r in rows if r["id"] == "ACTOR_1_profile"][0]
j = r["japanese"]
nj = fill_62_profiles.norm(j)
keys = {fill_62_profiles.norm(k): k for k in fill_62_profiles.P}
print("norm japanese:", repr(nj[:50]))
for kn, k in keys.items():
    if kn.startswith("庶民"):
        print("norm key     :", repr(kn[:50]))
        print("equal:", kn == nj)
