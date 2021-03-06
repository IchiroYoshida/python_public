'''
 country name -> continent
 2020-06-02

'''

db="""
West Bank and Gaza,Asia
Kosovo,Europe
USA,North America
Brazil,South America
Russia,Europe
Spain,Europe
UK,Europe
Italy,Europe
India,Asia
France,Europe
Germany,Europe
Peru,South America
Turkey,Asia
Iran,Asia
Chile,South America
Mexico,North America
Canada,North America
Saudi Arabia,Asia
Pakistan,Asia
Belgium,Europe
Qatar,Asia
Bangladesh,Asia
Netherlands,Europe
Belarus,Europe
Ecuador,South America
Sweden,Europe
Singapore,Asia
UAE,Asia
South Africa,Africa
Portugal,Europe
Switzerland,Europe
Colombia,South America
Kuwait,Asia
Indonesia,Asia
Egypt,Africa
Ireland,Europe
Poland,Europe
Ukraine,Europe
Romania,Europe
Philippines,Asia
Dominican Republic,North America
Argentina,South America
Israel,Asia
Japan,Asia
Austria,Europe
Afghanistan,Asia
Panama,North America
Oman,Asia
Bahrain,Asia
Denmark,Europe
S. Korea,Asia
Serbia,Europe
Kazakhstan,Asia
Nigeria,Africa
Bolivia,South America
Algeria,Africa
Armenia,Asia
Czechia,Europe
Norway,Europe
Moldova,Europe
Ghana,Africa
Malaysia,Asia
Morocco,Africa
Australia,Australia/Oceania
Finland,Europe
Iraq,Asia
Cameroon,Africa
Azerbaijan,Asia
Honduras,North America
Guatemala,North America
Sudan,Africa
Luxembourg,Europe
Tajikistan,Asia
Hungary,Europe
Guinea,Africa
Senegal,Africa
Uzbekistan,Asia
Djibouti,Africa
DRC,Africa
Thailand,Asia
Ivory Coast,Africa
Greece,Europe
Gabon,Africa
El Salvador,North America
Bosnia and Herzegovina,Europe
Bulgaria,Europe
North Macedonia,Europe
Croatia,Europe
Haiti,North America
Cuba,North America
Somalia,Africa
Kenya,Africa
Mayotte,Africa
Estonia,Europe
Maldives,Asia
Kyrgyzstan,Asia
Nepal,Asia
Iceland,Europe
Lithuania,Europe
Sri Lanka,Asia
Slovakia,Europe
Venezuela,South America
New Zealand,Australia/Oceania
Slovenia,Europe
Guinea-Bissau,Africa
Mali,Africa
Equatorial Guinea,Africa
Ethiopia,Africa
Lebanon,Asia
Albania,Europe
Zambia,Africa
Hong Kong,Asia
Tunisia,Africa
Costa Rica,North America
CAR,Africa
Latvia,Europe
Paraguay,South America
South Sudan,Africa
Niger,Africa
Cyprus,Asia
Sierra Leone,Africa
Burkina Faso,Africa
Madagascar,Africa
Uruguay,South America
Georgia,Asia
Chad,Africa
Andorra,Europe
Nicaragua,North America
Jordan,Asia
Diamond Princess,
San Marino,Europe
Malta,Europe
Congo,Africa
Mauritania,Africa
Jamaica,North America
Channel Islands,Europe
Tanzania,Africa
French Guiana,South America
Sao Tome and Principe,Africa
Réunion,Africa
Cabo Verde,Africa
Uganda,Africa
Palestine,Asia
Togo,Africa
Taiwan,Asia
Rwanda,Africa
Yemen,Asia
Isle of Man,Europe
Malawi,Africa
Mauritius,Africa
Vietnam,Asia
Montenegro,Europe
Liberia,Africa
Eswatini,Africa
Mozambique,Africa
Benin,Africa
Myanmar,Asia
Zimbabwe,Africa
Martinique,North America
Faeroe Islands,Europe
Mongolia,Asia
Gibraltar,Europe
Libya,Africa
Guadeloupe,North America
Guyana,South America
Cayman Islands,North America
Bermuda,North America
Brunei,Asia
Cambodia,Asia
Syria,Asia
Trinidad and Tobago,North America
Comoros,Africa
Bahamas,North America
Aruba,North America
Monaco,Europe
Barbados,North America
Angola,Africa
Liechtenstein,Europe
Sint Maarten,North America
Burundi,Africa
French Polynesia,Australia/Oceania
Macao,Asia
Suriname,South America
Bhutan,Asia
Saint Martin,North America
Eritrea,Africa
Botswana,Africa
Antigua and Barbuda,North America
St. Vincent Grenadines,North America
Gambia,Africa
Namibia,Africa
Timor-Leste,Asia
Grenada,North America
New Caledonia,Australia/Oceania
Curaçao,North America
Laos,Asia
Belize,North America
Fiji,Australia/Oceania
Saint Lucia,North America
Dominica,North America
Saint Kitts and Nevis,North America
Falkland Islands,South America
Greenland,North America
Turks and Caicos,North America
Vatican City,Europe
Montserrat,North America
Seychelles,Africa
Western Sahara,Africa
British Virgin Islands,North America
Papua New Guinea,Australia/Oceania
Caribbean Netherlands,North America
St. Barth,North America
Anguilla,North America
Lesotho,Africa
Saint Pierre Miquelon,North America
China,Asia
"""

continents = {}

for lines in db.strip().split('\n'):
    line = lines.split(',')
    country = str(line[0])
    continent = str(line[1])
    continents[country]=[continent]

