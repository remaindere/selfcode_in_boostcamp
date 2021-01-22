import csv

row_count = 0
header = []
duk_sung_w_high_school_cam_data = []

with open("seoul_bukchon_cctv_foottrafic_data.csv", "r", encoding="cp949") as s_file :
    csv_data = csv.reader(s_file)
    for row in csv_data :
        if row_count == 0 :
            header = row
        camera_des = row[3]
        if camera_des.find(u"덕성여고 앞") != -1:
            duk_sung_w_high_school_cam_data.append(row)
        row_count +=1

with open("duk_sung_w_high_school_cam_data.csv", "w", encoding="utf-8") as d_file :
    writer = csv.writer(d_file, delimiter=',', quotechar="\"", quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    for row in duk_sung_w_high_school_cam_data :
        writer.writerow(row)