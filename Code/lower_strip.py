#!/usr/bin/env python
#-*- coding: utf-8 -*-


import pandas as pd


def simpleCleaner(s):
	'''
	removes whitespaces and makes string lowercase
	'''
	return s.str.lower.str.strip()
