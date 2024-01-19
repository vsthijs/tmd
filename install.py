import os
import stat
import sys

base = os.path.dirname(__file__)
bindir = os.path.join(os.path.dirname(base), "take", "bin") # ../take/bin

print(f"copying {os.path.join(base, 'tmd.py')} -> {os.path.join(bindir, 'tmd')}")

with open(os.path.join(base, 'tmd.py'), "r") as f:
    script = f.read()

with open(os.path.join(bindir, 'tmd'), "w") as f:
    f.write(f"#!{sys.executable}\n")
    f.write(script)

print(f"chmod +x {os.path.join(bindir, 'tmd')}")
st = os.stat(os.path.join(bindir, 'tmd'))
os.chmod(os.path.join(bindir, 'tmd'), st.st_mode | stat.S_IEXEC)
