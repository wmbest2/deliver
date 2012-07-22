import argparse

class FlagAction(argparse.Action):
    def __call__(self, parser, ns, values, option):
        setattr(ns, self.dest, True)
