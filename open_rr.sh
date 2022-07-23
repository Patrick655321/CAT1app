#!/bin/bash
if [ $# -eq 1 ] && [ $1 == "help" ]; then
 help.md; else
python3 ./roster_right.py
fi