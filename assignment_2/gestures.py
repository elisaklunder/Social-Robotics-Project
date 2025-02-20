from alpha_mini_rug import movements

arms_upper_default = 0.1
arms_lower_default = -1.0

def nod(tag_positions=None):
    frames = []
    frames.append({"time": 0, "data": {"body.head.pitch": 0.0}})
    for tag in tag_positions:
        tag_time = int((tag["syllable_position"] / 4) * 1000)
        frames.append({"time": tag_time - 400, "data": {"body.head.pitch": 0.0}})
        frames.append({"time": tag_time, "data": {"body.head.pitch": -0.1}})
        frames.append({"time": tag_time + 400, "data": {"body.head.pitch": 0.0}})
    frames.append({"time": 0, "data": {"body.head.pitch": 0.0}})
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


def arm_gesture_1(tag_positions=None):
    frames = []
    frames.append(
        {
            "time": 0,
            "data": {
                "body.arms.right.upper.pitch": arms_upper_default,
                "body.arms.right.lower.roll": arms_lower_default,
            },
        }
    )
    for tag in tag_positions:
        if tag["tag"] == "arms":
            tag_time = int((tag["syllable_position"] / 4) * 1000)
            frames.append(
                {
                    "time": tag_time - 800,
                    "data": {
                        "body.arms.right.upper.pitch": -0.5,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time - 400,
                    "data": {
                        "body.arms.right.upper.pitch": -0.5,
                        "body.arms.right.lower.roll": -0.8,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time,
                    "data": {
                        "body.arms.right.upper.pitch": -0.5,
                        "body.arms.right.lower.roll": arms_lower_default,
                    },
                }
            )
            frames.append(
                {
                    "time": tag_time + 400,
                    "data": {
                        "body.arms.right.upper.pitch": arms_upper_default,
                        "body.arms.right.lower.roll": -arms_lower_default,
                    },
                }
            )
            
    return frames


def arm_gesture_2(self):
    pass


def emotional_gesture(self):
    pass


def make_gestures(tag_positions=None):
    frames = arm_gesture_1(tag_positions)
    return frames
