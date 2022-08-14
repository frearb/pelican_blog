pelican content -o output -s publishconf.py

ghp-import output -b gh-pages

git push -f git@github.com:frearb/frearb.github.io.git gh-pages:master