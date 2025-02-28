import random

arms_upper_default = -0.4
arms_lower_default = -1.0
head_pitch_default = 0.0
head_yaw_default = 0.0
head_roll_default = 0.0


def listen():
    frames = []
    frames.append(
        {
            "time": 400,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": -0.17,
                "body.arms.right.upper.pitch": arms_upper_default,
                "body.arms.right.lower.roll": arms_lower_default,
            },
        }
    )
    return frames

def dont_listen():
    frames = []
    frames.append(
        {
            "time": 0,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": arms_upper_default,
                "body.arms.right.lower.roll": arms_lower_default,
            },
        }
    )
    return frames

def hi():
    frames = []
    frames.append(
        {
            "time": 0,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": arms_upper_default,
                "body.arms.right.lower.roll": arms_lower_default,
            },
        }
    )
    frames.append(
        {
            "time": 800,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": arms_lower_default,
            },
        }
    )
    frames.append(
        {
            "time": 1200,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": -0.4,
            },
        }
    )
    frames.append(
        {
            "time": 1600,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": -0.4,
            },
        }
    )
    frames.append(
        {
            "time": 2000,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": -1.2,
            },
        }
    )
    frames.append(
        {
            "time": 2400,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": arms_lower_default,
            },
        }
    )
    frames.append(
        {
            "time": 3200,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": arms_lower_default,
            },
        }
    )
    return frames


def nod(tag_positions):
    frames = []
    for tag in tag_positions:
        if tag["tag"] == "nod":
            tag_time = int((tag["start_position"] / 4) * 1000)
            frames.append(
                {
                    "time": tag_time,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 400,
                    "data": {
                        "body.head.pitch": -0.1,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 800,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
    return frames


def shake_head(tag_positions):
    frames = []
    for tag in tag_positions:
        if tag["tag"] == "shake":
            tag_time = int((tag["start_position"] / 4) * 1000)
            frames.append(
                {
                    "time": tag_time,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 400,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": 0.4,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 800,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": -0.4,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 1200,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )

    return frames


def arm_beat(tag_positions):
    frames = []
    for tag in tag_positions:
        if tag["tag"] == "beat_1" or tag["tag"] == "beat_2":
            tag_time = int((tag["start_position"] / 4.5) * 1000)
            frames.append(
                {
                    "time": tag_time,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 400,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": -0.7,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 800,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": -0.7,
                        "body.arms.right.lower.roll": -0.8,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 1200,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": -0.7,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 1600,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )

    return frames


def make_gestures(tag_positions=None):
    frames = []
    frames.extend(arm_beat(tag_positions))
    frames.extend(nod(tag_positions))
    frames.extend(shake_head(tag_positions))

    frames = sorted(frames, key=lambda frame: frame["time"])

    # if frames:
    #     naughty_frame = frames[0]
    #     if (
    #         naughty_frame["time"] < 0
    #     ):  # if we have a negative time at the start, we need to adjust all times
    #         for frame in frames:
    #             frame["time"] -= frames[0]["time"]
    # else:
    #     naughty_frame = None

    return frames
