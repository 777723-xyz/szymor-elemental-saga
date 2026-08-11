import sys

sys.path.insert(0, "tools/batches")
import fill_62_profiles

print("module file:", fill_62_profiles.__file__)
import dis
dis.dis(fill_62_profiles.norm)
lines = open("tools/batches/fill_62_profiles.py", encoding="utf-8").read().split("\n")
print("line 47 bytes:", lines[46].encode("utf-8"))
