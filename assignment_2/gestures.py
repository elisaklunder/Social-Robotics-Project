import random

arms_upper_default = -0.4
arms_lower_default = -1.0
head_pitch_default = 0.0
head_yaw_default = 0.0
head_roll_default = 0.0
body_torso_yaw_default = 0.0


def hi():
    step_size = 400
    big_step_size = 1000
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
                "body.arms.left.upper.pitch": arms_upper_default,
                "body.arms.left.lower.roll": arms_lower_default,
                "body.torso.yaw": body_torso_yaw_default
            },
        }
    )
    frames.append(
        {
            "time": big_step_size,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": arms_lower_default,
                "body.arms.left.upper.pitch": arms_upper_default,
                "body.arms.left.lower.roll": arms_lower_default,
                "body.torso.yaw": body_torso_yaw_default
            },
        }
    )
    frames.append(
        {
            "time": big_step_size + step_size,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": -0.4,
                "body.arms.left.upper.pitch": arms_upper_default,
                "body.arms.left.lower.roll": arms_lower_default,
                "body.torso.yaw": body_torso_yaw_default
            },
        }
    )
    frames.append(
        {
            "time": big_step_size + 2 * step_size,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": -1.2,
                "body.arms.left.upper.pitch": arms_upper_default,
                "body.arms.left.lower.roll": arms_lower_default,
                "body.torso.yaw": body_torso_yaw_default
            },
        }
    )
    frames.append(
        {
            "time": big_step_size + 3 * step_size,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": -0.4,
                "body.arms.left.upper.pitch": arms_upper_default,
                "body.arms.left.lower.roll": arms_lower_default,
                "body.torso.yaw": body_torso_yaw_default
            },
        }
    )
    frames.append(
        {
            "time": big_step_size + 4 * step_size,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": -2.0,
                "body.arms.right.lower.roll": arms_lower_default,
                "body.arms.left.upper.pitch": arms_upper_default,
                "body.arms.left.lower.roll": arms_lower_default,
                "body.torso.yaw": body_torso_yaw_default
            },
        }
    )
    frames.append(
        {
            "time": big_step_size + 5 * step_size + big_step_size,
            "data": {
                "body.head.pitch": head_pitch_default,
                "body.head.yaw": head_yaw_default,
                "body.head.roll": head_roll_default,
                "body.arms.right.upper.pitch": arms_upper_default,
                "body.arms.right.lower.roll": arms_lower_default,
                "body.arms.left.upper.pitch": arms_upper_default,
                "body.arms.left.lower.roll": arms_lower_default,
                "body.torso.yaw": body_torso_yaw_default
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
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
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
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
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
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
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
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
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
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
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
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
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
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
                    },
                }
            )

    return frames



def arm_gesture_1(tag_positions):
    frames=[]
    for tag in tag_positions:
        if tag["tag"] == "arms":
            tag_time = int((tag["syllable_position"] / 4) * 1000)
            frames.append(
                {
                    "time": tag_time - 1200,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time - 800,
                    "data": {
                        "body.arms.right.upper.pitch": -0.7,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
                        "body.head.roll": head_roll_default,
                        "body.torso.yaw": body_torso_yaw_default
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time - 400,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": -0.7,
                        "body.arms.right.lower.roll": -0.8,
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": -0.7,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 400,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default
                    },
                }
            )

    return frames

    """
    The possible gestures are:
•⁠  ⁠<nod>content</nod> (4 syllables) = a head nod to mean yes
•⁠  ⁠<shake>content</shake> (5 syllables) = a head shake to mean no
•⁠  ⁠<beat>content</beat> (7 syllables) = arm movements that mimicks typical human beat gestures
•⁠  ⁠<yippee>content</yippee> (10 syllables) = a full body celebration for something
•⁠  ⁠<confused>content</confused> (10 syllables) = a gesture for stratching your head in confused manner
    
    arms_upper_default = -0.4
    arms_lower_default = -1.0

    body_head_pitch_default = 0.0
    body_head_yaw_default = 0.0
    body_head_roll_default = 0.0

    body_torso_yaw_default = 0.0
    """
    
def arm_gesture_2(tag_positions):
    frames=[]
    #random torso movement
    random_torso= random.uniform(0.3, -0.3)
    # random upper hand
    random_upper_hand = random.uniform(-1.4, -1.2)
    # random lower hand
    random_lower_hand = random.uniform(-1.2, -0.8)
    for tag in tag_positions:
        if tag["tag"] == "beat_2":
            tag_time = int((tag["syllable_position"] / 4) * 1000)
            frames.append(
                {
                    "time": tag_time,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 1000,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": random_upper_hand,
                        "body.arms.right.lower.roll": random_lower_hand,
                        "body.arms.left.upper.pitch": random_upper_hand,
                        "body.arms.left.lower.roll": random_lower_hand,
                        "body.torso.yaw": random_torso,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 2000,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": arms_upper_default,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )

    return frames


def emotional_gesture(self):
    pass


def make_gestures(tag_positions=None):
    frames = []
    frames.extend(arm_gesture_1(tag_positions))
    frames.extend(arm_gesture_2(tag_positions))
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
