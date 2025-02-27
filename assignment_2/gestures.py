from alpha_mini_rug import movements

arms_upper_default = -0.4
arms_lower_default = -1.0
body_head_pitch_default = 0.0
body_head_yaw_default = 0.0

def nod(frames, tag_positions=None):
    for tag in tag_positions:
        if tag["tag"] != "nod":
            continue
        tag_time = int((tag["syllable_position"] / 4) * 1000)
        frames.append(
            {
                "time": tag_time - 400,
                "data": {
                    "body.head.pitch": body_head_pitch_default,
                    "body.arms.right.upper.pitch": arms_upper_default,
                    "body.arms.right.lower.roll": arms_lower_default,
                },
            }
        )
        frames.append(
            {
                "time": tag_time,
                "data": {
                    "body.head.pitch": -0.1,
                    "body.arms.right.upper.pitch": arms_upper_default,
                    "body.arms.right.lower.roll": arms_lower_default,
                },
            }
        )
        frames.append(
            {
                "time": tag_time + 400,
                "data": {
                    "body.head.pitch": body_head_pitch_default,
                    "body.arms.right.upper.pitch": arms_upper_default,
                    "body.arms.right.lower.roll": arms_lower_default,
                },
            }
        )
    return frames


def shake_head(self):
    # Shake no
    # yaw
    yield movements.perform_movement(
        self.session,
        frames=[
            {"time": 400, "data": {"body.head.yaw": 0.1}},
            {"time": 1200, "data": {"body.head.yaw": -0.1}},
            {"time": 2000, "data": {"body.head.yaw": 0.1}},
            {"time": 2400, "data": {"body.head.yaw": 0.0}},
        ],
        force=True,
    )


def arm_gesture_1(frames, tag_positions=None):
    for tag in tag_positions:
        if tag["tag"] == "arms":
            tag_time = int((tag["syllable_position"] / 4) * 1000)
            frames.append(
                {
                    "time": tag_time - 1200,
                    "data": {
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.head.pitch": body_head_pitch_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time - 800,
                    "data": {
                        "body.arms.right.upper.pitch": -0.7,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.head.pitch": body_head_pitch_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time - 400,
                    "data": {
                        "body.arms.right.upper.pitch": -0.7,
                        "body.arms.right.lower.roll": -0.8,
                        "body.head.pitch": body_head_pitch_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time,
                    "data": {
                        "body.arms.right.upper.pitch": -0.7,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.head.pitch": body_head_pitch_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 400,
                    "data": {
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": arms_lower_default,
                        "body.head.pitch": body_head_pitch_default,
                    },
                }
            )

    return frames


def arm_gesture_2(self):
    pass


def emotional_gesture(self):
    pass


def make_gestures(tag_positions=None):
    frames = []
    frames = arm_gesture_1(frames, tag_positions)
    frames = nod(frames, tag_positions)
    
    frames = sorted(frames, key=lambda frame: frame["time"])
    naughty_frame = frames[0]
    if naughty_frame["time"] < 0:   # if we have a negative time at the start, we need to adjust all times
        for frame in frames:
            frame["time"] -= frames[0]["time"]

    return frames, naughty_frame
