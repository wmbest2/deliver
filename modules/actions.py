from abc import abstractmethod, ABCMeta
from argparse import Action, ArgumentParser

from yaml import load

class FlagAction(Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, True)

class SetDefaultFromFile(Action):
    """
    Populates arguments with file contents.

    This abstract class is to be inherited per type of file read.
    """

    def __call__(self, parser, namespace, values, option_string=None):
        print "HERHHERHRE"
        config = self._get_config_from_file(values)
        for key, value in config.items():
            setattr(namespace, key, value)

    def _get_config_from_file(self, filename):
        raise NotImplementedError


class SetDefaultFromYAMLFile(SetDefaultFromFile):
    """
    Populates arguments with a YAML file contents.
    """

    def _get_config_from_file(self, filename):
        print filename
        with open(filename) as f:
            config = load(f)
            print config
        return config

