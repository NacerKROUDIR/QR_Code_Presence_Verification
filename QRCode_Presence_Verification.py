import cv2
import pandas as pd
import pyqrcode


"""Create a folder named 'QR_Codes' in the same directory to store the generated qr codes in
   The csv file needs to be in the same directory as the program
   Guide:
   To generate the qr codes for the participants run 'generate' function with the data frame as an argument

   In the beginning of every session you need to run 'add_session' function with the data frame as an argument
   to add a new session column in the data frame
   PS: the name of the session is generated automatically

   To verify the qr code run 'verify' function with the arguments (data frame, session name)
   """


def verify(workshop, session):
    """workshop is the dataframe
       session is the name of the column preferably the date or the number of that session"""
    qrCodeDetector = cv2.QRCodeDetector()
    video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        check, frame = video.read()
        email, points, _ = qrCodeDetector.detectAndDecode(frame)
        if email == '':
            pass
        else:
            """if the session does not exist the code will print 'Session {session} does not exist!'
               if the student email does not exist in the list the code will print 'Student\'s email {email} does not exist!'
               if the student exist and is marked absent the code will mark him as present and print 'Code scanned successfully'
               if the student exist and is already marked present then the code will print'Code already scanned!'"""
            try:
                if workshop[workshop['Email'] == email][session].bool() == False:
                    temp = workshop.index[workshop['Email']==email]
                    workshop.at[temp, session] = True
                    workshop.to_csv(csv_path, index=False)
                    name = workshop.loc[temp, 'Full name'].values[0]
                    print(f'{name} Attendance Registered')
                    cv2.waitKey(3000)
                else:
                    temp = workshop.index[workshop['Email'] == email]
                    name = workshop.loc[temp, 'Full name'].values[0]
                    print(f'{name} Already Registered')
                    cv2.waitKey(3000)
                continue
            except ValueError:
                print(f'{email} Does Not Have Access!')
                cv2.waitKey(2000)
                continue
            except KeyError:
                print(f'{session} Does Not Exist!')
                break
        cv2.imshow('Capturing...', frame)
        k = cv2.waitKey(250)
        if k == ord(' '):
            break
    video.release()
    cv2.destroyAllWindows()


def session_name_generator(workshop):
    """workshop is the dataframe"""
    num = 1
    columns = workshop.columns
    session_name = f"Session {num}"
    while session_name in columns:
        num += 1
        session_name = f"Session {num}"
    return session_name


def add_session(workshop):
    """workshop is the dataframe"""
    l = []
    for i in range(workshop.shape[0]):
        l.append(False)
    session = session_name_generator(workshop)
    workshop[session] = l
    workshop.to_csv(csv_path, index=False)


def generate(workshop=df, folder='QR_Codes'):
    """workshop is the dataframe
       folder is the folder to save the qr codes into (it must be on the same path)"""
    emails = workshop['Email']
    for email in emails:
        picture = pyqrcode.create(email)
        picture.png(f'{folder}/{email}.png', scale=10)


csv_path = 'group2.csv'
df = pd.read_csv(csv_path)
# generate(df, 'QR_Codes')
# add_session(df)
# verify(df, 'Session 1')
