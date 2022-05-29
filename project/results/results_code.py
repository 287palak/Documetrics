import joblib
import face_recognition
import pandas as pd

saved_model = joblib.load('./trained.pkl')
data = pd.read_csv('./dataset_engage/results.csv')


#the face recognition model- compares the faces entered with those present in the database
def face_testing(img):
    results = dict(ADH_no = [],
                   UNI_ID = [],
                   name = [],
                   exam_name = [],
                   result = [],
                   crt_no = [])

    # Load the test image with unknown faces into a numpy array
    test = face_recognition.load_image_file(img)
    # Find all the faces in the test image using the default HOG-based model
    face_locations = face_recognition.face_locations(test)
    no = len(face_locations)
    print("Number of faces detected: ", no)
    # Predict all the faces in the test image using the trained classifier
    print("Found:")
    for i in range(no):
        test_image_enc = face_recognition.face_encodings(test)[i]
        name = saved_model.predict([test_image_enc])
    b = 0
    for i in data['Aadhar']:
        i_n = str(i)
        if (i_n == name[0]):
            results['ADH_no'].append(data.iloc[b,0])
            results['UNI_ID'].append(data.iloc[b, 1])
            results['name'].append(data.iloc[b,2])
            results['exam_name'].append(data.iloc[b,3])
            results['result'].append(data.iloc[b,4])
            results['crt_no'].append(data.iloc[b,5])
        b = b + 1
    return results

#function to check the otp entered by the user
def otp_testing(otp):
    results = dict(ADH_no = [],
                   UNI_ID = [],
                   name = [],
                   exam_name = [],
                   result = [],
                   crt_no = [])
    print(otp)
    print(type(otp))
    b = 0
    for i_n in data['OTP']:
        if (i_n == otp):
            results['ADH_no'].append(data.iloc[b,0])
            results['UNI_ID'].append(data.iloc[b, 1])
            results['name'].append(data.iloc[b,2])
            results['exam_name'].append(data.iloc[b,3])
            results['result'].append(data.iloc[b,4])
            results['crt_no'].append(data.iloc[b,5])
        b = b + 1
    return results


ADH_data = pd.read_csv('./dataset_engage/Aadhar_data .csv')
stu_rec = pd.read_csv('./dataset_engage/student_id.csv')


def stu_id_testing(stu_id):
    results = dict(ADH_no = [],
                   UNI_ID = [],)
    # print(stu_id)
    # print(type(stu_id))
    b = 0
    for i_n in stu_rec['Student ID']:
        if (i_n == stu_id):
            adh = stu_rec.iloc[b,1]
            results['UNI_ID'].append(stu_rec.iloc[b, 1])
        b = b + 1

    c = 0
    details = dict(ADH_no = [],
                   UNI_ID = [],
                   Name = [],)
    print(adh)
    print(type(adh))
    for i_n in ADH_data['Aadhar No']:
        if (i_n == adh):
            details['ADH_no'].append(ADH_data.iloc[c,0])
            details['UNI_ID'].append(stu_id)
            details['Name'].append(ADH_data.iloc[c,1])
            print(details)
        c = c + 1
    return details


