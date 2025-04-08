from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model import Session, CompressorTest
from logger import logger
from schemas import *
from flask_cors import CORS

# API data
info = Info(title="API - Compressor Test", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Define tags for API endpoints
home_tag = Tag(name="Documentation", description="Select documentation type")
compressor_test_tag = Tag(name="CompressorTest", description="Add, delete and visualize compressor test to the database")

@app.get('/', tags=[home_tag])
def home():
    """ Redirect to /openapi, the screen which allows to choose the documentation type.
    """
    return redirect('/openapi')

@app.post('/compressor_test', tags=[compressor_test_tag],
          responses={"200": CompressorTestViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_compressor_test(form: CompressorTestSchema):
    """
    Add new Compressor Test to the database 

    Returns:
      Representation of the compressor test data.
    """
    compressor_test = CompressorTest(
        tag = form.tag,
        project = form.project,
        model = form.model,
        clearance_de = form.clearance_de,
        clearance_nde = form.clearance_nde,
        unbalance_mass = form.unbalance_mass,
        oil_temperature = form.oil_temperature,
        tag_de_x = form.tag_de_x,
        tag_de_y = form.tag_de_y,
        tag_nde_x = form.tag_nde_x,
        tag_nde_y = form.tag_nde_y
        )
    logger.debug(f"Adding compressor test with Tag: '{compressor_test.tag}' \
                 for project '{compressor_test.project}'")
    try:
        # connect to the base
        session = Session()
        # add the new compressor test to the database
        session.add(compressor_test)
        session.commit()

        logger.debug(f"Added compressor test with Tag number '{compressor_test.tag}' \
                 for project '{compressor_test.project}'")
        return show_compressor_test(compressor_test), 200

    except IntegrityError as e:
        # handle duplicate entries (IntegrityError)
        error_msg = "Compressor Tag number for this Project already exists in the database."
        logger.warning(f"Failed to add compressor test with Tag number '{compressor_test.tag}' \
                       for project '{compressor_test.project}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # Handle unexpected errors
        error_msg = "It was not possible to save this item to the database."
        logger.warning(f"Failed to add compressor test with Tag number '{compressor_test.tag}' \
                       for project '{compressor_test.project}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/compressors_tests', tags=[compressor_test_tag],
         responses={"200": ListCompressorsTestsSchema, "404": ErrorSchema, "500": ErrorSchema})
def get_compressors_tests():
    """ 
    Retrieve all compressors tests stored in the database.

    Returns:
        List of compressors tests.
    """
    logger.debug(f"Retrieving compressors tests from the database")

    # Connect to the database
    session = Session()
    # Query all compressors tests
    compressors_tests = session.query(CompressorTest).all()

    if not compressors_tests:
        logger.debug("No compressor test found in the database.")
        return {"compressor tests": []}, 200
    else:
        logger.debug(f"Found {len(compressors_tests)} compressors tests in the database")
        # Return a representation of the compressors tests
        return show_compressors_tests(compressors_tests), 200


@app.get('/compressor_test', tags=[compressor_test_tag],
         responses={"200": CompressorTestViewSchema, "404": ErrorSchema})
def get_compressor_test(query: CompressorTestSearchSchema): 
    """ 
    Search for a specific compressor test based on its Tag and project name.

    Returns: 
        Representation of the found compressor test.
    """
    
    compressor_test_tag = query.tag
    compressor_test_project = query.project
    
    logger.debug(f"Searching for compressor Tag number '{compressor_test_tag}' \
                 and project '{compressor_test_project}'")
    
    # Connect to the database
    session = Session()
    # Do the search
    compressor_test = session.query(CompressorTest).filter( 
        CompressorTest.tag == compressor_test_tag, 
        CompressorTest.project == compressor_test_project).first()

    if not compressor_test:
        error_msg = "Compressor test not found in the database."
        logger.warning(f"Failed to find the compressor test for Tag number '{compressor_test_tag}' \
                       and project '{compressor_test_project}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Compressor test found: Tag number '{compressor_test_tag}' \
                     and project '{compressor_test_project}'")
        # Return a representation of the compressor test
        return show_compressor_test(compressor_test), 200
        

@app.delete('/compressor_test', tags=[compressor_test_tag],
            responses={"200": CompressorTestDelSchema, "404": ErrorSchema})
def del_compressor_test(query: CompressorTestSearchSchema):
    """
    Delete a Compressor test based on its Tag number and project.

    Returns:
        Confirmation of deletion or errro message.
    """
    compressor_test_tag = unquote(unquote(query.tag))
    compressor_test_project = unquote(unquote(query.project))

    logger.debug(f"Deleting compressor test with Tag number '{compressor_test_tag}' \
                 and project '{compressor_test_project}'")
    
    # Connect to the database
    session = Session()
    # Delete compressor test
    count = session.query(CompressorTest).filter( 
        CompressorTest.tag == compressor_test_tag, 
        CompressorTest.project == compressor_test_project).delete()
    session.commit()

    if count:
        logger.debug(f"Compressor test deleted: TAG number '{compressor_test_tag}' \
                       and project '{compressor_test_project}'")
        return {"message": "Compressor Test Deleted", "Tag": compressor_test_tag, \
                "Project": compressor_test_project}
    else:
        error_msg = "Compressor test not found in the database."
        logger.warning(f"Failed to delete compressor test with Tag number '{compressor_test_tag}' \
                       and project '{compressor_test_project}', {error_msg}")
        return {"message": error_msg}, 404
    


    