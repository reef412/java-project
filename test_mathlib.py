import mathlib

def test_calc_total():
	total = mathlib.calc_total (4,5)
	assert total == 9

def test_calc_multiply():
	product = mathlib.calc_multiply (10,3)
	assert product == 30