import pandas as pd
from bs4 import BeautifulSoup

html_string = '''
  <table>
        <tr class="table-dark-row">
            <td align="left" class="snapshot-td2-cp" title="cssbody=[tooltip_short_bdy] cssheader=[tooltip_short_hdr] body=[Stock has options trading on a market exchange] offsetx=[10] offsety=[20] delay=[300]" width="7%">Optionable</td><td align="left" class="snapshot-td2" width="8%"><b>Yes</b></td>
            <td align="left" class="snapshot-td2-cp" title="cssbody=[tooltip_short_bdy] cssheader=[tooltip_short_hdr] body=[Total Debt to Equity (mrq)] offsetx=[10] offsety=[20] delay=[300]" width="7%">Debt/Eq</td><td align="left" class="snapshot-td2" width="8%"><b><span class="is-red">1.69</span></b></td>
            <td align="left" class="snapshot-td2-cp" title="cssbody=[tooltip_short_bdy] cssheader=[tooltip_short_hdr] body=[Quarterly earnings growth (yoy)] offsetx=[10] offsety=[20] delay=[300]" width="7%">EPS Q/Q</td><td align="left" class="snapshot-td2" width="8%"><b><span class="is-green">34.60%</span></b></td>
            <td align="left" class="snapshot-td2-cp" title="cssbody=[tooltip_short_bdy] cssheader=[tooltip_short_hdr] body=[Net Profit Margin (ttm)] offsetx=[10] offsety=[20] delay=[300]" width="7%">Profit Margin</td><td align="left" class="snapshot-td2" width="8%"><b><span class="is-green">21.70%</span></b></td>
            <td align="left" class="snapshot-td2-cp" title="cssbody=[tooltip_short_bdy] cssheader=[tooltip_short_hdr] body=[Relative volume] offsetx=[10] offsety=[20] delay=[300]" width="7%">Rel Volume</td><td align="left" class="snapshot-td2" width="8%"><b>0.58</b></td>
            <td align="left" class="snapshot-td2-cp" title="cssbody=[tooltip_short_bdy] cssheader=[tooltip_short_hdr] body=[Previous close] offsetx=[10] offsety=[20] delay=[300]" width="7%">Prev Close</td><td align="left" class="snapshot-td2" width="8%"><b>135.13</b></td>
        </tr>
  </table>
'''

soup = BeautifulSoup(html_string, 'lxml')  # Parse the HTML as a string

table = soup.find_all('table')[0]  # Grab the first table

new_table = pd.DataFrame()  # I know the size

row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        print(column)
        # new_table.iat[row_marker, column_marker] = column.get_text()
        column_marker += 1

print(new_table)
