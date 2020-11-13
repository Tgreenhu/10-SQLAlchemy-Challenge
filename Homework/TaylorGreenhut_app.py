# Import necessary dependencies & libraries
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create engine
engine = create_engine("sqlite:///Hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create our flask app
app = Flask(__name__)

# Route 1
@app.route("/")
def welcome():
    return(
        f"Welcome To My Climate App!"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"

# Route 2
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    precip = session.query(measurement.date, measurement.prcp).\
        order_by(measurement.date).all()
    session.close()
    total = []
    for number in precip:
        data = {}
        row['date'] = precip[0]
        row['prcp'] = precip[1]
        total.append(data)
    return jsonify(total)

# Route 3
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station = session.query(stations.station).all()
    session.close()
    all_stations = list(np.ravel(station))
    return jsonify(all_stations)

# Route 4
@app.route("/api/v1.0/tobs")
def tbs():
    session = Session(engine)
    previous_year = dt.date(2017, 8, 23) - dt.datetimedelta(days=365)
    data = session.query(measurement.tobs)\
            .filter(measurement.station == 'USC00519281')\
            .filter(measurement.date >= previous_year).all()
    session.close()
    data_list = list(np.ravel(data))
    return jsonify(data_list)

# Route 5
@app.route("/api/v1.0/<start>")
def start():

# Route 6
@app.route("/api/v1.0/<start>/<end>")
def startend():

if __name__ == "__main__":
    app.run()