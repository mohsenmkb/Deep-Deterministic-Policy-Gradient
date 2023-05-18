import gym
import matplotlib.pyplot as plt


env = gym.make("BipedalWalker-v3", hardcore=True,render_mode="human")

env.reset()


while True:
    x = env.render()
    next_state, reward, done, _, info =  env.step(env.action_space.sample())
    if done:
        break