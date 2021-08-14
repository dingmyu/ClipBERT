# Author: Mingyu Ding
# Time: 14/8/2021 5:53 PM
# Copyright 2019. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os
data_root = '/home/zfchen/code/output/render_output_vislab3/v16/render/causal_sim/'
for index in range(10000):
    os.system(f'ffmpeg -framerate 25 -loop 0 -f image2 -i {data_root}sim_{index:05d}/frames/frame_%05d.png'
              ' -pix_fmt yuv420p -vcodec libx264 -crf 23 clevrer_video/video{index}.mp4')
    break
