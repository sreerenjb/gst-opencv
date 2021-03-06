#!/usr/bin/env python
import pygst
pygst.require("0.10")
import gst
import gtk

class FaceDetect:

	def __init__(self):
		pipe = """filesrc location=mike-boat.jpg ! decodebin ! ffmpegcolorspace ! facedetect ! ffmpegcolorspace ! ximagesink"""
		self.pipeline = gst.parse_launch(pipe)
	
		self.bus = self.pipeline.get_bus()
		self.bus.add_signal_watch()
		self.bus.connect("message::element", self.bus_message)

		self.pipeline.set_state(gst.STATE_PLAYING)

	def bus_message(self, bus, message):
		st = message.structure
		if st.get_name() == "face":
			print "Face found at %d,%d with dimensions %dx%d" % (st["x"], st["y"], st["width"], st["height"])

if __name__ == "__main__":
	f = FaceDetect()
	gtk.main()
