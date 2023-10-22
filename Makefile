test:
	python3 -m pytest

build: test
	python3 -m build

clean:
	rm -rf clamg.egg* dist
