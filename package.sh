pkg_ver=`cat version`
echo $pkg_ver
sed -i '' "s/@@@version@@@/${pkg_ver}/g" setup.py
rm -rf dist
python3 setup.py sdist
python3 -m twine upload --repository baselib --verbose dist/*
