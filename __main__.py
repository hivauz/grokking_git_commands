from argparse import ArgumentParser

parser =ArgumentParser(prog = "hungry")
parser.add_argument('--user_id', type= int)
parser.add_argument('-e', '--email', type = str)
args = parser.parse_args()

print("these are the args  you just passed")
