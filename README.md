# API - Compressor Test

The **Compressor Test** application is designed to create and manage a database of compressor tests for oil and gas applications. In most industrial projects there are many centrifugal compressors, each undergoing some validation steps during fabrication process. One critical step is the **Unbalance Response Test** which validates the compressor rotordynamic behaviour and whether it is according to what has been designed. 

The application allow users to sabe key test parameters to an SQlite database, utilizing the SQLAlchemy library for database interactions. Eeach test is uniquely identified in the database by a composite primary key which consists of **"TAG"** and **"Project"**. The TAG number of the compressor represents its service but it may be reused across similar projects. Therefore, including the Project name is essential to uniquely identify and store test data within the database.


## How to run the application

It is recommended to set up a dedicated virtual environment to run the application.  If you are using Conda to create a virtual environment, refer to the link: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html.


### Step 1: Install Dependencies

After creating the virtual environment, install all required libraries listed in the requirements.txt file.
Navigate to the folder containing the `requirements.txt` file and execute the following command:

```
(env)$ pip install -r requirements.txt
```

### Step 2: Run the API

To start the API, use the following command:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

#### Optional: Development Mode
For development purposes, it is recommended to use the --reload flag. This allows the server to automatically restart whenever changes are made to the code:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

### Step 3: Verify API Execution
Open http://localhost:5000/#/ in your browser to confirm the API is running successfully.