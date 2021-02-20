import color_gradient


class TestFadeColors:
    def setup_method(self):
        self.fade = color_gradient.FadeColors(["602767", "9f1244"])

    def test_hex2rgb(self):
        hexs = [
            {"hex": "8237de", "rgb": (130, 55, 222)},
            {"hex": "cc37de", "rgb": (204, 55, 222)},
            {"hex": "129f19", "rgb": (18, 159, 25)},
        ]
        for h in hexs:
            assert color_gradient.FadeColors.hex2rgb(h["hex"]) == h["rgb"]

    def test_get_channels(self):
        rgbs = [(130, 55, 222), (204, 55, 222), (18, 159, 25)]
        r, g, b = color_gradient.FadeColors.get_channels(rgbs)
        assert r == [130, 204, 18]
        assert g == [55, 55, 159]
        assert b == [222, 222, 25]

    def test_find_slope(self):
        point_pair_collection = [
            {"points": (0, 2, 4, 5), "slope": 0.75},
            {"points": (0, 1, 2, 2), "slope": 0.5},
            {"points": (-2, 1, 1, 2), "slope": 0.3333333333333333},
        ]
        for point in point_pair_collection:
            slope = color_gradient.FadeColors.find_slope(*point["points"])
            assert slope == point["slope"]

    def test_part(self):
        parts = [{"num": 1.4, "parts": (1, 2)}]
        for part in parts:
            assert color_gradient.FadeColors.part(part["num"]) == part["parts"]

    def test_find_y(self):
        x_values = [0, 0.1, 0.2, 1]
        r_y = [96, 102, 109, 159]
        for num, value in enumerate(x_values):
            y = self.fade.find_y(value, self.fade.red)
            assert r_y[num] == y
        g_y = [39, 37, 35, 18]
        for num, value in enumerate(x_values):
            y = self.fade.find_y(value, self.fade.green)
            assert g_y[num] == y
        b_y = [103, 100, 96, 68]
        for num, value in enumerate(x_values):
            y = self.fade.find_y(value, self.fade.blue)
            assert b_y[num] == y

    def test_get_rgb(self):
        rgbs = [(96, 39, 103), (109, 35, 96), (115, 33, 92), (159, 18, 68)]
        for num, x in enumerate([0, 0.2, 0.3, 1]):
            assert self.fade.get_rgb(x) == rgbs[num]
