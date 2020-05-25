'''
pomber(HitHub) country name -> worldmeters country name 
2020-05-23
'''
#pomber(GitHub) country name,worldmeters country name

db="""
Afghanistan,Afghanistan
Albania,Albania
Algeria,Algeria
Andorra,Andorra
Angola,Angola
Antigua and Barbuda,Antigua and Barbuda
Argentina,Argentina
Armenia,Armenia
Australia,Australia
Austria,Austria
Azerbaijan,Azerbaijan
Bahamas,Bahamas
Bahrain,Bahrain
Bangladesh,Bangladesh
Barbados,Barbados
Belarus,Belarus
Belgium,Belgium
Belize,Belize
Benin,Benin
Bhutan,Bhutan
Bolivia,Bolivia
Bosnia and Herzegovina,Bosnia and Herzegovina
Botswana,Botswana
Brazil,Brazil
Brunei,Brunei
Bulgaria,Bulgaria
Burkina Faso,Burkina Faso
Burma,Myanmar
Burundi,Burundi
Cabo Verde,Cabo Verde
Cambodia,Cambodia
Cameroon,Cameroon
Canada,Canada
Central African Republic,CAR
Chad,Chad
Chile,Chile
China,China
Colombia,Colombia
Comoros,Comoros
Congo (Brazzaville),Congo
Congo (Kinshasa),Congo
Costa Rica,Costa Rica
Cote d'Ivoire,Ivory Coast
Croatia,Croatia
Cuba,Cuba
Cyprus,Cyprus
Czechia,Czechia
Denmark,Denmark
Djibouti,Djibouti
Dominica,Dominica
Dominican Republic,Dominican Republic
Ecuador,Ecuador
Egypt,Egypt
El Salvador,El Salvador
Equatorial Guinea,Equatorial Guinea
Eritrea,Eritrea
Estonia,Estonia
Eswatini,Eswatini
Ethiopia,Ethiopia
Fiji,Fiji
Finland,Finland
France,France
Gabon,Gabon
Gambia,Gambia
Georgia,Georgia
Germany,Germany
Ghana,Ghana
Greece,Greece
Grenada,Grenada
Guatemala,Guatemala
Guinea-Bissau,Guinea-Bissau
Guinea,Guinea
Guyana,Guyana
Haiti,Haiti
Holy See,
Honduras,Honduras
Hungary,Hungary
Iceland,Iceland
India,India
Indonesia,Indonesia
Iran,Iran
Iraq,Iraq
Ireland,Ireland
Israel,Israel
Italy,Italy
Jamaica,Jamaica
Japan,Japan
Jordan,Jordan
Kazakhstan,Kazakhstan
Kenya,Kenya
Korea South,S. Korea
Kuwait,Kuwait
Kyrgyzstan,Kyrgyzstan
Laos,Laos
Latvia,Latvia
Lebanon,Lebanon
Lesotho,Lesotho
Liberia,Liberia
Libya,Libya
Liechtenstein,Liechtenstein
Lithuania,Lithuania
Luxembourg,Luxembourg
Madagascar,Madagascar
Malawi,Malawi
Malaysia,Malaysia
Maldives,Maldives
Mali,Mali
Malta,Malta
Mauritania,Mauritania
Mauritius,Mauritius
Mexico,Mexico
Moldova,Moldova
Monaco,Monaco
Mongolia,Mongolia
Montenegro,Montenegro
Morocco,Morocco
Mozambique,Mozambique
Namibia,Namibia
Nepal,Nepal
Netherlands,Netherlands
New Zealand,New Zealand
Nicaragua,Nicaragua
Niger,Niger
Nigeria,Nigeria
North Macedonia,North Macedonia
Norway,Norway
Oman,Oman
Pakistan,Pakistan
Panama,Panama
Papua New Guinea,Papua New Guinea
Paraguay,Paraguay
Peru,Peru
Philippines,Philippines
Poland,Poland
Portugal,Portugal
Qatar,Qatar
Romania,Romania
Russia,Russia
Rwanda,Rwanda
Saint Kitts and Nevis,Saint Kitts and Nevis
Saint Lucia,Saint Lucia
Saint Vincent and the Grenadines,St. Vincent Grenadines
San Marino,San Marino
Sao Tome and Principe,Sao Tome and Principe
Saudi Arabia,Saudi Arabia
Senegal,Senegal
Serbia,Serbia
Seychelles,Seychelles
Sierra Leone,Sierra Leone
Singapore,Singapore
Slovakia,Slovakia
Slovenia,Slovenia
Somalia,Somalia
South Africa,South Africa
South Sudan,South Sudan
Spain,Spain
Sri Lanka,Sri Lanka
Sudan,Sudan
Suriname,Suriname
Sweden,Sweden
Switzerland,Switzerland
Syria,Syria
Taiwan*,Taiwan
Tajikistan,Tajikistan
Tanzania,Tanzania
Thailand,Thailand
Timor-Leste,Timor-Leste
Togo,Togo
Trinidad and Tobago,Trinidad and Tobago
Tunisia,Tunisia
Turkey,Turkey
US,USA
Uganda,Uganda
Ukraine,Ukraine
United Arab Emirates,UAE
United Kingdom,UK
Uruguay,Uruguay
Uzbekistan,Uzbekistan
Venezuela,Venezuela
Vietnam,Vietnam
West Bank and Gaza,
Western Sahara,Western Sahara
Yemen,Yemen
Zambia,Zambia
Zimbabwe,Zimbabwe
"""

countries = {}

for lines in db.strip().split('\n'):
    line = lines.split(',')
    name0 = str(line[0])
    name1 = str(line[1])
    countries[name0]=[name1]

