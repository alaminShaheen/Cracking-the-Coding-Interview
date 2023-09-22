# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
from collections import defaultdict


def is_unique_hashmap(sentence: str) -> bool:
	dictionary = defaultdict(bool)

	for char in sentence:
		if dictionary[char]:
			return False
		dictionary[char] = True
	return True


def is_unique_set(sentence: str) -> bool:
	unique_chars = set()

	for char in sentence:
		if unique_chars:
			return False
		unique_chars.add(char)
	return True


def is_unique_bitmask(sentence: str) -> bool:
	mask = 0

	for char in sentence:
		char_order = ord(char) - (ord('0') if char.isdigit() else ord('a'))

		if (1 << char_order) & mask:
			return False

		mask |= 1 << char_order
	return True
