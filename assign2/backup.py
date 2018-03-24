import base64,hashlib,hmac,struct,sys,time
def TOTP(secretKey):
	key = base64.b32decode(secretKey)#Decode base32 input
	unpackedMsg = int(time.time()) // 30#Use agreed upon T0/TI:Unix epoch,30 sec
	msg = struct.pack('>Q', unpackedMsg)#Binary representation
	digest = hmac.new(key, msg, hashlib.sha1).digest()#Generate new hmac with binary representation
	offset = ord(digest[19]) & 15# set offset
        packedToken = digest[offset : offset+4]#set packed token range
        unpackedToken = struct.unpack('>I', packedToken)[0] & 0x7fffffff#unpack the token
	tokenValue = unpackedToken % 1000000#modulate token by 1000000
        token = '{0:06d}'.format(tokenValue)#pad w/ zeroes
        return token
def main():
        print("SHARED KEY: qxgt krxu ydqn h3eu 63y3 opub cv3u 7jau")
	key = "qxgt krxu ydqn h3eu 63y3 opub cv3u 7jau"
	key = ("".join(key.split())).upper()
	while True:
		print(TOTP(key))
		time.sleep(30)
main()
