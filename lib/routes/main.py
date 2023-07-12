# Author: Sakthi Santhosh
# Created on: 29/05/2023
from datetime import datetime
from flask import (
    make_response,
    jsonify,
    render_template,
    request
)

from lib import app_handle, db_handle, log_handle, socket_handle
from lib.actions import NotificationDispatcher
from lib.constants import EMAIL_LIMIT_PERIOD_S, PREDICTION_THRESHOLD
from lib.models import Device, Event, Responder

last_event = datetime(2023, 1, 1, 12, 0, 0)

@app_handle.route('/')
def index_handle():
    return render_template("index.html")

@app_handle.route("/add_event", methods=["POST"])
def add_event_handle():
    global last_event

    payload = request.get_json()
    device = Device.query.filter_by(device_id=payload["device_id"]).first()

    if device is None:
        log_handle.error("Access is not granted for device with ID \"%s\"."%(payload["device_id"]))
        return make_response(jsonify(response="auth_error"), 401)

    dt = datetime.now()
    device.last_updated = datetime.now()

    db_handle.session.add(Event(
        datetime=dt,
        device_id=payload["device_id"],
        prediction=payload["prediction"],
        image=payload["image"]
    ))
    db_handle.session.commit()

    socket_handle.emit("new_data", {
        "datetime": str(dt),
        "image": payload["image"],
        "location": f"{device.latitude},{device.longitude}",
        "name": device.name,
        "prediction": payload["prediction"]
    })

    log_handle.debug("Prediction: " + str(payload["prediction"]))
    if (
        payload["prediction"] > PREDICTION_THRESHOLD
        and (dt - last_event).total_seconds() > EMAIL_LIMIT_PERIOD_S
    ):
        responders = Responder.query.all()

        if responders:
            first_responders = {
                "email_ids": [],
                "phones": []
            }

            for responder in responders:
                first_responders["email_ids"].append(responder.email_id)
                first_responders["phones"].append(responder.phone)

            log_handle.critical("Human intrusion detected. Informing first responders...")
            NotificationDispatcher(first_responders, {
                "datetime": str(dt),
                "image": payload["image"],
                "location": "%f,%f"%(device.latitude, device.longitude),
                "name": device.name,
            }).notify()
    last_event = dt
    return make_response(jsonify(response="success"), 200)

@app_handle.errorhandler(404)
def error404_handle(error):
    return render_template("error404.html")
