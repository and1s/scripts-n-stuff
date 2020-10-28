#!/bin/bash

#my first script

echo "testing"
ssh -t spiridea@atom.mit.edu -p2866 'cd data1;echo "yes"; bash -l'
echo "nope"