# Copyright (c) 2025, 🐚 17711 Smart Services <contact+public@17711.eu>
# Version 0.0.1
# Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0)

__auto_imports__ = [
    'cv2',
    'moviepy.VideoClip'
]



def get_zoom_factor_function(duration: float, max_zoom_multiplier: float):
    """
    """
    def zoom_factor_fn(t_relative: float):
        normalized_t = max(0.0, min(1.0, t_relative / duration))
        return 1.0 + normalized_t * (max_zoom_multiplier - 1.0)
    return zoom_factor_fn


def apply(input_source, **kwargs):
    """
    """
    video_clip = input_source

    effect_duration = float(kwargs.get("duration", video_clip.duration))
    max_zoom_factor = float(kwargs.get("max_zoom", 1.2))

    if effect_duration <= 0:
        raise ValueError("Duration must be > 0.")
    if max_zoom_factor < 1.0:
        raise ValueError("Factor must be >= 1.0.")

    zoom_fn = get_zoom_factor_function(effect_duration, max_zoom_factor)

    def make_zoomed_frame(t_absolute: float):
        frame = video_clip.get_frame(t_absolute)
        h, w = frame.shape[:2]
        z = zoom_fn(t_absolute)
        zh, zw = int(h * z), int(w * z)

        zoomed = cv2.resize(frame, (zw, zh), interpolation=cv2.INTER_LINEAR)

        x0 = (zw - w) // 2
        y0 = (zh - h) // 2
        return zoomed[y0:y0 + h, x0:x0 + w]

    zoomed_clip = VideoClip(make_frame=make_zoomed_frame, duration=video_clip.duration)
    zoomed_clip.fps = getattr(video_clip, 'fps', 24)

    return zoomed_clip

