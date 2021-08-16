# Author: Mingyu Ding
# Time: 17/8/2021 1:37 AM
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

import cv2
data_root = '/home/zfchen/code/output/render_output_vislab3/v16/render/causal_sim/'
ref_root = '/home/zfchen/code/output/render_output_vislab3/v16/render/reference/'
for index in range(10000):
    videoWriter = cv2.VideoWriter(f'clevrer_video_ref/video{index}.mp4', cv2.VideoWriter_fourcc(*'XVID'), 25, (480, 320))
    for i in range(125):
        frame = cv2.imread(f'{data_root}sim_{index:05d}/frames/frame_%05d.png' % i, -1)
        videoWriter.write(frame[:, :, :3])
    for i in range(50):
        frame = cv2.imread(f'{ref_root}sim_{index:05d}/0/frames/frame_%05d.png' % i, -1)
        videoWriter.write(frame[:, :, :3])
    for i in range(50):
        frame = cv2.imread(f'{ref_root}sim_{index:05d}/1/frames/frame_%05d.png' % i, -1)
        videoWriter.write(frame[:, :, :3])
    for i in range(50):
        frame = cv2.imread(f'{ref_root}sim_{index:05d}/2/frames/frame_%05d.png' % i, -1)
        videoWriter.write(frame[:, :, :3])
    for i in range(50):
        frame = cv2.imread(f'{ref_root}sim_{index:05d}/3/frames/frame_%05d.png' % i, -1)
        videoWriter.write(frame[:, :, :3])
    videoWriter.release()
    videoWriter = None
    print(index)
