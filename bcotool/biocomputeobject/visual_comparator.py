import json
import cairo
from visualcomparatorerrors import VisualComparatorError, RGBNotInRangeError, ValueOutOfRange
import numpy as np
import cv2
import os

class VisualComparator:
    #
    # Default values
    #

    # Canvas Defaults
    WIDTH = 800
    HEIGHT = 1800

    # Connector Defaults
    CONNECTOR_LINE_WIDTH = 0.6
    CONNECTOR_LINE_COLOR = (0., 0., 0.)  # Black

    # Step box defaults
    STEP_BOX_COLOR = (255, 255, 255)  # White
    STEP_BOX_WIDTH = 200
    STEP_BOX_HEIGHT = 100

    # Text defaults
    TEXT_COLOR = (0, 0, 0)  # Black

    # Global level to keep track of stack drawing
    GLOBAL_LEVEL = 0
    VERTICAL_SPACE = 20

    class BCOVisualization:
        """
        Helper class, keeps ordering for BCO visualizations (the columns)
        """
        current_level = 0
        current_step = 0  # this might be redundant with current level; not sure yet
        box_coordinates = []
        connector_lines = []
        bco_object = None
        last_y_position = 0
        x_index = None

        def __init__(self, bco, column, box_width, margin):
            self.bco_object = bco
            self.column = column
            self.margin = margin
            self.box_width = box_width
            # set x index based on which column
            self.x_index = self.margin + (column * (box_width + margin))

        def add_level(self):
            pass

    # TODO: Need to merge with the BCO_Class implementation - specifically should take in the outputList
    #       returned in the alignSteps function.
    # TODO: Need to update BCO_Class to return more information in the alignSteps function (bco IDs etc.)
    def __init__(self, bco_overlap_list: list, width: int = None, height: int = None, file_name: str = "comparison.png"):
        """

        :param width: Canvas width in pixels
        :param height: Canvas height in pixels
        """

        self.bco_overlap_list = bco_overlap_list[0]
        self.bco_pipeline_tool_types = bco_overlap_list[1:]
        # print(self.bco_pipeline_tool_types)
        self.bco_pipeline_tool_types1 = bco_overlap_list[1]
        self.bco_pipeline_tool_types2 = bco_overlap_list[2]

        # Placeholder until we deal with BCO ids.
        self.bco_visualizations = {}

        # Use until replaced with above
        self._bco_visualizations = []

        # Temp: Assume a list of two for the moment
        # self.bco_ids = [1, 2]
        for idx, bco in enumerate(self.bco_pipeline_tool_types):
            # self.bco_visualizations[bco["object_id"]] = self.BCOVisualization(bco)
            print("BCO {}: {}".format(idx, bco))
            self._bco_visualizations.append(self.BCOVisualization(bco, column=idx, box_width=200, margin=20))

        if width is not None:
            self.WIDTH = width
        if height is not None:
            self.HEIGHT = height

        # Save the filename we will use
        # NOTE: For the moment we only support PNGs (native for pycairo)
        #       This could be changed if needed, but will require conversion
        #       code.

        splt = os.path.splitext(file_name)
        if splt[-1].lower() != "png":
            self.file_name = splt[0] + ".png"
        else:
            self.file_name = file_name

        # Construct the surface
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.WIDTH, self.HEIGHT)
        # Construct the context
        self.ctx = cairo.Context(self.surface)

    def visualize(self):
        """

        :return:
        """
        # TODO: Draw BCO Object IDs

        # Construct Graph
        # Assuming overlapping steps are in order
        overlap_idx = []
        for tool in self.bco_overlap_list:
            overlap_idx.append({
                "loc1": self.bco_pipeline_tool_types1.index(tool),
                "loc2": self.bco_pipeline_tool_types2.index(tool)
            })
        print("OVERLAP {}".format(self.bco_overlap_list))

        for idx, overlap in enumerate(overlap_idx):
            print("OVERLAP {}".format(idx))
            if overlap["loc1"] == overlap["loc2"]:
                while self.GLOBAL_LEVEL <= overlap["loc1"]:
                    [self._add_box(bco, self.GLOBAL_LEVEL) for bco in self._bco_visualizations]
                    self.GLOBAL_LEVEL += 1
            else:
                # 1. Need to bring loc1 up to overlap step
                while self._bco_visualizations[0].current_step < overlap["loc1"]:
                    # TODO: I don't like how this is hard coded for the first visualization
                    # print(" ADDing 1: Level {}: Global: {}".format(self._bco_visualizations[0].current_level, self.GLOBAL_LEVEL))
                    self._add_box(self._bco_visualizations[0], self.GLOBAL_LEVEL)
                    self.GLOBAL_LEVEL += 1

                # 2. Need to bring loc2 up to overlap step
                while self._bco_visualizations[1].current_step < overlap["loc2"]:
                    # TODO: I don't like how this is hard coded for the first visualization
                    # print(" ADDing 2: Level {}: Global: {}".format(self._bco_visualizations[1].current_level, self.GLOBAL_LEVEL))
                    self._add_box(self._bco_visualizations[1], self.GLOBAL_LEVEL)
                    # tmp_global += 1
                    self.GLOBAL_LEVEL += 1

                # 3. need to draw overlap at same global level
                # print("ADDIing Global: {} -> obj 1 {}: obj 2 {}".format(self.GLOBAL_LEVEL, self._bco_visualizations[0].current_level,self._bco_visualizations[1].current_level))
                [self._add_box(bco, self.GLOBAL_LEVEL) for bco in self._bco_visualizations]
                self.GLOBAL_LEVEL += 1

        # Write out any remaining steps.
        while self._bco_visualizations[0].current_step < len(self._bco_visualizations[0].bco_object):
            self._add_box(self._bco_visualizations[0], self.GLOBAL_LEVEL)
            self.GLOBAL_LEVEL += 1

        while self._bco_visualizations[1].current_step < len(self._bco_visualizations[1].bco_object):
            self._add_box(self._bco_visualizations[1], self.GLOBAL_LEVEL)
            self.GLOBAL_LEVEL += 1


        # elif overlap["loc1"] > overlap["loc2"]:
            #     # TODO this can be done more cleverly - duplicated from above basically
            #     # 1. Need to bring loc1 up to overlap step
            #     tmp_global = self.GLOBAL_LEVEL
            #     while tmp_global < overlap["loc1"]:
            #         # TODO: I don't like how this is hard coded for the first visualization
            #         self._add_box(self._bco_visualizations[0], tmp_global)
            #         tmp_global += 1
            #
            #     # 2. Need to bring loc2 up to overlap step
            #     tmp_global = self.GLOBAL_LEVEL
            #     while tmp_global < overlap["loc2"]:
            #         # TODO: I don't like how this is hard coded for the first visualization
            #         self._add_box(self._bco_visualizations[1], tmp_global)
            #         tmp_global += 1
            #
            #     # 3. need to draw overlap at same global level
            #     self.GLOBAL_LEVEL = tmp_global
            #     while self.GLOBAL_LEVEL <= overlap["loc2"]:
            #         [self._add_box(bco, self.GLOBAL_LEVEL) for bco in self._bco_visualizations]
            #         self.GLOBAL_LEVEL += 1


            # for bco_id, bco in self._bco_visualizations:
            #     if idx == bco.current_step:
            #         # Go ahead and draw at global level
            #         pass
            #     elif idx > bco.current_step:
            #         # need to draw to catch up.  draw all steps up to idx
            #         pass
            #     else:
            #         # Error state, shouldn't get
            #         print("This is an error state; shouldn't get here!")
            #
            # self.GLOBAL_LEVEL

        # for idx1, tool1 in enumerate(self.bco_pipeline_tool_types1):
        #     for idx2, tool2 in enumerate(self.bco_pipeline_tool_types2):
        #
        #
        #     if tool in self.bco_overlap_list:
        #         # They overlap; draw both boxes at same level
        #         pass
        # self.bco_overlap_list
        # self.bco_pipeline_tool_types1
        # self.bco_pipeline_tool_types2

    #################################################################################
    # Settings functions
    #################################################################################
    def set_step_box_color(self, red: int, green: int, blue: int) -> tuple:
        """
        Sets the color of the Step Box in RGB space

        :param red: 0-255 Red value
        :param green: 0-255 Green value.
        :param blue: 0-255 Blue value.
        :return: Tuple of RGB values
        """
        if not 0 < red > 255:
            # Red is outside normal boundary, throw error
            raise RGBNotInRangeError("red", red)
        if not 0 < green > 255:
            # Green is outside normal boundary, throw error
            raise RGBNotInRangeError("green", green)
        if not 0 < blue > 255:
            # Blue is outside normal boundary, throw error
            raise RGBNotInRangeError("blue", blue)

        self.STEP_BOX_COLOR = (red, green, blue)
        return self.STEP_BOX_COLOR

    # TODO: This is redundant with the above function; should combine the error handling
    def set_connector_line_color(self, red: int, green: int, blue: int) -> tuple:
        """
        Sets the color of the Connector Line in RGB space

        :param red: 0-255 Red value
        :param green: 0-255 Green value.
        :param blue: 0-255 Blue value.
        :return: Tuple of RGB values
        """
        if not 0 < red > 255:
            # Red is outside normal boundary, throw error
            raise RGBNotInRangeError("red", red)
        if not 0 < green > 255:
            # Green is outside normal boundary, throw error
            raise RGBNotInRangeError("green", green)
        if not 0 < blue > 255:
            # Blue is outside normal boundary, throw error
            raise RGBNotInRangeError("blue", blue)

        self.CONNECTOR_LINE_COLOR = (red, green, blue)
        return self.CONNECTOR_LINE_COLOR

    def set_connector_line_width(self, width):
        """
        Sets the connector line width.  Default is 0.6

        :param width: Width value in pixels.
        :return: Width value set.
        """
        if width < 0:
            raise ValueOutOfRange(message="The line width of the connector cannot be negative.")

        # TODO: not putting an upper limit.
        self.CONNECTOR_LINE_WIDTH = width

    #################################################################################
    # Internal functions
    #################################################################################
    def _draw_rectangle(self, x: int, y: int, width: int, height: int):
        """
        Draws a rectangle in the context

        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        """

        self.ctx.set_source_rgb(*self.STEP_BOX_COLOR)
        self.ctx.rectangle(x, y, width, height)
        self.ctx.fill()

    def _draw_vertical_line(self, x: float, y: float, length: float) -> None:
        """
        Helper function to draw vertical (connector) lines

        :param x: Start x coordinate (pixels).
        :param y: Start y coordinate (pixels).
        :param length: Length of the line in pixels.
        :return: None
        """

        self.ctx.move_to(x, y)
        self.ctx.line_to(x, y + length)
        self.ctx.set_source_rgb(*self.CONNECTOR_LINE_COLOR)
        self.ctx.set_line_width(self.CONNECTOR_LINE_WIDTH)
        self.ctx.stroke()

    def _draw_text(self, x: float, y: float, text: str, font_size: int) -> None:
        self.ctx.set_source_rgb(*self.TEXT_COLOR)
        self.ctx.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL,
                                  cairo.FONT_WEIGHT_NORMAL)
        # TODO: Not sure what size here...don't have good scaling
        self.ctx.set_font_size(font_size)
        self.ctx.move_to(x, y)
        self.ctx.show_text(text)

    def _add_box(self, bco, level):
        """
        Adds a new display box for a BCO
        :return:
        """

        # Need to first draw connector line if not at level 0 (special case)
        #    If the current level of the bco is behind the global level, need to draw
        #    connector to the proper level
        # TODO: Draw connector
        #
        # if level is not 0:
        #     _draw_connector()

        # Calculate box top left coordinate
        x = bco.x_index
        y = bco.last_y_position + self.VERTICAL_SPACE
        if level != bco.current_level:
            difference = level - bco.current_level
            y = (self.VERTICAL_SPACE + self.STEP_BOX_HEIGHT) * difference + y

        self._draw_rectangle(x=x, y=y, width=self.STEP_BOX_WIDTH, height=self.STEP_BOX_HEIGHT)

        # Add Text
        text = bco.bco_object[bco.current_step]
        self._draw_text(x=x + 10, y=y + 10, text=text, font_size=16)

        # Update last y position
        bco.last_y_position = y + self.STEP_BOX_HEIGHT

        # Increment BCO current level
        bco.current_level = level + 1
        # Increment BCO current step
        bco.current_step += 1

    def finalize(self):
        self.surface.write_to_png(self.file_name)

    def show(self):
        buf = self.surface.get_data()
        array = np.ndarray (shape=(self.HEIGHT, self.WIDTH, 4), dtype=np.uint8, buffer=buf)
        cv2.imshow("Comparison", array)
        cv2.waitKey(0)
        cv2.destroyAllWindows()