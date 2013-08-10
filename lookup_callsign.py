import qrz
import ipdb; ipdb.set_trace()
qrz = qrz.QRZ('./settings.cfg')
result = qrz.callsign("w7atc")
print result['fname'], result['name']
print result['addr2'], result['state']
