# Author: Sakthi Santhosh
# Created on: 29/05/2023
from flask import (
    flash,
    redirect,
    render_template,
    url_for
)
from uuid import uuid4

from lib import app_handle, db_handle, log_handle
from lib.constants import MAPS_LINK
from lib.forms import AddDevice
from lib.models import Device

@app_handle.route("/add_device", methods=["GET", "POST"])
def add_device_handle():
    form = AddDevice()

    if form.validate_on_submit():
        device_id = str(uuid4())

        db_handle.session.add(Device(
            device_id=device_id,
            latitude=form.latitude.data,
            longitude=form.longitude.data,
            name=form.name.data
        ))
        db_handle.session.commit()

        message = f"Device with ID \"{device_id}\" was added successfully."

        log_handle.info(message)
        flash(message)
        return redirect(url_for("devices_handle"))
    return render_template("add_device.html", form=form)

@app_handle.route("/devices")
def devices_handle():
    data = Device.query.all()
    return render_template("devices.html", devices=data, maps_link=MAPS_LINK)

@app_handle.route("/remove_device/<int:guid>")
def remove_device_handle(guid: int):
    data = Device.query.get(guid)
    message = f"Device with ID \"{data.device_id}\" was removed successfully."

    db_handle.session.delete(data)
    db_handle.session.commit()

    log_handle.info(message)
    flash(message)
    return redirect(url_for("devices_handle"))

@app_handle.route("/update_device/<int:guid>", methods=["GET", "POST"])
def update_device_handle(guid: int):
    data = Device.query.get(guid)
    form = AddDevice(obj=data)

    if form.validate_on_submit():
        data.name = form.name.data
        message = f"Device with ID \"{data.device_id}\" was updated successfully."

        db_handle.session.commit()

        log_handle.info(message)
        flash(message)
        return redirect(url_for("devices_handle"))
    return render_template("update_device.html", form=form, device=data)
