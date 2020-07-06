from anomaly import tables, db, app
from anomaly.tables import event_config

@app.route('/', methods=['GET'])
def add_config(data):
    if event_config.device_id:
        e1 = event_config.query.add(data)
        db.session.commit()


def edit_config(device_id, data):
    try:

        if event_config.device_id == id:
            edit_record = event_config.query.filter_by(id).all()
            edit_record.update(data)
            db.session.commit()
        else:
            return "Incorrect Device_id provided. Please give a valid id."

    except Exception as e:
        return False

    return True


@app.route('/', methods=['GET'])
def delete_config(id):
    if event_config.device_id==id:
        delete_record = event_config.query.filter_by(id).all()
        delete_record.delete()
        db.session.commit()

    else:
        return "Incorrect Device_id provided. Please give a valid id."

def get_config_one(query):
    pass

def get_all_config(query):
    pass

def congestion_detection(congestion_detection_enable):
    if congestion_detection_enable is True:
        congestion_detection_threshold = 00
        congestion_detection_distance = 00

def congestion_detection(lane_1_low_speed_enable):
    if lane_1_low_speed_enable is True:
        lane_1_low_speed_threshold = 00
        lane_1_low_speed_distance = 00

def congestion_detection(lane_2_low_speed_enable):
    if lane_2_low_speed_enable is True:
        lane_2_low_speed_threshold = 00
        lane_2_low_speed_distance = 00



