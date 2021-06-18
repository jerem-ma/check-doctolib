# check-doctolib
Python script used to check available doctolib apointments each t time and send notification if there is one

## Requirements
- Python
- Requests (Python module)
- PyGObject

## Usage
### Get API link
- Open your browser
- Press F12 to open developer console
- Open network tab
- Go to your doctor page and try to get availables apointments
- Check on the developer console a link containing `availabilities.json` and write it down
- Here is what you could get:
`https://www.doctolib.fr/availabilities.json?start_date=2021-06-18&visit_motive_ids=689642&agenda_ids=117589&insurance_sector=public&practice_ids=43475&limit=3`
- Replace start_date value by `' + str(tmp_begin_date) + '`
`https://www.doctolib.fr/availabilities.json?start_date=' + str(tmp_begin_date) + '&visit_motive_ids=689642&agenda_ids=117589&insurance_sector=public&practice_ids=43475&limit=3`
- Change limit value to 14
`https://www.doctolib.fr/availabilities.json?start_date=' + str(tmp_begin_date) + '&visit_motive_ids=689642&agenda_ids=117589&insurance_sector=public&practice_ids=43475&limit=14`
- Write down this final link

### Replace link in code
- Go through code to the definition of availabilities_link and change the default one to the one you found in last part

### Usage
- Type this in a terminal:
`python check_doctolib.py`
