import random
from typing import Dict, List, Optional, Union

arms_upper_default = -0.4
arms_lower_default = -1.0
head_pitch_default = 0.0
head_yaw_default = 0.0
head_roll_default = 0.0
body_torso_yaw_default = 0.0


def get_tag_time(start_position: int) -> int:
    """Calculate the time marker (in milliseconds) for a gesture tag based on its starting position.

    Args:
        start_position (int): The starting position of the gesture tag in the sequence (1-based index)

    Returns:
        int: The calculated time in milliseconds for when the gesture tag should occur
    """
    return int(((start_position - 1) / 4) * 1000)


def hi() -> List[Dict[str, Union[int, Dict[str, float]]]]:
    """Generate frames for a waving gesture animation.

    Returns:
        List[Dict[str, Union[int, Dict[str, float]]]]: List of animation frames with timing and joint positions
    """
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
                "body.torso.yaw": body_torso_yaw_default,
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
                "body.torso.yaw": body_torso_yaw_default,
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
                "body.torso.yaw": body_torso_yaw_default,
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
                "body.torso.yaw": body_torso_yaw_default,
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
                "body.torso.yaw": body_torso_yaw_default,
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
                "body.torso.yaw": body_torso_yaw_default,
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
                "body.torso.yaw": body_torso_yaw_default,
            },
        }
    )
    return frames


def nod(
    tag_positions: List[Dict[str, Union[str, int]]],
) -> List[Dict[str, Union[int, Dict[str, float]]]]:
    """Generate frames for nodding head gestures at specified positions.

    Args:
        tag_positions (List[Dict[str, Union[str, int]]]): List of dictionaries containing tag type and position information

    Returns:
        List[Dict[str, Union[int, Dict[str, float]]]]: List of animation frames for the nodding gestures
    """
    frames = []
    for tag in tag_positions:
        if tag["tag"] == "nod":
            tag_time = get_tag_time(tag["start_position"])
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
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 200,
                    "data": {
                        "body.head.pitch": -0.1,
                        "body.head.yaw": head_yaw_default,
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
                    "time": tag_time + 450,
                    "data": {
                        "body.head.pitch": 0.17,
                        "body.head.yaw": head_yaw_default,
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
                    "time": tag_time + 650,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
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


def shake_head(
    tag_positions: List[Dict[str, Union[str, int]]],
) -> List[Dict[str, Union[int, Dict[str, float]]]]:
    """Generate frames for head shaking gestures at specified positions.

    Args:
        tag_positions (List[Dict[str, Union[str, int]]]): List of dictionaries containing tag type and position information

    Returns:
        List[Dict[str, Union[int, Dict[str, float]]]]: List of animation frames for the head shaking gestures
    """
    frames = []
    for tag in tag_positions:
        if tag["tag"] == "shake":
            tag_time = get_tag_time(tag["start_position"])
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
                        "body.torso.yaw": body_torso_yaw_default,
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
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 1000,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": -0.4,
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
                    "time": tag_time + 1400,
                    "data": {
                        "body.head.pitch": head_pitch_default,
                        "body.head.yaw": head_yaw_default,
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


def arm_gesture_1(
    tag_positions: List[Dict[str, Union[str, int]]],
) -> List[Dict[str, Union[int, Dict[str, float]]]]:
    """Generate frames for the first type of arm gesture at specified positions.
    Randomly chooses between raising left or right arm.

    Args:
        tag_positions (List[Dict[str, Union[str, int]]]): List of dictionaries containing tag type and position information

    Returns:
        List[Dict[str, Union[int, Dict[str, float]]]]: List of animation frames for the arm gestures
    """
    raise_left = random.choice([True, False])

    right_upper = -0.7
    right_lower = -0.8
    left_upper = arms_upper_default
    left_lower = arms_lower_default
    if raise_left:
        left_upper = -0.7
        left_lower = -0.8
        right_upper = arms_upper_default
        right_lower = arms_lower_default

    frames = []
    for tag in tag_positions:
        if tag["tag"] == "beat_1":
            tag_time = get_tag_time(tag["start_position"])
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
                        "body.torso.yaw": body_torso_yaw_default,
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
                        "body.arms.right.upper.pitch": right_upper,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": left_upper,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 800,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": right_upper,
                        "body.arms.right.lower.roll": right_lower,
                        "body.arms.left.upper.pitch": left_upper,
                        "body.arms.left.lower.roll": left_lower,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 1200,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": right_upper,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": left_upper,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 1600,
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


def arm_gesture_2(
    tag_positions: List[Dict[str, Union[str, int]]],
) -> List[Dict[str, Union[int, Dict[str, float]]]]:
    """Generate frames for the second type of arm gesture at specified positions.
    Includes random torso movement and arm positions.

    Args:
        tag_positions (List[Dict[str, Union[str, int]]]): List of dictionaries containing tag type and position information

    Returns:
        List[Dict[str, Union[int, Dict[str, float]]]]: List of animation frames for the arm gestures
    """
    frames = []
    # random torso movement
    random_torso = random.uniform(0.3, -0.3)
    # random upper hand
    random_upper_hand = random.uniform(-1.4, -1.2)
    # random lower hand
    random_lower_hand = random.uniform(-1.2, -0.8)
    for tag in tag_positions:
        if tag["tag"] == "beat_2":
            tag_time = get_tag_time(tag["start_position"])
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


def celebration(
    tag_positions: List[Dict[str, Union[str, int]]],
) -> List[Dict[str, Union[int, Dict[str, float]]]]:
    """Generate frames for celebration gestures at specified positions.
    Creates an enthusiastic raising both arms motion.

    Args:
        tag_positions (List[Dict[str, Union[str, int]]]): List of dictionaries containing tag type and position information

    Returns:
        List[Dict[str, Union[int, Dict[str, float]]]]: List of animation frames for the celebration gestures
    """
    frames = []

    for tag in tag_positions:
        if tag["tag"] == "yippee":
            tag_time = get_tag_time(tag["start_position"])
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
                    "time": tag_time + 1200,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": -2.5,
                        "body.arms.right.lower.roll": -0.1,
                        "body.arms.left.upper.pitch": -2.5,
                        "body.arms.left.lower.roll": -0.1,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 2800,
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


def confused(
    tag_positions: List[Dict[str, Union[str, int]]],
) -> List[Dict[str, Union[int, Dict[str, float]]]]:
    """Generate frames for confused gestures at specified positions.
    Creates a sequence of head tilts and arm movements indicating confusion.

    Args:
        tag_positions (List[Dict[str, Union[str, int]]]): List of dictionaries containing tag type and position information

    Returns:
        List[Dict[str, Union[int, Dict[str, float]]]]: List of animation frames for the confused gestures
    """
    frames = []
    step_size = 400
    big_step_size = 800

    for tag in tag_positions:
        if tag["tag"] == "confused":
            tag_time = int((tag["start_position"] / 4) * 1000)
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
                    "time": tag_time + big_step_size,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": -2.2,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + big_step_size + step_size,
                    "data": {
                        "body.head.yaw": -0.3,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": -2.4,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + big_step_size + 2 * step_size,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": -2.2,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + big_step_size + 3 * step_size,
                    "data": {
                        "body.head.yaw": -0.3,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": -2.4,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + big_step_size + 4 * step_size,
                    "data": {
                        "body.head.yaw": head_yaw_default,
                        "body.head.pitch": head_pitch_default,
                        "body.head.roll": head_roll_default,
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.arms.left.upper.pitch": -2.2,
                        "body.arms.left.lower.roll": arms_lower_default,
                        "body.torso.yaw": body_torso_yaw_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + big_step_size + 4 * step_size + big_step_size,
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


def make_gestures(
    tag_positions: Optional[List[Dict[str, Union[str, int]]]] = None,
) -> List[Dict[str, Union[int, Dict[str, float]]]]:
    """Combine all gesture types into a single animation sequence.

    Args:
        tag_positions (Optional[List[Dict[str, Union[str, int]]]], optional): List of dictionaries containing tag type
            and position information. Defaults to None.

    Returns:
        List[Dict[str, Union[int, Dict[str, float]]]]: Combined and sorted list of animation frames for all gestures
    """
    frames = []
    if tag_positions is None:
        return []

    frames.extend(arm_gesture_1(tag_positions))
    frames.extend(arm_gesture_2(tag_positions))
    frames.extend(nod(tag_positions))
    frames.extend(shake_head(tag_positions))
    frames.extend(confused(tag_positions))
    frames.extend(celebration(tag_positions))

    frames = sorted(frames, key=lambda frame: frame["time"])

    # Legacy code for handling negative times, not used in the current implementation but
    # might be useful in the future if some gestures are not working as expected 
    # (also it's funny so we wanted to keep it in)

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
