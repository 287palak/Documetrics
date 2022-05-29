import csv
import joblib
import face_recognition
import pandas as pd

saved_model = joblib.load('./trained.pkl')
student = pd.read_csv('./dataset_engage/student_id.csv')


def chk_id(aadhar):
    count=0
    stu = pd.read_csv('./dataset_engage/student_id.csv')
    for i in stu['Aadhar']:
        i_n = str(i)
        if(i_n == aadhar[0]):
            student_id = stu['Student ID'][count]
            return student_id
        count=count+1
    return 0


def chk_exam(unique_id,exam):
    count=0
    ex = pd.read_csv('./dataset_engage/exams.csv')
    for j in ex['Unique ID']:
        print(j)
        print(type(j))
        print(unique_id)
        print(type(unique_id))
        if j == unique_id:
            if exam == ex['Exam'][count]:
                return 1
        count = count+1
    return 0


def make_student_id(aadhar):
    student = pd.read_csv('./dataset_engage/student_id.csv')
    student_id = 10000+len(student)
    filename = "./dataset_engage/student_id.csv"
    with open(filename, 'a') as csvfile:
        rows = [student_id,	*aadhar]
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows csvwriter.writerow(rows)
        csvwriter.writerow(rows)
    return student_id


def register_exam(id, exam):
    filename = "./dataset_engage/exams.csv"
    with open(filename, 'a') as csvfile:
        rows = [ id,	exam]
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows csvwriter.writerow(rows)
        csvwriter.writerow(rows)
    return rows


def display_stu_reg(aadhar, name,exam,id):
    results = dict(ADH_no = [],
                   UNI_ID = [],
                   name = [],
                   exam_name = [])
    results['ADH_no'].append(*aadhar)
    results['UNI_ID'].append(id)
    results['name'].append(name)
    results['exam_name'].append(exam)
    return results


def face_testing(img):
    # Load the test image with unknown faces into a numpy array
    test = face_recognition.load_image_file(img)
    # Find all the faces in the test image using the default HOG-based model
    face_locations = face_recognition.face_locations(test)
    no = len(face_locations)
    print("Number of faces detected: ", no)
    print("Found:")
    if no==0:
        print('no faces found ')
        return
    else:
        for i in range(no):
            test_image_enc = face_recognition.face_encodings(test)[i]
            name = saved_model.predict([test_image_enc])
        return name


def student_register(name, photo, exam):
    # generating aadhar
    chk_aadhar = face_testing(photo)
    aadhar_no = chk_aadhar

    # check if id exists
    id = chk_id(aadhar_no)
    # if id doesn't exist
    if id == 0:
        id = make_student_id(aadhar_no)
        register_exam(id, exam)
        data = display_stu_reg(aadhar_no, name, exam, id)
        return data

    # if id already exists
    else:
        ex = chk_exam(id, exam)

        # student already registered for exam
        if ex == 1:
            data = display_stu_reg(aadhar_no, name, exam, id)
            return data

        # student not registered for exam
        else:
            register_exam(id, exam)
            data = display_stu_reg(aadhar_no, name, exam, id)
            return data


def student_authentication(name, photo, exam):
    #generating aadhar
    chk_aadhar = face_testing(photo)
    aadhar_no = chk_aadhar

    #check if id exists
    id = chk_id(aadhar_no)
    #if id doesn't exist
    if (id==0):
        print('student not registered for exam: AUTHENTICATION FAILED')
        data = dict(ADH_no=[],
                    UNI_ID=[],
                    name=[],
                    exam_name=[])
        data['ADH_no'].append(0)
        data['UNI_ID'].append(0)
        data['name'].append(0)
        data['exam_name'].append(0)
        return data

    #if id already exists
    else:
        ex = chk_exam(id,exam)
        #student already registered for exam
        if(ex==1):
            data = display_stu_reg(aadhar_no, name,exam,id)
            return data
        #student not registered for exam
        else:
            print('student not registered for exam: AUTHENTICATION FAILED')
            data = dict(ADH_no=[],
                           UNI_ID=[],
                           name=[],
                           exam_name=[])
            data['ADH_no'].append(0)
            data['UNI_ID'].append(0)
            data['name'].append(0)
            data['exam_name'].append(0)
            return data