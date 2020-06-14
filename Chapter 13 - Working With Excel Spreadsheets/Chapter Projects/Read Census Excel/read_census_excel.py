#! python3
# read_census_excel.py - Tabulates population and number of census tracts for each county.

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet[f'B{row}'].value
    county = sheet[f'C{row}'].value
    pop = sheet[f'D{row}'].value
    print(state, county, pop)

    # Make sure the key for this state exists.
    county_data.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    county_data[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    county_data[state][county]['pop'] += int(pop)

# Open a new text file and write the contents of countyData to it.
print('Writing results...')
result_file = open('census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('Done.')