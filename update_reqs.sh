#!/usr/bin/env bash

ROOT=`dirname $0`
pip install pipreqs
pipreqs --force ${ROOT}
