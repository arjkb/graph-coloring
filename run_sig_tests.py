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
				for _ in range(100):
					with open("./vweight_test/sig_vweights_"+str(vw_0)+"_"+str(vw_1)+"_"+str(vw_2)+"_"+str(vw_3)+"_"+g_name, "a") as fout:
						start_time = datetime.now()
						subprocess.run(["./sig", str(g), str(1), "--vweights", str(vw_0), str(vw_1), str(vw_2), str(vw_3)], stdout=subprocess.PIPE)	
						elapsed_time = datetime.now() - start_time
						fout.write(str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)+"\n")

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
				for _ in range(100):
					with open("./cweight_test/sig_cweights_"+str(cw_0)+"_"+str(cw_1)+"_"+str(cw_2)+"_"+str(cw_3)+"_"+"_"+str(cw_4)+"_"+str(cw_5)+"_"+g_name, "a") as fout:
						start_time = datetime.now()
						subprocess.run(["./sig", str(g), str(1), "--cweights", str(cw_0), str(cw_1), str(cw_2), str(cw_3), str(cw_4), str(cw_5)], stdout=subprocess.PIPE)	
						elapsed_time = datetime.now() - start_time
						fout.write(str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)+"\n")

def run_initpolicy(graphs):
	
	if not os.path.exists("./initpolicy_test"):
		os.makedirs("./initpolicy_test")

	for g in graphs:
		g_name = g.split("/")[1];
		for init in range(1, 3):
			for _ in range(100):
				with open("./initpolicy_test/sig_initpolicy_"+str(init)+"_"+g_name, "a") as fout:
					start_time = datetime.now()
					subprocess.run(["./sig", str(g), str(init)], stdout=subprocess.PIPE)	
					elapsed_time = datetime.now() - start_time
					fout.write(str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)+"\n")

def run_maxiter(graphs):
	
	if not os.path.exists("./maxiter_test"):
		os.makedirs("./maxiter_test")

	for g in graphs:
		g_name = g.split("/")[1];
		for maxiter in range(50, 1000, 50):
			for _ in range(100):
				with open("./maxiter_test/sig_maxiter_"+str(maxiter)+"_"+g_name, "a") as fout:
					start_time = datetime.now()
					subprocess.run(["./sig", str(g), str(1), "--maxiter", str(maxiter)], stdout=subprocess.PIPE)	
					elapsed_time = datetime.now() - start_time
					fout.write(str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)+"\n")

def run_revert(graphs):
	
	if not os.path.exists("./revert_test"):
		os.makedirs("./revert_test")

	for g in graphs:
		g_name = g.split("/")[1];
		for revert in range(5, 100, 5):
			for _ in range(100):
				with open("./revert_test/sig_revert_"+str(revert)+"_"+g_name, "a") as fout:
					start_time = datetime.now()
					subprocess.run(["./sig", str(g), str(1), "--revert", str(revert)], stdout=subprocess.PIPE)	
					elapsed_time = datetime.now() - start_time
					fout.write(str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)+"\n")

def run_trials(graphs):
	
	if not os.path.exists("./trials_test"):
		os.makedirs("./trials_test")

	for g in graphs:
		g_name = g.split("/")[1];
		for trials in range(5, 100, 5):
			for _ in range(100):
				with open("./trials_test/sig_trials_"+str(1)+"_"+g_name, "a") as fout:
					start_time = datetime.now()
					subprocess.run(["./sig", str(g), str(1), "--trials", str(trials)], stdout=subprocess.PIPE)	
					elapsed_time = datetime.now() - start_time
					fout.write(str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)+"\n")

def run_target(graphs):
	
	if not os.path.exists("./target_test"):
		os.makedirs("./target_test")

	for g in graphs:
		g_name = g.split("/")[1];
		for target in range(5, 100, 5):
			for _ in range(100):
				with open("./target_test/sig_target_"+str(1)+"_"+g_name, "a") as fout:
					start_time = datetime.now()
					subprocess.run(["./sig", str(g), str(1), "--target", str(target)], stdout=subprocess.PIPE)	
					elapsed_time = datetime.now() - start_time
					fout.write(str((elapsed_time.days * 24 * 60 * 60 + elapsed_time.seconds) * 1000 + elapsed_time.microseconds / 1000.0)+"\n")

def main():
	if len(sys.argv) < 2:
		print("Error: please give graph directory")
		sys.exit(1)
	
	graphs = glob.glob(sys.argv[1])

	make_sig()

	run_vweights(graphs)				

	run_cweights(graphs)

	run_initpolicy(graphs)

	run_maxiter(graphs)

	run_revert(graphs)

	run_trials(graphs)

	run_target(graphs)

if __name__ == "__main__":
	main()
