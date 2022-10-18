import json
import pandas as pd
import uuid
import pymysql


class Config:
    def __init__(self):
        self.db_conn = pymysql.connect( host="67.205.163.33",
                                        user="oar8",
                                        password="InfSci1500_4173812",
                                        db="oar8",
                                        charset="utf8mb4",
                                        cursorclass=pymysql.cursors.DictCursor)



class doctor:
    def __init__(self, f, l, doctor_id = ""):
        self.__f_name = f
        self.__l_name = l

        if doctor_id == "":
            self.__doctor_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO doctor (doctor_id, first_name, last_name)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__doctor_id, self.__f_name, self.__l_name)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__doctor_id = doctor_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM doctor WHERE doctor_id = '" + doctor_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__doctor_id = row["doctor_id"]
                        self.__f_name = row["first_name"]
                        self.__l_name = row["last_name"]
            finally:
                con.close()




    def get_doc_id(self):
        return self.__doctor_id

    # getter method
    def get_f_name(self):
        return self.__f_name
      
    # setter method
    def set_f_name(self, f):
        self.__f_name = f
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET f_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()

    # getter method
    def get_l_name(self):
        return self.__l_name
      
    # setter method
    def set_l_name(self, l):
        self.__l_name = l
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET l_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()


    def to_json(self):
        return json.dumps(self.__dict__)
    






class patient:
    def __init__(self, f, l, patient_id = ""):
        
        self.__f_name = f
        self.__l_name = l

        if patient_id == "":
            self.__patient_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO patient (patient_id, first_name, last_name)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__patient_id, self.__f_name, self.__l_name)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__patient_id = patient_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM patient WHERE patient_id = '" + patient_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__patient_id = row["patient_id"]
                        self.__f_name = row["first_name"]
                        self.__l_name = row["last_name"]
            finally:
                con.close()




    def get_patient_id(self):
        return self.__patient_id

    # getter method
    def get_f_name(self):
        return self.__f_name
      
    # setter method
    def set_f_name(self, f):
        self.__f_name = f
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET f_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__f_name, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()

    # getter method
    def get_l_name(self):
        return self.__l_name
      
    # setter method
    def set_l_name(self, l):
        self.__l_name = l
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE doctor SET l_name = %s WHERE doctor_id = %s;'
                print(qry)
                cur.execute(qry, (self.__l_name, self.__doctor_id)) 
                con.commit()
        finally:
            con.close()

    def to_json(self):
        return json.dumps(self.__dict__)






class visit:
    def __init__(self, date, r, doc, pat, visit_id = ""):
        self.__visit_date = date
        self.__visit_reason = r
        self.__fk_doctor_id = doc
        self.__fk_patient_id = pat


        if visit_id == "":
            self.__visit_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO visit (visit_id, visit_date, visit_reason, fk_doctor_id, fk_patient_id)'
                    qry = qry + 'VALUES(%s, %s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__visit_id, self.__visit_date, self.__visit_reason, self.__fk_doctor_id, self.__fk_patient_id)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__visit_id = visit_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM visit WHERE visit_id = '" + visit_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__visit_id = row["visit_id"]
                        self.__visit_date = row["visit_date"]
                        self.__visit_reason = row["visit_reason"]
                        self.__fk_doctor_id = row["fk_doctor_id"]
                        self.__fk_patient_id = row["fk_patient_id"]
            finally:
                con.close()




    def get_visit_id(self):
        return self.__visit_id

    # getter method
    def get_visit_date(self):
        return self.__visit_date
      
    # setter method
    def set_visit_date(self, x):
        self.__visit_date = x
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET visit_date = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__visit_date, self.__visit_id)) 
                con.commit()
        finally:
            con.close()

    # getter method
    def get_visit_reason(self):
        return self.__visit_reason
      
    # setter method
    def set_visit_reason(self, x):
        self.__visit_reason = x
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE visit SET visit_reason = %s WHERE visit_id = %s;'
                print(qry)
                cur.execute(qry, (self.__visit_reason, self.__visit_id)) 
                con.commit()
        finally:
            con.close()

    # getter method
    def get_fk_doctor_id(self):
        return self.__fk_doctor_id

    # getter method
    def get_fk_patient_id(self):
        return self.__fk_patient_id


    def to_json(self):
        return json.dumps(self.__dict__)

    





class diagnosis:
    def __init__(self, n, d, diagnosis_id = ""):
        self.__diagnosis_name = n
        self.__diagnosis_description = d

        if diagnosis_id == "":
            self.__diagnosis_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO diagnosis (diagnosis_id, diagnosis_name, diagnosis_description)'
                    qry = qry + 'VALUES(%s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__diagnosis_id, self.__diagnosis_name, self.__diagnosis_description)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__diagnosis_id = diagnosis_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM diagnosis WHERE diagnosis_id = '" + diagnosis_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__diagnosis_id = row["diagnosis_id"]
                        self.__diagnosis_name = row["diagnosis_name"]
                        self.__diagnosis_description = row["diagnosis_description"]
            finally:
                con.close()



    def get_diagnosis_id(self):
        return self.__diagnosis_id

    # getter method
    def get_diagnosis_name(self):
        return self.__diagnosis_name
      
    # setter method
    def set_diagnosis_name(self, x):
        self.__diagnosis_name = x
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET diagnosis_reason = %s WHERE diagnosis_id = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis_name, self.__diagnosis_id)) 
                con.commit()
        finally:
            con.close()

    # getter method
    def get_diagnosis_description(self):
        return self.__diagnosis_description
      
    # setter method
    def set_diagnosis_description(self, x):
        self.__diagnosis_description = x
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE diagnosis SET diagnosis_description = %s WHERE diagnosis_id = %s;'
                print(qry)
                cur.execute(qry, (self.__diagnosis_description, self.__diagnosis_id)) 
                con.commit()
        finally:
            con.close()

    def to_json(self):
        return json.dumps(self.__dict__)




class procedure_table:
    def __init__(self, n, d, s, procedure_id = ""):
        self.__procedure_name = n
        self.__procedure_description = d
        self.__successful = s

        if procedure_id == "":
            self.__procedure_id = str(uuid.uuid4())
            try: 
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = 'INSERT INTO procedure (procedure_id, procedure_name, procedure_description, successful)'
                    qry = qry + 'VALUES(%s, %s, %s, %s)'
                    print(qry)
                    cur.execute(qry, (self.__procedure_id, self.__procedure_name, self.__procedure_description, self.__successful)) 
                    con.commit()
            finally:
                con.close()
        else:
            self.__procedure_id = procedure_id
            try:
                config = Config()
                con = config.db_conn
                with con.cursor() as cur:
                    qry = "SELECT * FROM procedure WHERE procedure_id = '" + procedure_id + "'"
                    print(qry)
                    cur.execute(qry)
                    rows = cur.fetchall()
                    for row in rows:
                        self.__procedure_id = row["procedure_id"]
                        self.__procedure_name = row["procedure_name"]
                        self.__procedure_description = row["procedure_description"]
                        self.__successful = row["successful"]
            finally:
                con.close()


    def get_procedure_id(self):
        return self.__procedure_id

    # getter method
    def get_procedure_name(self):
        return self.__procedure_name
      
    # setter method
    def set_procedure_name(self, x):
        self.__procedure_name = x
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_table SET procedure_reason = %s WHERE procedure_id = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure_name, self.__procedure_id)) 
                con.commit()
        finally:
            con.close()

    # getter method
    def get_procedure_description(self):
        return self.__procedure_description
      
    # setter method
    def set_procedure_description(self, x):
        self.__procedure_description = x
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_table SET procedure_description = %s WHERE procedure_id = %s;'
                print(qry)
                cur.execute(qry, (self.__procedure_description, self.__procedure_id)) 
                con.commit()
        finally:
            con.close()
    
    # getter method
    def get_successful(self):
        return self.__successful
      
    # setter method
    def set_successful(self, x):
        self.__successful = x
        try: 
            config = Config()
            con = config.db_conn
            with con.cursor() as cur:
                qry = 'UPDATE procedure_table SET successful = %s WHERE procedure_id = %s;'
                print(qry)
                cur.execute(qry, (self.__successful, self.__procedure_id)) 
                con.commit()
        finally:
            con.close()

    def to_json(self):
        return json.dumps(self.__dict__)


class visit_procedure:
    def __init__(self, doc, pat):
        self.__fk_visit_id = doc
        self.__fk_procedure_id = pat
    
    # getter method
    def get_fk_visit_id(self):
        return self.__fk_visit_id

    # getter method
    def get_fk_procedure_id(self):
        return self.__fk_procedure_id



class visit_diagnosis:
    def __init__(self, doc, pat):
        self.__fk_visit_id = doc
        self.__fk_diagnosis_id = pat
    
    # getter method
    def get_fk_visit_id(self):
        return self.__fk_visit_id

    # getter method
    def get_fk_diagnosis_id(self):
        return self.__fk_diagnosis_id










