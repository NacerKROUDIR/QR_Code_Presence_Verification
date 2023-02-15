# Presence Verification System
## By Nacer KROUDIR

The purpose of this program is to generate qr codes for visitors and to mark their presence or absence after scanning
the qr code

## Requirement:
- To run this project on your local machine, you will need to have Python 3 installed. You can install these dependencies by running the following commands in your terminal:

```
pip install pandas
pip install opencv-python
pip install pyqrcode
```

- The folder of the images generated must be in the same directory as the program.
- The csv file should preferably be in the same directory as the program (PS: An example of the csv file format is included)

## Guide:

- `generate` function is run to generate the qr codes for the visitors (PS: The qr code will contain the email of the visitor).
for the case of a workshop: in the beginning of every session you need to run `add_session` function with the data frame 
as an argument. The function will simply add a column to your data frame.

> PS: the name of the session is generated automatically
- `verify` function is run to verify the qr code and mark the presence of the visitor.
- The different outputs of `verify` function:
1. if the session does not exist the code will print `{session} Does Not Exist!`
2. if the visitor is not included in the list the code will print `{content of qr_code} Does Not Have Access!`
3. if the visitor is included in the list and is marked absent the code will mark him as present and print `{name} Attendance Confirmed`
4. if the visitor is included in the list and is already marked present then the code will print `{name} Attendance Already Confirmed!`
