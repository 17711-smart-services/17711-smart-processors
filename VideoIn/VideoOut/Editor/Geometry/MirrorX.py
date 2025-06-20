# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu) 
# Version 0.0.1 
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'random',
    'moviepy.video.fx.MirrorX.MirrorX'
]


def apply(input_source, **kwargs):
    """
    Apply a Mirror X effect on the provided input. 
    """
    output = input_source.with_effects([MirrorX()])
    return output


