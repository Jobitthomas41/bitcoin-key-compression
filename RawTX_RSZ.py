import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "01000000013ead4d5bebdcdc4d26f61ad34353d778c904fcd05fde56a3ff4e872d80b9fb2f070000008a47304402201fa14696d4333e405c4cff00d908d8f1fb52dc9982e576beab236a01c4a7cc400220798a954111b9343ea64b190992c565f43dc6bef3fd098906e9d4124693688f410141042a6fd5fcaa79f430815b859d5532d5277dc019874105af1f9f51bdb0a97c54ceb374dbfd107b54568f50d27aea5adfce89897f1ba68453b8b910c5f0e5ef4f6dffffffff0221774301000000001976a9144c89b416b3f572ddb9cf16eeecc2810f9b359ae588acf5516600000000001976a914a8f511a2752b6bb5eb1203cbae1149696642f6bc88ac00000000"
m = txnUtils.parseTxn(tx)
e = txnUtils.getSignableTxn(m)
z = hashlib.sha256(hashlib.sha256(e.decode('hex')).digest()).digest()
z1 = z[::-1].encode('hex_codec')
z = z.encode('hex_codec')
s = keyUtils.derSigToHexSig(m[1][:-2])
pub =  m[2]
sigR = s[:64]
sigS = s[-64:]
sigZ = z
print ('Signed TX is :', tx)
print ('Signature (r, s pair) is :', s)
print ('Public Key is :', pub)
print ("")
print ("#################################################################################################")
print ("")
print ('Unsigned TX is :', e)
print ('hash of message (sigZ) is USE This ONE :', z)
print ('reversed z :', z1)
print ("")
print ("#################################################################################################")
print ("##################################VALUES NEEDED ARE BELOW #######################################")
print ("#################################################################################################")
print ("")
print ('THE R VALUE is  :', sigR)
print ('THE S VALUE is  :', sigS)
print ('THE Z VALUE is  :', sigZ)
print ('THE PUBKEY is :', pub)
