# Pypi

1. pypi 계정 만들기
2. prepare `setup.py`
3. 기존에 있던 빌드 관련된 폴더들은 지우고 새로 하는 것이 좋음.
4. version.py update 확인하기.
5. build
   1. `pip install setuptools wheel`
   2. `python setup.py sdist bdist_wheel`
6. upload to pypi
   1. `pip install twine`
   2. `twine upload dist/*`
7. tagging

   ```
   git tag -a v0.1.6 -m "annotation for this release"
   git push origin --tags
   ```
