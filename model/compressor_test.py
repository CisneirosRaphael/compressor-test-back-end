from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from typing import Union, List

from  model import Base


class CompressorTest(Base):
    __tablename__ = 'compressor_test'

    # Primary keys to uniquely identify a compressor test
    tag = Column("pk1_ct", String(140), primary_key=True)
    project = Column("pk2_ct",String(140), primary_key=True)

    model = Column(String(12))
    clearance_de = Column(Float)
    clearance_nde = Column(Float)
    unbalance_mass = Column(Float)
    oil_temperature = Column(Float)
    tag_de_x = Column(String(12))
    tag_de_y = Column(String(12))
    tag_nde_x = Column(String(12))
    tag_nde_y = Column(String(12))
    date_input = Column(DateTime, default=datetime.now())

    def __init__(self, tag:str, project:str, model:str, clearance_de:str,
                 clearance_nde:str, unbalance_mass:float, oil_temperature:float,
                 tag_de_x :str, tag_de_y :str, tag_nde_x:str, tag_nde_y:str,
                 date_input:Union[DateTime, None] = None):
        """
        Instantiate a CompressorTest object with information about a specific compressor test.

        Arguments:
            tag: str
                Machine Tag number
            project: str
                Name of the project
            model: str
                Compressor model
            clearance_de: float
                Diametral bearing clearance for the drive end side of the shaft (micrometers).
            clearance_nde: float
                Diametral bearing clearance for the non-drive end side of the shaft (micrometers).
            unbalance_mass: float
                Unbalance mass placed on the coupling before the test (in mm*g).
            oil_temperature: float
                Oil inlet temperature at the bearing (in °C).
            tag_de_x: str
                Drive end side radial probe Tag number for X-axis
            tag_de_y: str
                Drive end side radial probe Tag number for Y-axis
            tag_nde_x: float
                Non-drive end side radial probe Tag number for X-axis
            tag_nde_y: float
                Non-drive end side radial probe Tag number for Y-axis
            date_input: float
                Date when the test data was inserted into database.
        """

        self.tag = tag.upper()
        self.project = project.upper()
        self.model =  model.upper()
        self.clearance_de = clearance_de 
        self.clearance_nde = clearance_nde
        self.unbalance_mass = unbalance_mass
        self.oil_temperature = oil_temperature
        self.tag_de_x = tag_de_x.upper()
        self.tag_de_y = tag_de_y.upper()
        self.tag_nde_x = tag_nde_x.upper()
        self.tag_nde_y = tag_nde_y.upper()

        # If no date is provided, use the system's current date/time
        if date_input:
            self.date_input = date_input

