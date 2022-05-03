import _plotly_utils.basevalidators


class GriddashValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="griddash", parent_name="layout.ternary.baxis", **kwargs
    ):
        super(GriddashValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop(
                "values", ["solid", "dot", "dash", "longdash", "dashdot", "longdashdot"]
            ),
            **kwargs,
        )