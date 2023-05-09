from pynmeagps import NMEAReader
stream = open('./logs/22090401.LOG','rb')
nmr = NMEAReader(stream, nmeaonly=True)
for (raw_data, parsed_data) in nmr:
    print(parsed_data)
