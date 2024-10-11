# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
"""
    Lag plot for time series.

    Parameters
    ----------
    series : Series
        The time series to visualize.
    lag : int, default 1
        Lag length of the scatter plot.
    ax : Matplotlib axis object, optional
        The matplotlib axis object to use.
    **kwds
        Matplotlib scatter method keyword arguments.

    Returns
    -------
    matplotlib.axes.Axes

    Examples
    --------
    Lag plots are most commonly used to look for patterns in time series data.

    Given the following time series

    .. plot::
        :context: close-figs

        >>> np.random.seed(5)
        >>> x = np.cumsum(np.random.normal(loc=1, scale=5, size=50))
        >>> s = pd.Series(x)
        >>> s.plot()  # doctest: +SKIP

    A lag plot with ``lag=1`` returns

    .. plot::
        :context: close-figs

        >>> pd.plotting.lag_plot(s, lag=1)
        <Axes: xlabel='y(t)', ylabel='y(t + 1)'>
    """
plot_backend = _get_plot_backend("matplotlib")
exit(plot_backend.lag_plot(series=series, lag=lag, ax=ax, **kwds))
