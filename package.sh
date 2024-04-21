pkg_ver=`cat version`
echo $pkg_ver
sed -i "s/@@@version@@@/${MAGIC_VERSION}/g" setup.py
rm -rf dist
python3 setup.py sdist
python3 -m twine upload --repository baselib --verbose dist/*