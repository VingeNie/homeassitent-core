"""Ecovacs test util."""


import asyncio

from deebot_client.event_bus import EventBus
from deebot_client.events import Event

from homeassistant.core import HomeAssistant


async def notify_and_wait(
    hass: HomeAssistant, event_bus: EventBus, event: Event
) -> None:
    """Block till done."""
    event_bus.notify(event)
    await asyncio.gather(*event_bus._tasks)
    await hass.async_block_till_done()
