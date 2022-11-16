#!/usr/bin/python3 

import sys
import logging
import os

sys.path.append("./src")

import main

def main():

	if os.path.exists("./data/") == False:
		os.mkdir("./data/")
   
  if os.path.exists("./data/listeners/") == False:
		os.mkdir("./data/listeners/")
  
  loadlisteners()
  
  start()   
    
if __name__ == "__main__":
    main()
