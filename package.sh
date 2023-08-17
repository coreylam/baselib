rm -rf dist
python3 setup.py sdist
twine upload --username ${PROJ_USER} --password ${PROJ_PWD}   --verbose dist/*