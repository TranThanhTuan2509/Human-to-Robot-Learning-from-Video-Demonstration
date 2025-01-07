import numpy as np


# Parameters for drawing figure.
display_input_size = (10, 10)
overall_fig_size = (18, 24)

# Parameters for drawing figure.
line_thickness = 1
fig_size_w = 35
# fig_size_h = min(max(5, int(len(category_names) / 2.5) ), 10)
mask_color = 'red'
alpha = 0.5

#@markdown **Global constants:** pick and place objects, colors, workspace bounds.
PIXEL_SIZE = 0.00267857 # The size of each pixel in real-world units (such as meters)

BOUNDS = np.float32([[-0.3, 0.3], [-0.8, -0.2], [0, 0.15]])  # (X, Y, Z) (width, depth, height)

COLORS = {
	'blue': (78 / 255, 121 / 255, 167 / 255, 255 / 255),
	'red': (255 / 255, 87 / 255, 89 / 255, 255 / 255),
	'green': (89 / 255, 169 / 255, 79 / 255, 255 / 255),
	'orange': (242 / 255, 142 / 255, 43 / 255, 255 / 255),
	'yellow': (237 / 255, 201 / 255, 72 / 255, 255 / 255),
	'purple': (176 / 255, 122 / 255, 161 / 255, 255 / 255),
	'pink': (255 / 255, 157 / 255, 167 / 255, 255 / 255),
	'cyan': (118 / 255, 183 / 255, 178 / 255, 255 / 255),
	'brown': (156 / 255, 117 / 255, 95 / 255, 255 / 255),
	'gray': (186 / 255, 176 / 255, 172 / 255, 255 / 255),
}

PICK_TARGETS = {
	'blue block': None,
	'red block': None,
	'green block': None,
	'orange block': None,
	'yellow block': None,
	'purple block': None,
	'pink block': None,
	'cyan block': None,
	'brown block': None,
	'gray block': None,
}

PLACE_TARGETS = {
	'blue block': None,
	'red block': None,
	'green block': None,
	'orange block': None,
	'yellow block': None,
	'purple block': None,
	'pink block': None,
	'cyan block': None,
	'brown block': None,
	'gray block': None,

	'blue bowl': None,
	'red bowl': None,
	'green bowl': None,
	'orange bowl': None,
	'yellow bowl': None,
	'purple bowl': None,
	'pink bowl': None,
	'cyan bowl': None,
	'brown bowl': None,
	'gray bowl': None,

	'top left corner':     (-0.3 + 0.05, -0.2 - 0.05, 0),
	'top side':            (0,           -0.2 - 0.05, 0),
	'top right corner':    (0.3 - 0.05,  -0.2 - 0.05, 0),
	'left side':           (-0.3 + 0.05, -0.5,        0),
	'middle':              (0,           -0.5,        0),
	'right side':          (0.3 - 0.05,  -0.5,        0),
	'bottom left corner':  (-0.3 + 0.05, -0.8 + 0.05, 0),
	'bottom side':         (0,           -0.8 + 0.05, 0),
	'bottom right corner': (0.3 - 0.05,  -0.8 + 0.05, 0),
}

single_template = [
	"a photo of {article} {}."
]

multiple_templates = [
	'There is {article} {} in the scene.',
	'There is the {} in the scene.',
	'a photo of {article} {} in the scene.',
	'a photo of the {} in the scene.',
	'a photo of one {} in the scene.',

	'itap of {article} {}.',
	'itap of my {}.',  # itap: I took a picture of
	'itap of the {}.',
	'a photo of {article} {}.',
	'a photo of my {}.',
	'a photo of the {}.',
	'a photo of one {}.',
	'a photo of many {}.',

	'a good photo of {article} {}.',
	'a good photo of the {}.',
	'a bad photo of {article} {}.',
	'a bad photo of the {}.',
	'a photo of a nice {}.',
	'a photo of the nice {}.',
	'a photo of a cool {}.',
	'a photo of the cool {}.',
	'a photo of a weird {}.',
	'a photo of the weird {}.',

	'a photo of a small {}.',
	'a photo of the small {}.',
	'a photo of a large {}.',
	'a photo of the large {}.',

	'a photo of a clean {}.',
	'a photo of the clean {}.',
	'a photo of a dirty {}.',
	'a photo of the dirty {}.',

	'a bright photo of {article} {}.',
	'a bright photo of the {}.',
	'a dark photo of {article} {}.',
	'a dark photo of the {}.',

	'a photo of a hard to see {}.',
	'a photo of the hard to see {}.',
	'a low resolution photo of {article} {}.',
	'a low resolution photo of the {}.',
	'a cropped photo of {article} {}.',
	'a cropped photo of the {}.',
	'a close-up photo of {article} {}.',
	'a close-up photo of the {}.',
	'a jpeg corrupted photo of {article} {}.',
	'a jpeg corrupted photo of the {}.',
	'a blurry photo of {article} {}.',
	'a blurry photo of the {}.',
	'a pixelated photo of {article} {}.',
	'a pixelated photo of the {}.',

	'a black and white photo of the {}.',
	'a black and white photo of {article} {}.',

	'a plastic {}.',
	'the plastic {}.',

	'a toy {}.',
	'the toy {}.',
	'a plushie {}.',
	'the plushie {}.',
	'a cartoon {}.',
	'the cartoon {}.',

	'an embroidered {}.',
	'the embroidered {}.',

	'a painting of the {}.',
	'a painting of a {}.',
]

category_names = ['blue block',
				  'red block',
				  'green block',
				  'orange block',
				  'yellow block',
				  'purple block',
				  'pink block',
				  'cyan block',
				  'brown block',
				  'gray block',

				  'blue bowl',
				  'red bowl',
				  'green bowl',
				  'orange bowl',
				  'yellow bowl',
				  'purple bowl',
				  'pink bowl',
				  'cyan bowl',
				  'brown bowl',
				  'gray bowl']

# def display(self):
# 	"""Display Configuration values."""
# 	print("\nConfigurations:")
# 	print("-" * 30)
# 	for a in dir(self):
# 		if not a.startswith("__") and not callable(getattr(self, a)):
# 			print("{:30} {}".format(a, getattr(self, a)))
# 	print()