#!/bin/bash
# rm -rf path/to/venv

# echo "🍺 Adding or updating Robin-Stocks as a submodule..."
# if [ -d "robin_stocks" ]; then
#     echo "🍺 Robin-Stocks submodule already exists. Pulling latest changes..."
#     git -C robin_stocks pull origin master
# else
#     echo "🍺 Cloning Robin-Stocks as a submodule..."
#     git submodule add https://github.com/jmfernandes/robin_stocks.git robin_stocks
#     git submodule update --init --recursive
# fi

# echo "🍺 Installing Robin-Stocks in editable mode..."
# pip install -e robin_stocks


python3 -m venv path/to/venv                                                                     ─╯
source path/to/venv/bin/activate  # Unix/macOS
pip3 install -r requirements.txt
python3 login-test.py