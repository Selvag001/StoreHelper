#run the following instruction in order

conda create -n "dev" python=3.8

conda activate dev

pip install -r requirement.txt

flask db init

flask db migrate -m "First commit"

flask db upgrade

flask run

