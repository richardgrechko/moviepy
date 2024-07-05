from moviepy.decorators import apply_to_mask,apply_to_audio


def speedx(clip, factor=None, final_duration=None, keep_pitch=False):
    """
    Returns a clip playing the current clip but at a speed multiplied
    by ``factor``. Instead of factor, one can indicate the desired
    ``final_duration`` of the clip, and the factor will be automatically
    computed. If ``keep_pitch`` is True, the pitch will reset to 0.
    The same effect is applied to the clip's audio and mask if any.
    """
    
    if final_duration:
        factor = 1.0 * clip.duration / final_duration
        
    newclip = clip.fl_time(lambda t: factor * t, apply_to=[apply_to_mask, apply_to_audio])
    
    if clip.duration is not None:
        newclip = newclip.set_duration(1.0 * clip.duration / factor)

    if keep_pitch:
        sr = clip.audio.fps
        new_sr = newclip.audio.fps
        pitch_change = int(np.round(12 * np.log2(new_sr / sr)))
        newclip.audio = newclip.audio.fx(pitch, pitch_change)
    
    return newclip
