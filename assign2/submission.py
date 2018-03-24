import base64,hashlib,hmac,struct,sys,time
def generateTOTP(secretKey):
	key = base64.b32decode(secretKey)#Decode base32 input
	unpackedMsg = int(time.time()) // 30#Use agreed upon T0/TI:Unix epoch,30 sec
	msg = struct.pack('>Q', unpackedMsg)#Binary representation
	digest = hmac.new(key, msg, hashlib.sha1).digest()#Generate new hmac with binary representation
	offset = ord(digest[19]) & 15# set offset of which bits to use
        packedToken = digest[offset : offset+4]#set packed token range
        unpackedToken = struct.unpack('>I', packedToken)[0] & 0x7fffffff#unpack the binary representation to an integer
	tokenValue = unpackedToken % 1000000#modulate token by 1000000
        token = '{0:06d}'.format(tokenValue)#pad w/ zeroes
        return token#generated OTP for the shared key
def main():
        print("SHARED KEY: qxgt krxu ydqn h3eu 63y3 opub cv3u 7jau")#print hard-coded key
	key = "qxgt krxu ydqn h3eu 63y3 opub cv3u 7jau"#set key to be the same as the hard-coded
	key = ("".join(key.split())).upper()#strip spaces and move everything to uppercase
	while True:#infinit loop
		print(generateTOTP(key))#print the authentication code for 30 seconds
		time.sleep(30)#sleep for 30 seconds
main()
