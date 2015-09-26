import sys, string, os, shutil

def RenameFiles(srcdir, prefix):
    srcfiles = os.listdir(srcdir)
    index = 1
    for srcfile in srcfiles:
        srcfilename = os.path.splitext(srcfile)[0][1:]
        sufix = os.path.splitext(srcfile)[1]
        destfile = srcdir + "//" + prefix + "_%03d"%(index)+"_226" + sufix
        srcfile = os.path.join(srcdir, srcfile)
        os.rename(srcfile, destfile)
        index += 1
srcdir = "C:\\Users\\Jonny\\Documents\\dlnubuy\\images\\warp"
prefix = "warp"
RenameFiles(srcdir, prefix)
