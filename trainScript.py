import os

if __name__ == '__main__':
    dateset = "--dataset_path poem_dataset.pt "
    vocab = "--vocab_path models/google_zh_vocab.txt "
    model = "--output_model_path models/poem_gpt2_model.bin "
    config = "--config_path models/gpt2/config.json "
    world_size = "--world_size 0 "
    gpu = "--gpu_ranks 0 "
    step = "--total_steps 5000 "
    checkpoint = "--save_checkpoint_steps 1000 "
    report = "--report_steps 10 "
    learn_rate = "--learning_rate 1e-3 "
    batch = "--batch_size 32 "
    embedding = "--embedding word_pos --remove_embedding_layernorm "
    encoder = "--encoder transformer --mask causal --layernorm_positioning pre "
    target = "--target lm --tie_weight"
    assert os.getcwd() == 'D:\\GitHub\\UER-py'
    os.system("python pretrain.py "+dateset+vocab+model+config+world_size+step+checkpoint+report+learn_rate+batch+embedding+encoder+target)
