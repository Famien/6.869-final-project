import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import colorsys
import scipy
import scipy.sparse
import scipy.sparse.linalg
import logging
from scipy.misc import imread
np.set_printoptions(precision=8, suppress=True)

# set the photo file path
path_pic = 'peppers_gray.png'
path_pic_marked = 'peppers_marked.png'
# window width
wd_width = 1

pic_o_rgb = imread(path_pic)
pic_o = pic_o_rgb.astype(float)/255
pic_m_rgb = imread(path_pic_marked)
pic_m = pic_m_rgb.astype(float)/255

fig = plt.figure()
fig.add_subplot(1,2,1).set_title('Black & White')
imgplot = plt.imshow(pic_o_rgb)
fig.add_subplot(1,2,2).set_title('Color Hints')
imgplot = plt.imshow(pic_m_rgb)
plt.show();

class WindowNeighbor:
    def __init__(self, width, center, pic):
        # center is a list of [row, col, Y_intensity]
        self.center = [center[0], center[1], pic[center][0]]
        self.width = width
        self.neighbors = None
        self.find_neighbors(pic)
        self.mean = None
        self.var = None

    def find_neighbors(self, pic):
        self.neighbors = []
        ix_r_min = max(0, self.center[0] - self.width)
        ix_r_max = min(pic.shape[0], self.center[0] + self.width + 1)
        ix_c_min = max(0, self.center[1] - self.width)
        ix_c_max = min(pic.shape[1], self.center[1] + self.width + 1)
        for r in range(ix_r_min, ix_r_max):
            for c in range(ix_c_min, ix_c_max):
                if r == self.center[0] and c == self.center[1]:
                    continue
                self.neighbors.append([r,c,pic[r,c,0]])

    def __str__(self):
        return 'windows c=(%d, %d, %f) size: %d' % (self.center[0], self.center[1], self.center[2], len(self.neighbors))

# affinity functions, calculate weights of pixels in a window by their intensity.
def affinity_a(w):
    nbs = np.array(w.neighbors)
    sY = nbs[:,2]
    cY = w.center[2]
    diff = sY - cY
    sig = np.var(np.append(sY, cY))
    if sig < 1e-6:
        sig = 1e-6  
    wrs = np.exp(- np.power(diff,2) / (sig * 2.0))
    wrs = - wrs / np.sum(wrs)
    nbs[:,2] = wrs
    return nbs

# translate (row,col) to/from sequential number
def to_seq(r, c, rows):
    return c * rows + r

def fr_seq(seq, rows):
    r = seq % rows
    c = int((seq - r) / rows)
    return (r, c)

# combine 3 channels of YUV to a RGB photo: n x n x 3 array
def yuv_channels_to_rgb(cY,cU,cV):
    ansRGB = [colorsys.yiq_to_rgb(cY[i],cU[i],cV[i]) for i in range(len(ansY))]
    ansRGB = np.array(ansRGB)
    pic_ansRGB = np.zeros(pic_yuv.shape)
    pic_ansRGB[:,:,0] = ansRGB[:,0].reshape(pic_rows, pic_cols, order='F')
    pic_ansRGB[:,:,1] = ansRGB[:,1].reshape(pic_rows, pic_cols, order='F')
    pic_ansRGB[:,:,2] = ansRGB[:,2].reshape(pic_rows, pic_cols, order='F')
    return pic_ansRGB

def init_logger():
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    logger = logging.getLogger()
    return logger

log = init_logger()
(pic_rows, pic_cols, _) = pic_o.shape
pic_size = pic_rows * pic_cols

channel_Y,_,_ = colorsys.rgb_to_yiq(pic_o[:,:,0],pic_o[:,:,1],pic_o[:,:,2])
_,channel_U,channel_V = colorsys.rgb_to_yiq(pic_m[:,:,0],pic_m[:,:,1],pic_m[:,:,2])

map_colored = (abs(channel_U) + abs(channel_V)) > 0.0001

pic_yuv = np.dstack((channel_Y, channel_U, channel_V))
weightData = []
num_pixel_bw = 0

# build the weight matrix for each window.
for c in range(pic_cols):
    for r in range(pic_rows):
        res = []
        w = WindowNeighbor(wd_width, (r,c), pic_yuv)
        if not map_colored[r,c]:
            weights = affinity_a(w)
            for e in weights:
                weightData.append([w.center,(e[0],e[1]), e[2]])
        weightData.append([w.center, (w.center[0],w.center[1]), 1.])

sp_idx_rc_data = [[to_seq(e[0][0], e[0][1], pic_rows), to_seq(e[1][0], e[1][1], pic_rows), e[2]] for e in weightData]
sp_idx_rc = np.array(sp_idx_rc_data, dtype=np.integer)[:,0:2]
sp_data = np.array(sp_idx_rc_data, dtype=np.float64)[:,2]

matA = scipy.sparse.csr_matrix((sp_data, (sp_idx_rc[:,0], sp_idx_rc[:,1])), shape=(pic_size, pic_size))


b_u = np.zeros(pic_size)
b_v = np.zeros(pic_size)
idx_colored = np.nonzero(map_colored.reshape(pic_size, order='F'))
pic_u_flat = pic_yuv[:,:,1].reshape(pic_size, order='F')
b_u[idx_colored] = pic_u_flat[idx_colored]

pic_v_flat = pic_yuv[:,:,2].reshape(pic_size, order='F')
b_v[idx_colored] = pic_v_flat[idx_colored]


log.info('Optimizing Ax=b')
ansY = pic_yuv[:,:,0].reshape(pic_size, order='F')
ansU = scipy.sparse.linalg.spsolve(matA, b_u)
ansV = scipy.sparse.linalg.spsolve(matA, b_v)
pic_ans = yuv_channels_to_rgb(ansY,ansU,ansV)
log.info('Optimized Ax=b')

fig = plt.figure()
fig.add_subplot(1,2,1).set_title('Black & White')
imgplot = plt.imshow(pic_o_rgb)
fig.add_subplot(1,2,2).set_title('Colorized')
imgplot = plt.imshow(pic_ans)
plt.show();
