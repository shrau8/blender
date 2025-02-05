Blender Plugin (Blender add-on)

UI for object selection, transform controls, and API submission.
Listens to object transform changes and updates UI accordingly.
Sends data to FastAPI server.
FastAPI Server

Endpoints for handling transforms, file paths, and inventory management.
Simulates a 10-second delay and logs all requests.
Uses SQLite for persistent inventory storage.
SQLite Database

Stores inventory data.
Updates based on API requests.
PyQt/PySide UI

Displays inventory.
Allows adding/removing/updating items.
Runs smoothly without freezing.