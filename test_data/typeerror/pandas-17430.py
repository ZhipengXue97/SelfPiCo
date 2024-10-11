data = data.to_frame(name=label)
numeric_data = data._convert(datetime=True)._get_numeric_data()