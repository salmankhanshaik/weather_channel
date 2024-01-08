# -------------------------------- fastapi imports -----------------------------
from  main               import app
from fastapi.testclient  import TestClient

# initializing the client to start the each app level testing
client              =   TestClient(app)