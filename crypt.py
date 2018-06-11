#-*- coding:utf-8 -*-

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def calc_des(data, key, ifenc=True, mode='ECB', iv=None):
	if isinstance(data, str):
		data = bytes.fromhex(data)
	if isinstance(key, str):
		key = bytes.fromhex(key)
	if isinstance(iv, str):
		iv = bytes.fromhex(iv)

	backend = default_backend()
	if mode == 'ECB':
		cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=backend)
	else:
		cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend)
	if ifenc:
		encryptor = cipher.encryptor()
		ct = encryptor.update(data) + encryptor.finalize()
		return ct
	else:
		decryptor = cipher.decryptor()
		ct = decryptor.update(data) + decryptor.finalize()
		return ct

def des_ecb(data, key):
	return calc_des(data, key)

def undes_ecb(data, key):
	return calc_des(data, key, False)

def des_cbc(data, key, iv):
	return calc_des(data, key, True, 'CBC', iv)

def undes_cbc(data, key, iv):
	return calc_des(data, key, False, 'CBC', iv)


if __name__ == '__main__':
	# key = b'1122334455667788'
	# e = des_ecb(b'12345678', key)
	# print(e.hex())
	# d = undes_ecb(e, key)
	# print(d.hex())

	iv = '67ff18d343f34c31'
	key = b'1122334455667788'
	e = des_cbc(b'12345678ABCDEFGH', key, iv)
	print(e.hex().upper())
	d = undes_cbc(e, key, iv)
	print(d.hex())


