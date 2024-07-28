echo "Starting Build..."

echo "# Master dotenv file" > $PWD/bin/.env
echo "F1HOME=$PWD" >> $PWD/bin/.env
chmod 660 $PWD/bin/.env

if [ -d "venv" ]; then
    echo "Virtual environment directory exists. Removing it..."
    rm -rf "./venv"
fi

echo "Creating virtual environment"
python3 -m venv $PWD/venv
chmod 660 $PWD/venv

echo "Configuring pip"
source $PWD/venv/bin/activate
pip install --upgrade pip

echo "Installing required packages"
pip3 --default-timeout=1000 install -r $PWD/requirements.txt

echo "Installing custom package"
pip install -e f1_model

# Pytest and coverage report
export PYTHONPATH=$PWD/f1_model
coverage run --source f1_model --omit */setup.py -m pytest
coverage report -m

echo "Removing PyTest sample CSV file from data directory"
rm -rf $PWD/data/top_3_drivers.csv
echo "Build complete"
