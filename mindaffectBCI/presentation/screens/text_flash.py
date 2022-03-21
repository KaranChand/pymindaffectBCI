#!/usr/bin/env python3
#  Copyright (c) 2019 MindAffect B.V. 
#  Author: Jason Farquhar <jadref@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pyglet
import mindaffectBCI.presentation.selectionMatrix as selectionMatrix
from mindaffectBCI.noisetag import Noisetag
from mindaffectBCI.decoder.utils import search_directories_for_file
import os

class TextFlashScreen(selectionMatrix.SelectionGridScreen):
    """variant of SelectionGridScreen which changes the text on 'flash' rather than luminosity
    """  
    def __init__(self, window, noisetag, symbols, scale_to_fit:bool=True, color_labels:bool=True, **kwargs):
        self.scale_to_fit = scale_to_fit
        self.color_labels = color_labels
        super().__init__(window,noisetag,symbols=symbols,**kwargs)

    def init_target(self, symb, x, y, w, h, i, j, font_size:int=None):
        # make list of strings for the different state-dependent strings
        symbs = symb.split("|")
        sprite = [self.init_label(symb,x,y,w,h,font_size) for symb in symbs]

        # get the label
        symb = symbs[0] if len(symbs)>1 else symb
        label= self.init_label(symb,x,y,w,h,1)

        return sprite, label

    def update_object_state(self, idx:int, state):
        if self.objects[idx]:
            # make text black when "off", white otherwise.. 
            for sprite in self.objects[idx]:
                sprite.color = (0,0,0,0)
            img_idx = state if len(self.objects[idx])>1 and state<len(self.objects[idx]) else 0
            self.objects[idx][img_idx].color = (255,255,255,255)
            #self.objects[idx][img_idx].color = self.state2color[state]
        if self.labels[idx]:
            col = self.state2color.get(state,(255,255,255,255)) if self.color_labels else (255,255,255,255)
            self.labels[idx].color=  col if len(col)==4 else col+(255,) #(255,255,255,255) # reset labels

if __name__ == "__main__":
    args = selectionMatrix.parse_args()
    setattr(args,'symbols','prva.txt')
    setattr(args,'stimfile','6blk_rand_pr.txt')
    setattr(args,'framesperbit',4)
    setattr(args,'calibration_screen','mindaffectBCI.examples.presentation.image_flash.ImageFlashScreen')
    setattr(args,'calibration_screen_args', dict(font_size=20))
    setattr(args,"extra_screens",["mindaffectBCI.examples.presentation.image_flash.ImageFlashScreen",
                          "mindaffectBCI.examples.presentation.image_flash.ImageFlashScreen",
                          "mindaffectBCI.examples.presentation.image_flash.ImageFlashScreen"])
    setattr(args,"extra_stimseqs",["6blk_rand_pr.txt","6blk_sweep_pr.txt","6blk_rand.txt"])
    setattr(args,"extra_screen_args",[dict(font_size=10, scale_to_fit=False, color_labels=False)])

    selectionMatrix.run(**vars(args))
