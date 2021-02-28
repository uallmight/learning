from flask_sqlalchemy import SQLAlchemy

class HumanResourcesEmployeePayHistory(SQLAlchemy.Model):
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