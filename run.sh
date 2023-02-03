rm -rf docs
make html
mv build/html docs
cp _config.yml docs