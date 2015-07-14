import sys
import os.path
parent = os.path.abspath(os.path.join(os.path.dirname(__file__),'..')) 
sys.path.append(parent)

from airfare.atc import delete_all

delete_all()
