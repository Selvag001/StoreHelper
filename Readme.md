## Pre-req
** conda
** git

## run the following instruction in order

git clone https://github.com/Selvag001/StoreHelper.git

cd StoreHelper

conda create -n "dev" python=3.8

conda activate dev

pip install -r requirement.txt

flask db init

flask db migrate -m "First commit"

flask db upgrade

flask run

## Note
Sample data file is available in StoreHelper/data.csv
