from echarts.base import Base

class Line(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)
        self._option.update(series=[], legend={"data":[]})

    def add(self, name, x_axis, y_axis, **kwargs):
        if isinstance(x_axis, list) and isinstance(y_axis, list):
            assert len(x_axis) == len(y_axis)
            kwargs.update(x_axis=x_axis)
            xaxis, yaxis = Base._xy_axis(**kwargs)
            self._option.update(xAxis=xaxis, yAxis=yaxis)
            self._option.get('legend').get('data').append(name)
            self._option.get('series').append({
                "name": name,
                "smooth": kwargs.get('smooth', False),
                "type": "line",
                "data": y_axis,
                "label": Base._label(**kwargs),
                "markPoint": Base._markpoint(**kwargs)
            })
            self._option.update(color=Base._color(**kwargs))
        else:
            raise ValueError

    def config(self):
        pass


attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value_A = [5, 20, 36, 10, 10, 100]
value_B = [55, 60, 16, 14, 15, 80]

if __name__ == "__main__":
    line = Line("岗位地点分布折线图", "")
    line.add("商家A", attr, value_A, markpoint=("max", "min", "average"))
    line.add("商家B", attr, value_B, markpoint=("max", "min", "average"))
    line.show_config()
    line.render()