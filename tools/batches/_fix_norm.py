#!/usr/bin/env python3
"""Rebuild the broken norm() return line in fill_62_profiles.py (line 47)."""
import io

path = "tools/batches/fill_62_profiles.py"
lines = io.open(path, encoding="utf-8").read().split("\n")
bs = chr(92)  # backslash
# correct: return re.sub(r"[ \u3000]+", " ", s).strip().replace("\\", "\\")
lines[46] = ('    return re.sub(r"[ %su3000]+", " ", s).strip()'
             '.replace("%s%s%s%s", "%s%s")' % (bs, bs, bs, bs, bs, bs, bs))
io.open(path, "w", encoding="utf-8").write("\n".join(lines))
print("rebuilt line 47")
