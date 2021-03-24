#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# author: xiaoya li
# file: eval_pred_file.sh
# first create: 2021.01.05


REPO_PATH=/userhome/xiaoya/mrc-with-dice-loss
export PYTHONPATH="$PYTHONPATH:$REPO_PATH"

DATA_DIR=$1
OUTPUT_DIR=$2
DATA_FILE=${DATA_DIR}/dev-v1.1.json

python3 ${REPO_PATH}/tasks/squad/evaluate_predictions.py ${DATA_FILE} ${OUTPUT_DIR}
