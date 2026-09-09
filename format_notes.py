""""
date()

header(aaa) / hdr(aaa)
subheader(aaa) / sbhdr(aaa) / shdr(aaa)

start_test()
end_test()
"""

from os import walk
from os.path import join
from datetime import date

def parse_function(func,args):
	out=-1
	if (func=="date"):
		d=date.today()
		out=d.strftime("%d.%m.%Y")
	elif (func=="header" or func=="hdr"):
		out=f"= | = | = | = | = | {args} | = | = | = | = | ="
	elif (func=="subheader" or func=="sbhdr" or func=="shdr"):
		out=f"= = = = = = = = = = {args} = = = = = = = = = ="
	elif (func=="start_test" or func=="end_test"):
		out="!@#$%^&*()_+-={}[]|\\:;<>?,./~`"
		out="- + - + - + - + - + = - + - + - + - + - + - + - + - + - +"
		out=out+" TEST "+"".join(reversed(out))
	return out

for r,_,fs in walk("./"):
	for f in fs:
		if (not f.endswith(".txt") or f.endswith("_last.txt")): continue
		with open(join(r,f),"r") as file:
			txt=file.read().split("\n")
		
		changed=False
		result=txt.copy()
		for i,v in enumerate(txt):
			par=v.find("(");end_par=v.find(")");ending=v[end_par+1:]
			if (par==-1 or end_par==-1): continue
			func=v[:par]
			args=v[par+1:end_par]
			out=parse_function(func,args)
			if (out==-1): out=v
			else: 
				out+=ending
				changed=True
			result[i]=out
			
		if (not changed): continue
			
		with open(join(r,f),"w") as file:
			file.write("\n".join(result))
		
		with open(join(r,f[:f.rfind(".txt")]+"_last.txt"),"w") as file:
			file.write("\n".join(txt))