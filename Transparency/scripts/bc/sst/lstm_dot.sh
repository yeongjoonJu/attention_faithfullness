dataset_name=sst
output_path=./outputs
encoder_type=lstm
attention_type=dot
python train_and_run_experiments_bc.py --dataset ${dataset_name} --data_dir . --output_dir ${output_path} --attention ${attention_type} --encoder ${encoder_type}