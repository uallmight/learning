import urllib
from flask import Flask, json, jsonify, request
import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import sqltypes
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=AdventureWorks2019;Trusted_Connection=yes;")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc:///?odbc_connect={params}'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class HumanResourcesEmployeePayHistory(db.Model):
    """
    Data model used to bind schema to HumanResources.EmployeePayHistory
    data.
    """

    __tablename__ = 'EmployeePayHistory'

    __table_args__ = {
        "schema":"HumanResources",
        # "primarykey": PrimaryKeyConstraint('BusinessEntityID', 'RateChangeDate')
    }

    business_entity_id = db.Column(
        'BusinessEntityID', type_=sqltypes.INT, nullable=False, primary_key=True)
    rate_change_date = db.Column(
        'RateChangeDate', type_=sqltypes.DATETIME, nullable=False, primary_key=True)
    rate = db.Column('Rate', type_=sqltypes.REAL, nullable=False)
    pay_frequency = db.Column(
        'PayFrequency', type_=sqltypes.SMALLINT, nullable=False)
    modified_date = db.Column(
        'ModifiedDate', type_=sqltypes.DATETIME, nullable=False)

    def __init__(self, business_entity_id, rate_change_date, rate, pay_frequency, modified_date) -> None:
        super().__init__()
        self.business_entity_id = business_entity_id
        self.rate_change_date = rate_change_date
        self.rate = rate
        self.pay_frequency = pay_frequency
        self.modified_date = modified_date

    @property
    def serialized(self):
        """
            Returns self object as a json serializable format
        """
        return {
            'BusinessEntityID': self.business_entity_id,
            'RateChangeDate': self.rate_change_date,
            'PayFrequency': self.pay_frequency,
            'ModifiedDate': self.modified_date,
        }

class HumanResourcesEmployeePayHistorySchema(ma.Schema):
    class Meta:
        fields = ('BusinessEntityID','RateChangeDate','PayFrequency','ModifiedDate')
        model = HumanResourcesEmployeePayHistory

history_shema = HumanResourcesEmployeePayHistorySchema()
histories_schema = HumanResourcesEmployeePayHistorySchema(many=True)

class HistoryListResource(Resource):
    def get(self):
        histories = HumanResourcesEmployeePayHistory.query.all()
        histories_serializable = [history.serialized for history in histories]

        return histories_schema.jsonify(histories_serializable)

api.add_resource(HistoryListResource, '/history')

@app.route('/')
def defaut_handler():
    return jsonify({'statusCode': 200, 'message': 'ok'})

def main():
    app.run('127.0.0.1', port=3939)


if __name__ == '__main__':
    main()
