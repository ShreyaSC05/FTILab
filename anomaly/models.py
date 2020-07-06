from datetime import datetime
from anomaly import db

class event_config(db.Model):
    device_id = db.Column(db.String(10), unique=True, primary_key=True)
    device_name = db.Column(db.String(20), unique=True, nullable=False)

    congestion_detection_enable = db.Column(db.Boolean, default=False)
    congestion_detection_threshold = db.Column(db.Integer, default=00)
    congestion_detection_distance = db.Column(db.Decimal(60), default=00)

    lane_1_low_speed_enable = db.Column(db.Boolean, default=False)
    lane_1_low_speed_threshold = db.Column(db.Integer, default=00)
    lane_1_low_speed_distance = db.Column(db.Decimal(60), default=00)

    lane_2_low_speed_enable = db.Column(db.Boolean, nullable=False)
    lane_2_low_speed_threshold = db.Column(db.Integer, default=00)
    lane_2_low_speed_distance = db.Column(db.Decimal(60), default=00)

    date_created = db.Column(db.Datetime, default=datetime.utcnow)
    date_modified = db.Column(db.Datetime, default=datetime.utcnow)




class events(db.Model):
    device_id = db.Column(db.String(10), primary_key=True)
    device_name = db.Column(db.String(20), unique=True, nullable=False)

    event_type = db.Column(db.String(20),nullable=False)
    event_timestamp = db.Column(db.Datetime, default=datetime.utcnow)
    event_title = db.Column(db.String(20), nullable=False)
    event_description = db.Column(db.String(100), nullable=False)

    date_created = db.Column(db.Datetime, default=datetime.utcnow)
    date_modified = db.Column(db.Datetime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



