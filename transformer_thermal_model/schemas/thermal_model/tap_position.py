from pydantic import BaseModel


class TapPosition(BaseModel):
    """A class that defines a tap position and the corresponding load loss."""

    tap_position: int
    load_loss: float | None
