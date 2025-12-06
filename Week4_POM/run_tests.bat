@echo off
echo Activating virtual environment...
call env\Scripts\activate

echo Running tests...
pytest -q

echo Done.
pause
