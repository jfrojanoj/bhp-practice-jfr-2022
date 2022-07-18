echo "################## RUNING BLACK ##################"
black bhp/

echo "################## RUNING flake8 ##################"
flake8 bhp/


echo "################## RUNING mypy ##################"
mypy bhp/