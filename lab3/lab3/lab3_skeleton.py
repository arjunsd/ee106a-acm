#!/usr/bin/env python
"""
Lab 3, task 1
"""


import numpy as np
import scipy as sp
import kin_func_skeleton as kfs



def lab3(theta):
    q = np.ndarray((3,8))
    w = np.ndarray((3,7))
    
    q[0:3,0] = [0.0635, 0.2598, 0.1188]
    q[0:3,1] = [0.1106, 0.3116, 0.3885]
    q[0:3,2] = [0.1827, 0.3838, 0.3881]
    q[0:3,3] = [0.3682, 0.5684, 0.3181]
    q[0:3,4] = [0.4417, 0.6420, 0.3177]
    q[0:3,5] = [0.6332, 0.8337, 0.3067]
    q[0:3,6] = [0.7152, 0.9158, 0.3063]
    q[0:3,7] = [0.7957, 0.9965, 0.3058]

    w[0:3,0] = [-0.0059,  0.0113,  0.9999]
    w[0:3,1] = [-0.7077,  0.7065, -0.0122]
    w[0:3,2] = [ 0.7065,  0.7077, -0.0038]
    w[0:3,3] = [-0.7077,  0.7065, -0.0122]
    w[0:3,4] = [ 0.7065,  0.7077, -0.0038]
    w[0:3,5] = [-0.7077,  0.7065, -0.0122]
    w[0:3,6] = [ 0.7065,  0.7077, -0.0038]

    R = np.array([[0.0076, 0.0001, -1.0000],
                          [-0.7040, 0.7102, -0.0053],
                          [0.7102, 0.7040, 0.0055]]).T

    # YOUR CODE HERE
    N = 7
    zeroConfig = np.zeros((1,N))

    
    Rq0 = np.hstack((R,q[0:3,7].reshape(3,1)))
    gst0 = np.vstack((Rq0,np.array([[0,0,0,1]])))
    #print('gst0')
    #print(gst0)


    return gst(theta, gst0, w, q)





def gst(theta, gst0, w, q):
    #theta = array of 7 joint angles
    multiplication=1
    xi_array = []
    for i in range(len(theta)):
        q_i = q[0:3,i]
        w_i = w[0:3,i]
        qw_cross = np.cross(-(w_i), q_i)
        xi_i = np.vstack((qw_cross.reshape(3,1),w_i.reshape(3,1)))
        xi_array.append(xi_i[:,0])

    xi_array = np.array(xi_array)
    #print("xi_array.shape")
    #print(xi_array.shape)
    return np.dot(kfs.prod_exp(xi_array.T, theta),gst0)

    

if __name__ == "__main__":
    #print('Lab 3')
    test = np.zeros(7)
    #print(test.shape)
    lab3(test)

