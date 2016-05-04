# Copyright (c) 2016. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .regression_target import MAX_IC50

N_EPOCHS = 250
ACTIVATION = "tanh"
INITIALIZATION_METHOD = "lecun_uniform"
EMBEDDING_DIM = 32
HIDDEN_LAYER_SIZE = 100
DROPOUT_PROBABILITY = 0.1
LEARNING_RATE = 0.001
OPTIMIZER = "adam"
LOSS = "mse"

def add_hyperparameter_arguments_to_parser(parser):
    """
    Extend an argument parser with the following options:
        --training-epochs
        --activation
        --initialization
        --embedding-size
        --hidden-layer-size
        --dropout
        --max-ic50
        --random-negative-samples
        --imputation-method
        --learning-rate
    """
    parser.add_argument(
        "--training-epochs",
        type=int,
        default=N_EPOCHS,
        help="Number of training epochs. Default: %(default)s")

    parser.add_argument(
        "--initialization",
        default=INITIALIZATION_METHOD,
        help="Initialization for neural network weights Default: %(default)s")

    parser.add_argument(
        "--activation",
        default=ACTIVATION,
        help="Activation function for neural network layers. "
        "Default: %(default)s")

    parser.add_argument(
        "--embedding-size",
        type=int,
        default=EMBEDDING_DIM,
        help="Size of vector representations for embedding amino acids. "
        "Default: %(default)s")

    parser.add_argument(
        "--hidden-layer-size",
        type=int,
        default=HIDDEN_LAYER_SIZE,
        help="Size of hidden neural network layer. Default: %(default)s")

    parser.add_argument(
        "--dropout",
        type=float,
        default=DROPOUT_PROBABILITY,
        help="Dropout probability after neural network layers. "
        "Default: %(default)s")

    parser.add_argument(
        "--max-ic50",
        type=float,
        default=MAX_IC50,
        help="Largest IC50 represented by neural network output. "
        "Default: %(default)s")

    parser.add_argument(
        "--learning-rate",
        type=float,
        default=0.001,
        help="Learning rate for training neural network. Default: %(default)s")

    parser.add_argument(
        "--random-negative-samples",
        type=int,
        default=0,
        help="Number of random negtive samples to generate each training epoch")

    parser.add_argument(
        "--imputation-method",
        default="none",
        choices=("mice", "knn", "softimpute", "svd", "mean", "none"),
        type=lambda s: s.strip().lower(),
        help="Use the given imputation method to generate data for pre-training models")

    return parser