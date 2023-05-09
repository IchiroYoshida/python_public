from pynmeagps import NMEAReader
stream = open('./logs/22090401.LOG','rb')
nmr = NMEAReader(stream, nmeaonly=True)
for (raw_data, parsed_data) in nmr:
    if parsed_data.msgID == 'RMC':
        print(parsed_data.date,parsed_data.time,parsed_data.lat, parsed_data.lon)

