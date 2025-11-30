from pydantic import BaseModel, field_validator, Field
from typing import Optional, List, Dict, Any
from model.compressor_test import CompressorTest



class CompressorTestSchema(BaseModel):
    """
    Defines the structure for inserting new compressor test data.
    """
    tag: str = "C-UC-1231001A" # Machine Tag number
    project: str = "P-88" # Project name
    model: str = "BCL-406" # Compressor model
    clearance_de: float = 110 # Diametral bearing clearance for drive end side (in micrometers)
    clearance_nde: float = 130 # Diametral bearing clearance for non-drive end side (in micrometers)
    unbalance_mass: float = 473.4 # Unbalance mass for the test (in mm*g)
    oil_temperature: float = 50.0 # Oil inlet temperature (in °C)
    tag_de_x : str = "VXT-1231800A" # Drive end radial probe Tag number for X-axis
    tag_de_y : str = "VYT-1231800A" # Drive end radial probe Tag number for Y-axis
    tag_nde_x : str = "VXT-1231900A" # Non-drive end radial probe Tag number for X-axis
    tag_nde_y : str = "VYT-1231900A" # Non-drive end radial probe Tag number for Y-axis
    country : str = "Germany" # Country where the manufacturer test bench is located.

class CompressorTestUpdateSchema(BaseModel):
    """
    Defines how the compressor test update data should be represented.
    """
    model: Optional[str] = Field(default="", description="Compressor model")
    clearance_de: Optional[float] = Field(default="", description="DE clearance value")
    clearance_nde: Optional[float] = Field(default="", description="NDE clearance value")
    unbalance_mass: Optional[float] = Field(default="", description="Unbalance mass")
    oil_temperature: Optional[float] = Field(default="", description="Oil temperature")
    tag_de_x : Optional[str] = Field(default="", description="DE X tag value")
    tag_de_y : Optional[str] = Field(default="", description="DE Y tag value")
    tag_nde_x : Optional[str] = Field(default="", description="NDE X tag value")
    tag_nde_y : Optional[str] = Field(default="", description="NDE Y tag value")
    country : Optional[str] = Field(default="", description="Country")

    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == '' or v == 'null' or v is None:
            return None
        return v
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        # Override model_dump method to exclude None values
        return super().model_dump(exclude_none=True, **kwargs)

class CompressorTestSearchSchema(BaseModel):
    """ 
    Defines the structure for searching compressor tests based on 
    Tag number and Project name.       
    """
    tag: str = "C-UC-1231001A"
    project: str = "P-88"


class ListCompressorsTestsSchema(BaseModel):
    """ 
    Defines the structure for returning a list of compressor tests.
    """
    CompressorTest:List[CompressorTestSchema]


def show_compressors_tests(compressor_test: List[CompressorTest]):
    """ 
    Returns a structured representation of compressor test data 
    based on the CompressorTestViewSchema definition.
    """
    result = []
    for test in compressor_test:
        result.append({
            "tag": test.tag,
            "project": test.project,
            "model": test.model,
            "clearance_de": test.clearance_de,
            "clearance_nde": test.clearance_nde,
            "unbalance_mass": test.unbalance_mass,
            "oil_temperature": test.oil_temperature,
            "tag_de_x": test.tag_de_x,
            "tag_de_y": test.tag_de_y,
            "tag_nde_x": test.tag_nde_x,
            "tag_nde_y": test.tag_nde_y,
            "country": test.country,
        })

    return {"CompressorsTests": result}


class CompressorTestViewSchema(BaseModel):
    """ 
    Defines the structure for returning a compressor test from the database.
    """
    
    tag: str = "VXE-1231800"
    project: str = "P-88"
    model: str = "BCL-404"
    clearance_de: float = 110
    clearance_nde: float = 130
    unbalance_mass: float = 473.4
    oil_temperature: float = 50.0
    tag_de_x : Optional[float] = "VXE-1231800"
    tag_de_y : Optional[float] = "VYE-1231800"
    tag_nde_x : Optional[float] = "VXE-1231900"
    tag_nde_y : Optional[float] = "VYE-1231900"
    country: Optional[str] = "Germany"


class CompressorTestDelSchema(BaseModel):
    """ Defines the structure to show the data after a deletion request.
    """

    tag: str # Machine Tag number
    project: str # Project name

def show_compressor_test(compressor_test: CompressorTest):
    """ Returns a structured representation of a compressor test based on 
        CompressorTestViewSchema definition.
    """
    return {
        "tag": compressor_test.tag,
        "project": compressor_test.project,
        "model": compressor_test.model,
        "clearance_de": compressor_test.clearance_de,
        "clearance_nde": compressor_test.clearance_nde,
        "unbalance_mass": compressor_test.unbalance_mass,
        "oil_temperature": compressor_test.oil_temperature,
        "tag_de_x" : compressor_test.tag_de_x,
        "tag_de_y" : compressor_test.tag_de_y,
        "tag_nde_x" : compressor_test.tag_nde_x,
        "tag_nde_y" : compressor_test.tag_nde_y,
        "country" : compressor_test.country,
    }
