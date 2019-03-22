from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

myapp = App()

# Background
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, black)
bg = Sprite(bg_asset, (0,0))

myapp.run()
