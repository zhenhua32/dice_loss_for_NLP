import os
from dotenv import load_dotenv

env_file = os.path.join(os.path.dirname(__file__), ".env")
result = load_dotenv(env_file, verbose=True)
print("load env", result)

print(os.environ["LOSS_SIGN"])
os.makedirs(os.environ["OUTPUT_DIR"], exist_ok=True)

cmd = f"""
python "D:\\code\\github\\dice_loss_for_NLP\\tasks\\mrc_ner\\train.py" \
--gpus=1 \
--precision={os.environ["precision"]} \
--train_batch_size {os.environ["TRAIN_BATCH_SIZE"]} \
--eval_batch_size {os.environ["EVAL_BATCH_SIZE"]} \
--progress_bar_refresh_rate {os.environ["PROGRESS_BAR"]} \
--val_check_interval {os.environ["VAL_CHECK_INTERVAL"]} \
--max_length {os.environ["MAX_LENGTH"]} \
--optimizer {os.environ["OPTIMIZER"]} \
--data_dir {os.environ["DATA_DIR"]} \
--bert_hidden_dropout {os.environ["BERT_DROPOUT"]} \
--bert_config_dir {os.environ["BERT_DIR"]} \
--lr {os.environ["LR"]} \
--lr_scheduler {os.environ["LR_SCHEDULE"]} \
--accumulate_grad_batches {os.environ["ACC_GRAD"]} \
--default_root_dir {os.environ["OUTPUT_DIR"]} \
--output_dir {os.environ["OUTPUT_DIR"]} \
--max_epochs {os.environ["MAX_EPOCH"]} \
--gradient_clip_val {os.environ["GRAD_CLIP"]} \
--weight_decay {os.environ["WEIGHT_DECAY"]} \
--loss_type {os.environ["LOSS_TYPE"]} \
--weight_start {os.environ["W_START"]} \
--weight_end {os.environ["W_END"]} \
--weight_span {os.environ["W_SPAN"]} \
--dice_smooth {os.environ["DICE_SMOOTH"]} \
--dice_ohem {os.environ["DICE_OHEM"]} \
--dice_alpha {os.environ["DICE_ALPHA"]} \
--dice_square \
--warmup_proportion {os.environ["WARMUP_PROPORTION"]} \
--span_loss_candidates gold_pred_random \
--construct_entity_span start_and_end \
--num_labels 1 \
--flat_ner \
--is_chinese \
--pred_answerable "train_infer" \
--answerable_task_ratio 0.3 \
--activate_func relu \
--data_sign zh_msra
""".strip()

print(cmd)

os.system(cmd)

"""
输出结果为
DATALOADER:0 TEST RESULTS
{'test_span_f1': tensor(0.9463, device='cuda:0'),
 'test_span_precision': tensor(0.9454, device='cuda:0'),
 'test_span_recall': tensor(0.9472, device='cuda:0')}
"""
