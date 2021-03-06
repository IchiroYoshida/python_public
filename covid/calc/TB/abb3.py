"""
Country name -> Abb3 code and Death./Mil (today)

2020-05-16
"""

db="""
Afghanistan,AFG
Albania,ALB
Algeria,DZA
Andorra,AND
Angola,AGO
Anguilla,
Antigua and Barbuda,ATG
Argentina,ARG
Armenia,ARM
Aruba,ABW
Australia,AUS
Austria,AUT
Azerbaijan,AZE
Bahamas,BHS
Bahrain,BHR
Bangladesh,BGD
Barbados,BRB
Belarus,BLR
Belgium,BEL
Belize,BLZ
Benin,BEN
Bermuda,BMU
Bhutan,BTN
Bolivia,BOL
Bosnia and Herzegovina,BIH
Botswana,BWA
Brazil,BRA
British Virgin Islands,VGB
Brunei ,BRN
Bulgaria,BGR
Burkina Faso,BFA
Burundi,BDI
Cabo Verde,CPV
Cambodia,KHM
Cameroon,CMR
Canada,CAN
CAR,CAF
Caribbean Netherlands,CSS
Cayman Islands,CYM
Chad,TCD
Channel Islands,CHI
Chile,CHL
China,CHN
Colombia,COL
Comoros,COM
Congo,COD
Costa Rica,CRI
Croatia,HRV
Cuba,CUB
Curaçao,CUW
Cyprus,CYP
Czechia,CZE
Denmark,DNK
Djibouti,DJI
Dominica,DMA
Dominican Republic,DOM
DRC,COD
Ecuador,ECU
Egypt,EGY
El Salvador,SLV
Equatorial Guinea,GNQ
Eritrea,ERI
Estonia,EST
Eswatini,SWZ
Ethiopia,ETH
Faeroe Islands,FRO
Falkland Islands,
Fiji,FJI
Finland,FIN
France,FRA
French Guiana,
French Polynesia,PYF
Gabon,GAB
Gambia,GMB
Georgia,GEO
Germany,DEU
Ghana,GHA
Gibraltar,GIB
Greece,GRC
Greenland,GRL
Grenada,GRD
Guadeloupe,
Guatemala,GTM
Guinea,GIN
Guinea-Bissau,GNB
Guyana,GUY
Haiti,HTI
Honduras,HND
Hong Kong,HKG
Hungary,HUN
Iceland,ISL
India,IND
Indonesia,IDN
Iran,IRN
Iraq,IRQ
Ireland,IRL
Isle of Man,IMN
Israel,ISR
Italy,ITA
Ivory Coast,CIV
Jamaica,JAM
Japan,JPN
Jordan,JOR
Kazakhstan,KAZ
Kenya,KEN
Kuwait,KWT
Kyrgyzstan,KGZ
Laos,LAO
Latvia,LVA
Lebanon,LBN
Lesotho,LSO
Liberia,LBR
Libya,LBY
Liechtenstein,LIE
Lithuania,LTU
Luxembourg,LUX
Macao,MAC
Madagascar,MDG
Malawi,MWI
Malaysia,MYS
Maldives,MDV
Mali,MLI
Malta,MLT
Martinique,
Mauritania,MRT
Mauritius,MUS
Mayotte,
Mexico,MEX
Moldova,MDA
Monaco,MCO
Mongolia,MNG
Montenegro,MNE
Montserrat,
Morocco,MAR
Mozambique,MOZ
Myanmar,MMR
Namibia,NAM
Nepal,NRU
Netherlands,NLD
New Caledonia,NCL
New Zealand,NZL
Nicaragua,NIC
Niger,NER
Nigeria,NGA
North America,NAC
North Macedonia,MKD
Norway,NOR
Oman,OMN
Pakistan,PAK
Palestine,
Panama,PAN
Papua New Guinea,PNG
Paraguay,PRY
Peru,PER
Philippines,PHL
Poland,POL
Portugal,PRT
Qatar,QAT
Réunion,
Romania,ROU
Russia,RUS
Rwanda,RWA
S. Korea,KOR
Saint Kitts and Nevis,KNA
Saint Lucia,LCA
Saint Martin,MAF
Saint Pierre Miquelon,
San Marino,SMR
Sao Tome and Principe,STP
Saudi Arabia,SAU
Senegal,SEN
Serbia,SRB
Seychelles,SYC
Sierra Leone,SLE
Singapore,SGP
Sint Maarten,SXM
Slovakia,SVK
Slovenia,SVN
Somalia,SOM
South Africa,ZAF
South Sudan,SSD
Spain,ESP
Sri Lanka,LKA
St. Barth,
St. Vincent Grenadines,VCT
Sudan,SDN
Suriname,SUR
Sweden,SWE
Switzerland,CHE
Syria,SYR
Taiwan,
Tajikistan,TJK
Tanzania,TZA
Thailand,THA
Timor-Leste,TLS
Togo,TGO
Trinidad and Tobago,TTO
Tunisia,TUN
Turkey,TUR
Turks and Caicos,TCA
UAE,ARE
Uganda,UGA
UK,GBR
Ukraine,UKR
Uruguay,URY
USA,USA
Uzbekistan,UZB
Vatican City,
Venezuela,VEN
Vietnam,VNM
Western Sahara,
Total:,WLD
Yemen,YEM
Zambia,ZMB
Zimbabwe,ZWE
"""

countries = {}
codes = {}
for lines in db.strip().split('\n'):
    line = lines.split(',')
    name = str(line[0])
    code = str(line[1])
    countries[name]=[code]
    codes[code]=name

