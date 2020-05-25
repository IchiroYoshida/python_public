'''
Worldmeters coronavirus (https://www.worldometers.info/coronavirus/)
Country, Population
2020-05-23
'''
#Country,Population

db = """
Afghanistan,38826954 
Albania,2878120 
Algeria,43761439 
Andorra,77252 
Angola,32743009 
Anguilla,14989 
Antigua and Barbuda,97842 
Argentina,45150850 
Armenia,2962665 
Aruba,106718 
Australia,25467448 
Austria,9000927 
Azerbaijan,10129286 
Bahamas,392836 
Bahrain,1694317 
Bangladesh,164510959 
Barbados,287338 
Belarus,9449644 
Belgium,11584289 
Belize,396811 
Benin,12085815 
Bermuda,62301 
Bhutan,770679 
Bolivia,11655388 
Bosnia and Herzegovina,3282865 
Botswana,2346198 
Brazil,212397420 
British Virgin Islands,30209 
Brunei,437024 
Bulgaria,6953654 
Burkina Faso,20835388 
Burundi,11848359 
CAR,4820296 
Cabo Verde,555327 
Cambodia,16693317 
Cameroon,26468556 
Canada,37706381 
Caribbean Netherlands,26197 
Cayman Islands,65637 
Chad,16369695 
Channel Islands,173689 
Chile,19098478 
China,1439323776 
Colombia,50823711 
Comoros,867471 
Congo,5502218 
Costa Rica,5089080 
Croatia,4107806 
Cuba,11327329 
Curaçao,164022 
Cyprus,1206416 
Czechia,10706906 
DRC,89234236 
Denmark,5790054 
Djibouti,986402 
Dominica,71967 
Dominican Republic,10836077 
Ecuador,17613161 
Egypt,102115130 
El Salvador,6482732 
Equatorial Guinea,1397381 
Eritrea,3540980 
Estonia,1326442 
Eswatini,1158855 
Ethiopia,114630633 
Faeroe Islands,48843 
Falkland Islands,3468 
Fiji,895748 
Finland,5539822 
France,65258400 
French Guiana,297772 
French Polynesia,280735 
Gabon,2219628 
Gambia,2408601 
Georgia,3989952 
Germany,83755775 
Ghana,30998526 
Gibraltar,33692 
Greece,10428193 
Greenland,56760 
Grenada,112468 
Guadeloupe,400117 
Guatemala,17877985 
Guinea,13090666 
Guinea-Bissau,1962592 
Guyana,786150 
Haiti,11387245 
Honduras,9886968 
Hong Kong,7490427 
Hungary,9662856 
Iceland,341006 
India,1378529934 
Indonesia,273208135 
Iran,83874391 
Iraq,40118148 
Ireland,4931752 
Isle of Man,84985 
Israel,9197590 
Italy,60470956 
Ivory Coast,26301903 
Jamaica,2959800 
Japan,126515903 
Jordan,10192121 
Kazakhstan,18752041 
Kenya,53634644 
Kuwait,4263538 
Kyrgyzstan,6512107 
Laos,7263819 
Latvia,1888237 
Lebanon,6828536 
Lesotho,2140421 
Liberia,5043867 
Libya,6860947 
Liechtenstein,38117 
Lithuania,2725949 
Luxembourg,624836 
Macao,648355 
Madagascar,27607404 
Malawi,19071854 
Malaysia,32320265 
Maldives,539469 
Mali,20181288 
Malta,441420 
Martinique,375295 
Mauritania,4635263 
Mauritius,1271548 
Mayotte,272048 
Mexico,128785048 
Moldova,4034922 
Monaco,39212 
Mongolia,3272373 
Montenegro,628058 
Montserrat,4992 
Morocco,36862538 
Mozambique,31151425 
Myanmar,54370772 
Namibia,2535696 
Nepal,29077526 
Netherlands,17130906 
New Caledonia,285200 
New Zealand,4818013 
Nicaragua,6615901 
Niger,24098369 
Nigeria,205542168 
North Macedonia,2083383 
Norway,5416680 
Oman,5091392 
Pakistan,220403741 
Palestine,5087651 
Panama,4307167 
Papua New Guinea,8927762 
Paraguay,7122901 
Peru,32920920 
Philippines,109419831 
Poland,37850876 
Portugal,10199740 
Qatar,2875579 
Romania,19250526 
Russia,145927974 
Rwanda,12914674 
Réunion,894627 
S. Korea,51264600 
Saint Kitts and Nevis,53159 
Saint Lucia,183538 
Saint Martin,38592 
Saint Pierre Miquelon,5797 
San Marino,33924 
Sao Tome and Principe,218697 
Saudi Arabia,34753259 
Senegal,16691939 
Serbia,8740939 
Seychelles,98282 
Sierra Leone,7958421 
Singapore,5845390 
Sint Maarten,42823 
Slovakia,5459368 
Slovenia,2078908 
Somalia,15840585 
South Africa,59226304 
South Sudan,11179329 
Spain,46752901 
Sri Lanka,21403762 
St. Barth,9874 
St. Vincent Grenadines,110903 
Sudan,43730378 
Suriname,586063 
Sweden,10092543 
Switzerland,8647829 
Syria,17451066 
Taiwan,23812274 
Tajikistan,9512877 
Tanzania,59531669 
Thailand,69781627 
Timor-Leste,1315590 
Togo,8256184 
Trinidad and Tobago,1399011 
Tunisia,11805138 
Turkey,84239988 
Turks and Caicos,38659 
UAE,9877270 
UK,67848130 
USA,330795837 
Uganda,45566443 
Ukraine,43760129 
Uruguay,3472463 
Uzbekistan,33415264 
Vatican City,801 
Venezuela,28444157 
Vietnam,97243794 
Western Sahara,595623 
Yemen,29750177 
Zambia,18322805 
Zimbabwe,14838856
"""

countries = {}

for lines in db.strip().split('\n'):
    line = lines.split(',')
    name = str(line[0])
    pop  = int(line[1])
    countries[name]=[pop]


