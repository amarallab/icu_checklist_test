import MySQLdb as mdb
import csv

def download_table(conn, name, filename):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(name))

    with open(filename, 'wt') as f:
        wf = csv.writer(f, dialect='excel')
        column_names = [field[0] for field in cur.description]
        wf.writerow(column_names)
        for row in cur.fetchall():
            wf.writerow(row)

def download_sql():
    conn = mdb.connect(host='127.0.0.1', user='analyst', passwd='analyst', db='icuchecklist', port=7777)
    table_list = ["icuchecklist.auth_group", "icuchecklist.auth_group_permissions", 
        "icuchecklist.auth_permission", "icuchecklist.auth_user", "icuchecklist.auth_user_groups", 
        "icuchecklist.auth_user_user_permissions", "icuchecklist.backend_backendtoken", 
        "icuchecklist.backend_beaconconfiguration", "icuchecklist.backend_beaconconfigurationregion", 
        "icuchecklist.backend_challenge", "icuchecklist.backend_checklist", 
        "icuchecklist.backend_clearpatient", "icuchecklist.backend_feedback", 
        "icuchecklist.backend_patient", "icuchecklist.backend_patientdetailentry", 
        "icuchecklist.backend_patientresponse", "icuchecklist.backend_tmetryentrybeacon", 
        "icuchecklist.backend_tmetryentry", "icuchecklist.backend_userdata", 
        "icuchecklist.django_admin_log", "icuchecklist.django_content_type", 
        "icuchecklist.django_migrations", "icuchecklist.django_session", 
        "icuchecklist.mockup_backendtoken", "icuchecklist.mockup_patient"]

    for table in table_list:
        save_name = '../../data/iphone_responses/' + table.split('.')[1] + '.csv'
        download_table(conn, table, save_name)
    conn.close()

download_sql()
