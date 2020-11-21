# Import necessary dependencies & libraries
import datetime as dt
import time
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create engine
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table & start session
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Create our flask app
app = Flask(__name__)

# Route 1
@app.route("/")
def welcome():
    return(
        f"Welcome To My Climate App!<b/r>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>")

# Route 2
@app.route("/api/v1.0/precipitation")
def precipitation():
    most_recent_date = session.query(Measurement.date)\
        .order_by(Measurement.date.desc()).first()[0]
    year_ago = (dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365))\
        .strftime('%Y-%m-%d')
    precip_data = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date >= year_ago).all()
    all_prcp = list(np.ravel(precip_data))
    return jsonify(all_prcp)

# Route 3
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

# Route 4
@app.route("/api/v1.0/tobs")
def tobs():
    previous_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    data = session.query(Measurement.tobs)\
            .filter(Measurement.station == 'USC00519281')\
            .filter(Measurement.date >= previous_year).all()
    data_list = list(np.ravel(data))
    return jsonify(data_list)

# Route 5
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def info():
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        data2 = session.query(*sel).filter(Measurement.date >= start).all()
        temp_data = list(np.ravel(data2))
    data3 = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    temp_data2 = list(np.ravel(data3))

# Close our session
session.close()

# Run app
if __name__ == "__main__":
    app.run()