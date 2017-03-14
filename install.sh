#!/bin/bash

mkdir -p "/home/$USER/.local/bin"

rm -rf "/home/$USER/.local/bin/sc-tools"
cp -r . "/home/$USER/.local/bin/sc-tools"
rm -f "/home/$USER/.local/bin/sc-compile"
rm -f "/home/$USER/.local/bin/sc-push"
rm -f "/home/$USER/.local/bin/sc-test"

ln -s "/home/$USER/.local/bin/sc-tools/sc-compile" "/home/$USER/.local/bin/sc-compile"
ln -s "/home/$USER/.local/bin/sc-tools/sc-push" "/home/$USER/.local/bin/sc-push"
ln -s "/home/$USER/.local/bin/sc-tools/sc-test" "/home/$USER/.local/bin/sc-test"
