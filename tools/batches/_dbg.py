import csv
import sys

sys.path.insert(0, "tools/batches")
from fill_62_profiles import norm

rows = list(csv.DictReader(open("docs/text/batches/profile.tsv"), delimiter="\t"))
r = [r for r in rows if r["id"] == "ACTOR_1_profile"][0]
j = r["japanese"]
i = j.find("n")
print("raw around break:", repr(j[i - 6:i + 3]))
nj = norm(j)
ni = nj.find("n")
print("norm around break:", repr(nj[ni - 6:ni + 3]))
print("norm equals key:",
      nj in {norm(k) for k in __import__("fill_62_profiles").P})
