import argparse, os
import torch
parser = argparse.ArgumentParser(description='Run experiments on a dataset')
parser.add_argument('--dataset', type=str, required=True)
parser.add_argument("--data_dir", type=str, required=True)
parser.add_argument("--output_dir", type=str)
parser.add_argument('--encoder', type=str, choices=['cnn', 'lstm', 'average', 'all'], required=True)
parser.add_argument('--attention', type=str, choices=['tanh', 'dot', 'all'], required=True)
parser.add_argument("--gpu", type=str, default='2')
parser.add_argument("--layers", type=int, default=1, help='decoder layers')
parser.add_argument("--e_layers", type=int, default=0, help='encoder layers')

args, extras = parser.parse_known_args()
args.extras = extras

os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu

from Transparency.Trainers.DatasetBC import *
from Transparency.ExperimentsBC import *

dataset = datasets[args.dataset](args)

if args.output_dir is not None :
    dataset.output_dir = args.output_dir
dataset.display_stats()

encoders = ['cnn', 'lstm', 'average'] if args.encoder == 'all' else [args.encoder]

print(args)


if args.attention in ['tanh', 'all'] :
    train_dataset_on_encoders(dataset, encoders)

if args.attention in ['dot', 'all'] :
    encoders = [e + '_dot' for e in encoders]
    print(encoders)
    train_dataset_on_encoders(dataset, encoders)



