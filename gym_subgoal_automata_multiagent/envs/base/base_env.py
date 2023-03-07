from abc import ABC, abstractmethod
import gym
from gym_subgoal_automata_multiagent.utils import utils


class BaseEnv(ABC, gym.Env):
    RANDOM_SEED_FIELD = "environment_seed"
    NUM_AGENTS = "num_agents"

    def __init__(self, params=None):
        super().__init__()

        self.params = params
        self.num_agents = int(utils.get_param(self.params, BaseEnv.NUM_AGENTS))
        self.is_game_over = [False]*self.num_agents
        self.seed = utils.get_param(self.params, BaseEnv.RANDOM_SEED_FIELD)

    @abstractmethod
    def step(self, action):
        pass

    @abstractmethod
    def is_terminal(self):
        pass

    @abstractmethod
    def get_observables(self):
        pass

    @abstractmethod
    def get_restricted_observables(self):
        pass

    @abstractmethod
    def get_observations(self):
        pass

    @abstractmethod
    def get_automaton(self):
        pass

    @abstractmethod
    def reset(self):
        self.is_game_over = [False]*self.num_agents
        return None

    @abstractmethod
    def render(self, mode='human'):
        pass

    @abstractmethod
    def play(self):
        pass
