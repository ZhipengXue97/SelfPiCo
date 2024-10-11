state = self.async_get_last_state()
value = state and state.state
# Check against None because value can be 0
if value is not None and self._minimum <= len(value) <= self._maximum:
    self._current_value = value