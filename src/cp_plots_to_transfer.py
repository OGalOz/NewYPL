import sys, os

_, plots_dir = sys.argv
tsfr_d = os.path.join("/usr2/people/omreeg", "transfer", "new_plots")
if os.path.exists(tsfr_d):
    os.system(f"rm -r {tsfr_d}")
os.mkdir(tsfr_d)
# We rename each file to have the lib name at the beginning
lib_name = plots_dir.split("/")[-2]
if lib_name == "Plots":
    lib_name = plots_dir.split("/")[-3]
print("lib name:", lib_name)
plots_fs = os.listdir(plots_dir)
for f in plots_fs:
    if not f.startswith(lib_name):
        old_fp = os.path.join(plots_dir, f)
        new_fp = os.path.join(plots_dir, lib_name + "_" + f)
        os.system(f"cp {old_fp} {new_fp}")
        os.system(f"unlink {old_fp}")

os.system(f"cp {os.path.join(plots_dir, '*')} {tsfr_d}")
