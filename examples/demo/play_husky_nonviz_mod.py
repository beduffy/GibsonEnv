from gibson.envs.husky_env import HuskyNavigateEnvMod
from gibson.utils.play import play
import argparse
import os

config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'configs', 'play', 'play_husky_nonviz_mod'
                                                                                                 '.yaml')
print(config_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default=config_file)
    args = parser.parse_args()

    # import pdb;pdb.set_trace()
    env = HuskyNavigateEnvMod(config = args.config)
    print(env.config)
    env.reset()
    play(env, zoom=4)
