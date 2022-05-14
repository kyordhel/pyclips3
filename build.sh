#!/usr/bin/env bash

cat > .test.h <<'EOM'
#include <Python.h>
EOM
if ! gcc -E .test.h &> /dev/null; then
	echo -en "\033[33mWarning:\033[0m Python.h not found. "
	echo "CLIPS may not build"
fi
echo -e "\033[0m"

python3 setup.py build
