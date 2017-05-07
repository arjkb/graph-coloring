#!/usr/bin/python3

import sys
import os
import glob
import itertools
import subprocess
from datetime import datetime, timedelta

def make_sig():
	if not os.path.exists("./sig"):
		subprocess.run(["gcc", "-o", "sig", "sig.c"])

def run_vweights(graphs):
	
	if not os.path.exists("./vweight_test"):
		os.makedirs("./vweight_test")

	vweights = list(itertools.product([0,1], repeat = 4))

	for vw in vweights:
		vw_sum = sum(vw)
		
		if vw_sum != 0:
			vw_0 = vw[0] * (1.0/vw_sum)
			vw_1 = vw[1] * (1.0/vw_sum)
			vw_2 = vw[2] * (1.0/vw_sum)
			vw_3 = vw[3] * (1.0/vw_sum)
	
			for g in graphs:
				g_name = g.split("/")[1];
				for i in range(100):
					with open("./vweight_test/sig_vweights_"+str(vw_0)+"_"+str(vw_1)+"_"+str(vw_2)+"_"+str(vw_3)+"_"+g_name, "a") as fout:
						start_time = datetime.now()
						output = subprocess.run(["./sig", str(g), str(2), "--vweights", str(vw_0), str(vw_1), str(vw_2), str(vw_3)], stdout=subprocess.PIPE)	
						elapsed_time = datetime.now() - start_time
						t = str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)
						c = output.stdout.decode("utf-8").split("\n")[0].split(",")
						if len(c) < 4:
							print(g)
						else:
							fout.write(t + "," + c[0] + "," + c[1] + "," + c[2] + "," + c[3] + "\n")

def run_cweights(graphs):
	
	if not os.path.exists("./cweight_test"):
		os.makedirs("./cweight_test")

	cweights = list(itertools.product([0,1], repeat = 6))

	for cw in cweights:
		cw_sum = sum(cw)
		
		if cw_sum != 0:
			cw_0 = cw[0] * (1.0/cw_sum)
			cw_1 = cw[1] * (1.0/cw_sum)
			cw_2 = cw[2] * (1.0/cw_sum)
			cw_3 = cw[3] * (1.0/cw_sum)
			cw_4 = cw[4] * (1.0/cw_sum)
			cw_5 = cw[5] * (1.0/cw_sum)
	
			for g in graphs:
				g_name = g.split("/")[1];
				for i in range(100):
					with open("./cweight_test/sig_cweights_"+str(cw_0)+"_"+str(cw_1)+"_"+str(cw_2)+"_"+str(cw_3)+"_"+str(cw_4)+"_"+str(cw_5)+"_"+g_name, "a") as fout:
						start_time = datetime.now()
						output = subprocess.run(["./sig", str(g), str(2), "--cweights", str(cw_0), str(cw_1), str(cw_2), str(cw_3), str(cw_4), str(cw_5)], stdout=subprocess.PIPE)	
						elapsed_time = datetime.now() - start_time
						t = str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)
						c = output.stdout.decode("utf-8").split("\n")[0].split(",")
						if len(c) < 4:
							print(g)
						else:
							fout.write(t + "," + c[0] + "," + c[1] + "," + c[2] + "," + c[3] + "\n")

def run_initpolicy(graphs):
	
	if not os.path.exists("./initpolicy_test"):
		os.makedirs("./initpolicy_test")

	for g in graphs:
		g_name = g.split("/")[1];
		for init in range(1, 4):
			for i in range(100):
				with open("./initpolicy_test/sig_initpolicy_"+str(init)+"_"+g_name, "a") as fout:
					start_time = datetime.now()
					output = subprocess.run(["./sig", str(g), str(init)], stdout=subprocess.PIPE)	
					elapsed_time = datetime.now() - start_time
					t = str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)
					c = output.stdout.decode("utf-8").split("\n")[0].split(",")
					if len(c) < 4:
						print(g)
					else:
						fout.write(t + "," + c[0] + "," + c[1] + "," + c[2] + "," + c[3] + "\n")

def run_maxiter(graphs):
	
	if not os.path.exists("./maxiter_test"):
		os.makedirs("./maxiter_test")

	for g in graphs:
		g_name = g.split("/")[1];
		for maxiter in range(30, 300, 30):
			revert = maxiter/10
			for i in range(100):
				with open("./maxiter_test/sig_maxiter_"+str(maxiter)+"_"+g_name, "a") as fout:
					start_time = datetime.now()
					output = subprocess.run(["./sig", str(g), str(2), "--maxiter", str(maxiter), "--revert", str(revert)], stdout=subprocess.PIPE)	
					elapsed_time = datetime.now() - start_time
					t = str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)
					c = output.stdout.decode("utf-8").split("\n")[0].split(",")
					if len(c) < 4:
						print(g)
					else:
						fout.write(t + "," + c[0] + "," + c[1] + "," + c[2] + "," + c[3] + "\n")

def run_revert(graphs):
	
	if not os.path.exists("./revert_test"):
		os.makedirs("./revert_test")

	for g in graphs:
		g_name = g.split("/")[1];
		for revert in range(10, 100, 10):
			for i in range(100):
				with open("./revert_test/sig_revert_"+str(revert)+"_"+g_name, "a") as fout:
					start_time = datetime.now()
					output = subprocess.run(["./sig", str(g), str(2), "--revert", str(revert)], stdout=subprocess.PIPE)	
					elapsed_time = datetime.now() - start_time
					t = str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)
					c = output.stdout.decode("utf-8").split("\n")[0].split(",")
					if len(c) < 4:
						print(g)
					else:
						fout.write(t + "," + c[0] + "," + c[1] + "," + c[2] + "," + c[3] + "\n")


def run_target(graphs):
	
	if not os.path.exists("./target_test"):
		os.makedirs("./target_test")

	for g in graphs:
		g_name = g.split("/")[1];
		for target in range(10, 100, 10):
			for i in range(100):
				with open("./target_test/sig_target_"+str(target)+"_"+g_name, "a") as fout:
					start_time = datetime.now()
					output = subprocess.run(["./sig", str(g), str(2), "--target", str(target)], stdout=subprocess.PIPE)	
					elapsed_time = datetime.now() - start_time
					t = str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)
					c = output.stdout.decode("utf-8").split("\n")[0].split(",")
					if len(c) < 4:
						print(g)
					else:
						fout.write(t + "," + c[0] + "," + c[1] + "," + c[2] + "," + c[3] + "\n")

def main():
	if len(sys.argv) < 2:
		print("Error: please give graph directory")
		sys.exit(1)
	
	graphs = glob.glob(sys.argv[1])

	print("Making sig")
	make_sig()

#	print("Running vweights")
#	run_vweights(graphs)				

#	print("Running initpolicy") 
#	run_initpolicy(graphs)

	print("Running maxiter")
	run_maxiter(graphs)

	print("Running revert")
	run_revert(graphs)

	print("Running target")
	run_target(graphs)

#	print("Running cweights")
#	run_cweights(graphs)

if __name__ == "__main__":
	main()
